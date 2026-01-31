from bs4 import BeautifulSoup
import requests
# import tushare as ts
import pandas as pd
import akshare as ak
from akshare.utils import demjson
from io import StringIO

# TS_TOKEN = '31e5536e4d0ffbfb47a74e9832fd35c711fdaa2405bec6559b62d22d'


class DataSource:
    def __init__(self, name=__name__):
        self.__name = name
        # self.pro=ts.pro_api(TS_TOKEN)

        # 创建会话以复用连接
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        })

    def getAllFunds(self):
        '''
        从东方财富获取易方达基金列表
        '''
        url = 'http://fund.eastmoney.com/Company/80000229.html'

        try:
            with self.session.get(url=url) as response:
                response.encoding = 'utf-8'
                html_content = response.text

            # 初始化BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # 存储数据的列表
            data = []

            # 找到所有包含name和code的td元素
            td_elements = soup.find('div', id='kfsFundNetWrap').find_all('td', class_='fund-name-code')

            for td in td_elements:
                # 提取name和code
                name_tag = td.find('a', class_='name')
                code_tag = td.find('a', class_='code')

                # 确保标签存在，避免None报错
                name = name_tag.text.strip() if name_tag else ''
                code = code_tag.text.strip() if code_tag else ''

                data.append({'name': name, 'code': code})

            # 转换为DataFrame
            df = pd.DataFrame(data)
            return df
        except:
            return None

    # 获取指定基金基本信息
    def getFundBasic(self, code):
        try:
            df = ak.fund_individual_basic_info_xq(symbol=code)
            return df
        except:
            return None

    # 获取指定基金的单位净值走势
    def getFundAssetNetValues(self, code):
        try:
            df = ak.fund_open_fund_info_em(symbol=code, indicator='单位净值走势')
            return df
        except:
            return None

    # 获取指定基金的累计净值走势
    def getFundCumulativeNetValues(self, code):
        try:
            df = ak.fund_open_fund_info_em(symbol=code, indicator='累计净值走势')
            return df
        except:
            return None

    # 获取指定基金的累计收益率走势
    # period :  {"1月", "3月", "6月", "1年", "3年", "5年", "今年来", "成立来"}
    def getFundCumulativeReturnTrend(self, code, period='成立来'):
        try:
            df = ak.fund_open_fund_info_em(symbol=code, indicator='累计收益率走势', period=period)
            return df
        except:
            return None

    # 获取指定基金的同类排名走势
    def getFundRankingTrend(self, code):
        try:
            df = ak.fund_open_fund_info_em(symbol=code, indicator='同类排名走势')
            return df
        except:
            return None

    def getFundHoldRatio(self, code, date='20251231'):
        '''
        获取指定基金的持仓比列(股票、债券、现金、其他比例)
        ak.fund_individual_detail_hold_xq

        :param self: Description
        :param code: Description
        :param date: Description
        '''
        url = "https://danjuanfunds.com/djapi/fundx/base/fund/record/asset/percent"
        params = {
            "fund_code": f"{code}",
            "report_date": f"{'-'.join([date[:4], date[4:6], date[6:]])}",
        }

        try:
            with self.session.get(url, params=params, timeout=10) as response:
                response.raise_for_status()
                data_json = response.json()
                # 处理数据前先清理响应内容
                response._content = None

            temp_df = pd.DataFrame.from_dict(data_json["data"]["chart_list"], orient="columns")
            temp_df = temp_df[
                [
                    "type_desc",
                    "percent",
                ]
            ]
            temp_df.columns = [
                "资产类型",
                "仓位占比",
            ]
            temp_df["仓位占比"] = pd.to_numeric(temp_df["仓位占比"], errors="coerce")
            return temp_df
        except requests.RequestException as e:
            print(f"getFundHoldRatio: {e}")
            return None

    def getFundHoldShare(self, code, date='2025'):
        '''
        获取指定基金的持仓股票
        ak.fund_portfolio_hold_em

        :param self: Description
        :param code: Description
        :param date: Description
        '''
        url = "https://fundf10.eastmoney.com/FundArchivesDatas.aspx"
        params = {
            "type": "jjcc",
            "code": code,
            "topline": "10000",
            "year": date,
            "month": "",
            "rt": "0.913877030254846",
        }

        try:
            with self.session.get(url, params=params, timeout=10) as response:
                response.raise_for_status()
                data_text = response.text
                data_json = demjson.decode(data_text[data_text.find("{"): -1])
                soup = BeautifulSoup(data_json["content"], features="lxml")
                item_label = [
                    item.text.split("\xa0\xa0")[1]
                    for item in soup.find_all(name="h4", attrs={"class": "t"})
                ]

            column_name = [
                "序号",
                "股票代码",
                "股票名称",
                "占净值比例",
                "持股数",
                "持仓市值",
                "季度",
            ]
            big_df = pd.DataFrame(columns=column_name)

            for item in range(len(item_label)):
                temp_df = pd.read_html(
                    StringIO(data_json["content"]), converters={"股票代码": str}
                )[item]
                del temp_df["相关资讯"]
                temp_df.rename(columns={"占净值 比例": "占净值比例"}, inplace=True)
                temp_df["占净值比例"] = (
                    temp_df["占净值比例"].str.split("%", expand=True).iloc[:, 0]
                )
                temp_df.rename(
                    columns={"持股数（万股）": "持股数", "持仓市值（万元）": "持仓市值"},
                    inplace=True,
                )
                temp_df.rename(
                    columns={"持股数 （万股）": "持股数", "持仓市值 （万元）": "持仓市值"},
                    inplace=True,
                )
                temp_df.rename(
                    columns={"持股数（万股）": "持股数", "持仓市值（万元人民币）": "持仓市值"},
                    inplace=True,
                )
                temp_df.rename(
                    columns={
                        "持股数 （万股）": "持股数",
                        "持仓市值 （万元人民币）": "持仓市值",
                    },
                    inplace=True,
                )

                temp_df["季度"] = item_label[item]
                temp_df = temp_df[column_name]
                big_df = (
                    pd.concat(objs=[temp_df, big_df], ignore_index=True)
                    if not big_df.empty
                    else temp_df
                )

            if not big_df.empty:
                big_df["占净值比例"] = pd.to_numeric(big_df["占净值比例"], errors="coerce")
                big_df["持股数"] = pd.to_numeric(big_df["持股数"], errors="coerce")
                big_df["持仓市值"] = pd.to_numeric(big_df["持仓市值"], errors="coerce")
                del big_df["序号"]
                big_df.reset_index(inplace=True, drop=False)
                big_df["index"] = big_df["index"] + 1
                big_df.rename(columns={"index": "序号"}, inplace=True)
            return big_df
        except requests.RequestException as e:
            print(f"getFundHoldShare: {e}")
            return None

    def getFundHoldBond(self, code, date='2025'):
        '''
        获取指定基金的持仓债券
        ak.fund_portfolio_bond_hold_em

        :param self: Description
        :param code: Description
        :param date: Description
        '''
        url = "https://fundf10.eastmoney.com/FundArchivesDatas.aspx"
        params = {
            "type": "zqcc",
            "code": code,
            "year": date,
            "rt": "0.913877030254846",
        }
        try:
            with self.session.get(url, params=params, timeout=10) as response:
                response.raise_for_status()
                data_text = response.text
                data_json = demjson.decode(data_text[data_text.find("{"): -1])
                soup = BeautifulSoup(data_json["content"], features="lxml")
                item_label = [
                    item.text.split("\xa0\xa0")[1]
                    for item in soup.find_all(name="h4", attrs={"class": "t"})
                ]
            big_df = pd.DataFrame()
            for item in range(len(item_label)):
                temp_df = pd.read_html(
                    StringIO(data_json["content"]), converters={"债券代码": str}
                )[item]
                temp_df["占净值比例"] = (
                    temp_df["占净值比例"].str.split("%", expand=True).iloc[:, 0]
                )
                temp_df.rename(columns={"持仓市值（万元）": "持仓市值"}, inplace=True)
                temp_df["季度"] = item_label[item]
                temp_df = temp_df[
                    [
                        "序号",
                        "债券代码",
                        "债券名称",
                        "占净值比例",
                        "持仓市值",
                        "季度",
                    ]
                ]
                big_df = pd.concat(objs=[big_df, temp_df], ignore_index=True)
            big_df["占净值比例"] = pd.to_numeric(big_df["占净值比例"], errors="coerce")
            big_df["持仓市值"] = pd.to_numeric(big_df["持仓市值"], errors="coerce")
            big_df["序号"] = range(1, len(big_df) + 1)
            return big_df
        except requests.RequestException as e:
            print(f"getFundHoldBond: {e}")
            return None

    def getFundHoldIndustry(self, code, date='2025'):
        '''
        获取指定基金的持仓行业
        ak.fund_portfolio_industry_hold_em

        :param self: Description
        :param code: Description
        :param date: Description
        '''
        url = "https://api.fund.eastmoney.com/f10/HYPZ/"
        params = {
            "fundCode": code,
            "year": date,
            "callback": "jQuery183006997159478989867_1648016188499",
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "api.fund.eastmoney.com",
            "Pragma": "no-cache",
            "Referer": "https://fundf10.eastmoney.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/99.0.4844.82 Safari/537.36",
        }
        try:

            with self.session.get(url, params=params, headers=headers, timeout=10) as response:
                response.raise_for_status()
                data_text = response.text
                data_json = demjson.decode(data_text[data_text.find("{"): -1])
                temp_list = []
                for item in data_json["Data"]["QuarterInfos"]:
                    temp_list.extend(item["HYPZInfo"])

            temp_df = pd.DataFrame(temp_list)
            temp_df.reset_index(inplace=True)
            temp_df["index"] = temp_df.index + 1
            temp_df.columns = [
                "序号",
                "-",
                "截止时间",
                "-",
                "行业类别",
                "市值",
                "-",
                "占净值比例",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
                "-",
            ]
            temp_df = temp_df[
                [
                    "序号",
                    "行业类别",
                    "占净值比例",
                    "市值",
                    "截止时间",
                ]
            ]
            temp_df["市值"] = pd.to_numeric(temp_df["市值"], errors="coerce")
            temp_df["占净值比例"] = pd.to_numeric(temp_df["占净值比例"], errors="coerce")
            return temp_df
        except requests.RequestException as e:
            print(f"getFundHoldIndustry: {e}")
            return None

    def getAnalyzeIndexData(self, symbol='市场表征', start_date='20251231', end_date='20251231'):
        try:
            df = ak.index_analysis_daily_sw(symbol=symbol, start_date=start_date, end_date=end_date)
            return df
        except:
            return None


# 全局数据源实例
fundDataSource = DataSource()
