import re
from unittest import result
from bs4 import BeautifulSoup
import requests
# import tushare as ts
import pandas as pd
import akshare as ak
from akshare.utils import demjson
from akshare.utils.tqdm import get_tqdm
from io import StringIO
import py_mini_racer
import math
import json

# TS_TOKEN = '31e5536e4d0ffbfb47a74e9832fd35c711fdaa2405bec6559b62d22d'


class DataSource:
    def __init__(self, name=__name__):
        self.__name = name

        # 创建会话以复用连接
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        })

    def getAllFunds(self, company='80000229'):
        '''
        从东方财富获取易方达基金列表
        :param company: 公司代码，默认易方达
        '''
        url = f'http://fund.eastmoney.com/Company/{company}.html'

        try:
            with self.session.get(url=url) as response:
                response.encoding = 'utf-8'
                html_content = response.text

            # 初始化BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # 存储数据的列表
            result = []

            # 找到所有包含name和code的td元素
            td_elements = soup.find('div', id='kfsFundNetWrap').find_all('td', class_='fund-name-code')

            for td in td_elements:
                # 提取name和code
                name_tag = td.find('a', class_='name')
                code_tag = td.find('a', class_='code')

                # 确保标签存在，避免None报错
                name = name_tag.text.strip() if name_tag else ''
                code = code_tag.text.strip() if code_tag else ''
                result.append({'name': name, 'code': code})

            return result
        except:
            return None

    def getFundBasic(self, code):
        '''
        获取指定基金的基本信息
        ak.fund_individual_basic_info_xq
        :param code: Description
        '''
        url = f"https://danjuanfunds.com/djapi/fund/{code}"
        try:
            result = {"基金代码": code}
            with self.session.get(url, timeout=10) as response:
                response.encoding = 'utf-8'
                json_response = json.loads(response.text)

            result_code = json_response.get('result_code', -1)
            message = json_response.get("message", "")
            data = json_response.get("data", None)
            if result_code == 0 and data is not None:
                result["基金名称"] = data.get("fd_name", "")
                result["基金全称"] = data.get("fd_full_name", "")
                result["成立时间"] = data.get("found_date", "")
                result["最新规模"] = data.get("totshare", "")
                result["基金公司"] = data.get("keeper_name", "")
                result["基金经理"] = data.get("manager_name", "")
                result["托管银行"] = data.get("trup_name", "")
                result["基金类型"] = data.get("type_desc", "")
                result["基金评级"] = data.get("rating_desc", "")
                result["投资策略"] = data.get("invest_orientation", "")
                result["投资目标"] = data.get("invest_target", "")
                result["业绩比较基准"] = data.get("performance_bench_mark", "")
            else:
                result["错误信息"] = message
            
            return result
        except requests.RequestException as e:
            print(f"getFundBasic: {e}")
            return None

    def getFundAssetNetValues(self, code):
        '''
        获取指定基金的单位净值走势
        ak.fund_open_fund_info_em
        :param code: Description
        '''
        url = f"https://fund.eastmoney.com/pingzhongdata/{code}.js"

        try:
            with self.session.get(url, timeout=10) as response:
                response.encoding = 'utf-8'
                data_text = response.text

            js_code = py_mini_racer.MiniRacer()
            js_code.eval(data_text)

            # 单位净值走势
            data_json = js_code.execute("Data_netWorthTrend")
            temp_df = pd.DataFrame(data_json)
            if temp_df.empty:
                return pd.DataFrame()

            temp_df["x"] = pd.to_datetime(temp_df["x"], unit="ms", utc=True).dt.tz_convert(
                "Asia/Shanghai"
            )
            temp_df["x"] = temp_df["x"].dt.date
            temp_df.columns = [
                "净值日期",
                "单位净值",
                "日增长率",
                "_",
            ]
            temp_df = temp_df[
                [
                    "净值日期",
                    "单位净值",
                    "日增长率",
                ]
            ]
            temp_df["净值日期"] = pd.to_datetime(
                temp_df["净值日期"], errors="coerce"
            ).dt.date
            temp_df["单位净值"] = pd.to_numeric(temp_df["单位净值"], errors="coerce")
            temp_df["日增长率"] = pd.to_numeric(temp_df["日增长率"], errors="coerce")
            return temp_df
        except requests.RequestException as e:
            print(f"getFundAssetNetValues: {e}")
            return None

    def getFundCumulativeNetValues(self, code):
        '''
        获取指定基金的累计净值走势
        ak.fund_open_fund_info_em
        :param code: Description
        '''
        url = f"https://fund.eastmoney.com/pingzhongdata/{code}.js"

        try:
            with self.session.get(url, timeout=10) as response:
                response.encoding = 'utf-8'
                data_text = response.text

            js_code = py_mini_racer.MiniRacer()
            js_code.eval(data_text)

            data_json = js_code.execute("Data_ACWorthTrend")
            temp_df = pd.DataFrame(data_json)
            if temp_df.empty:
                return pd.DataFrame()
            temp_df.columns = ["x", "y"]
            temp_df["x"] = pd.to_datetime(temp_df["x"], unit="ms", utc=True).dt.tz_convert(
                "Asia/Shanghai"
            )
            temp_df["x"] = temp_df["x"].dt.date
            temp_df.columns = [
                "净值日期",
                "累计净值",
            ]
            temp_df = temp_df[
                [
                    "净值日期",
                    "累计净值",
                ]
            ]
            temp_df["净值日期"] = pd.to_datetime(
                temp_df["净值日期"], errors="coerce"
            ).dt.date
            temp_df["累计净值"] = pd.to_numeric(temp_df["累计净值"], errors="coerce")
            return temp_df
        except requests.RequestException as e:
            print(f"getFundCumulativeNetValues: {e}")
            return None

    def getFundCumulativeReturnTrend(self, code, period='成立来'):
        '''
        获取指定基金的累计收益率走势
        ak.fund_open_fund_info_em

        :param code: Description
        :param period: {"1月", "3月", "6月", "1年", "3年", "5年", "今年来", "成立来"}
        '''

        url = "https://api.fund.eastmoney.com/pinzhong/LJSYLZS"
        period_map = {
            "1月": "m",
            "3月": "q",
            "6月": "hy",
            "1年": "y",
            "3年": "try",
            "5年": "fiy",
            "今年来": "sy",
            "成立来": "se",
        }
        params = {
            "fundCode": code,
            "indexcode": "000300",
            "type": period_map[period],
        }

        try:
            with self.session.get(url, params=params, headers={"Referer": "https://fund.eastmoney.com/"}, timeout=10) as response:
                response.encoding = 'utf-8'
                data_json = response.json()

            temp_df = pd.DataFrame(data_json["Data"][0]["data"])
            temp_df.columns = ["日期", "累计收益率"]
            temp_df["日期"] = pd.to_datetime(
                temp_df["日期"], unit="ms", utc=True).dt.tz_convert("Asia/Shanghai")
            temp_df["日期"] = pd.to_datetime(temp_df["日期"], errors="coerce").dt.date
            temp_df["累计收益率"] = pd.to_numeric(temp_df["累计收益率"], errors="coerce")
            return temp_df
        except requests.RequestException as e:
            print(f"getFundCumulativeReturnTrend: {e}")
            return None

    def getFundRankingTrend(self, code):
        '''
        获取指定基金的同类排名走势
        ak.fund_open_fund_info_em
        :param code: Description
        '''

        url = f"https://fund.eastmoney.com/pingzhongdata/{code}.js"

        try:
            with self.session.get(url, timeout=10) as response:
                response.encoding = 'utf-8'
                data_text = response.text()

            js_code = py_mini_racer.MiniRacer()
            js_code.eval(data_text)

            data_json = js_code.execute("Data_rateInSimilarType")
            temp_df = pd.DataFrame(data_json)
            temp_df["x"] = pd.to_datetime(temp_df["x"], unit="ms", utc=True).dt.tz_convert(
                "Asia/Shanghai"
            )
            temp_df["x"] = temp_df["x"].dt.date
            temp_df.columns = [
                "报告日期",
                "同类型排名-每日近三月排名",
                "总排名-每日近三月排名",
            ]
            temp_df = temp_df[
                [
                    "报告日期",
                    "同类型排名-每日近三月排名",
                    "总排名-每日近三月排名",
                ]
            ]
            temp_df["报告日期"] = pd.to_datetime(
                temp_df["报告日期"], errors="coerce"
            ).dt.date
            temp_df["同类型排名-每日近三月排名"] = pd.to_numeric(
                temp_df["同类型排名-每日近三月排名"], errors="coerce"
            )
            temp_df["总排名-每日近三月排名"] = pd.to_numeric(
                temp_df["总排名-每日近三月排名"], errors="coerce"
            )
            return temp_df
        except requests.RequestException as e:
            print(f"getFundRankingTrend: {e}")
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
        '''
        获取指定时间范围内的指数分析数据
        ak.index_analysis_daily_sw

        :param self: Description
        :param symbol: Description
        :param start_date: Description
        :param end_date: Description
        '''
        url = "https://www.swsresearch.com/institute-sw/api/index_analysis/index_analysis_report/"
        params = {
            "page": "1",
            "page_size": "50",
            "index_type": symbol,
            "start_date": "-".join([start_date[:4], start_date[4:6], start_date[6:]]),
            "end_date": "-".join([end_date[:4], end_date[4:6], end_date[6:]]),
            "type": "DAY",
            "swindexcode": "all",
        }

        try:
            with self.session.get(url, params=params, verify=False) as response:
                response.raise_for_status()
                data_json = response.json()

            total_num = data_json["data"]["count"]
            total_page = math.ceil(total_num / 50)
            big_df = pd.DataFrame()
            tqdm = get_tqdm()
            for page in tqdm(range(1, total_page + 1), leave=False):
                params.update({"page": page})
                with self.session.get(url, params=params, verify=False) as response:
                    response.raise_for_status()
                    data_json = response.json()
                temp_df = pd.DataFrame(data_json["data"]["results"])
                big_df = pd.concat(objs=[big_df, temp_df], ignore_index=True)
            big_df.rename(
                columns={
                    "swindexcode": "指数代码",
                    "swindexname": "指数名称",
                    "bargaindate": "发布日期",
                    "closeindex": "收盘指数",
                    "bargainamount": "成交量",
                    "markup": "涨跌幅",
                    "turnoverrate": "换手率",
                    "pe": "市盈率",
                    "pb": "市净率",
                    "meanprice": "均价",
                    "bargainsumrate": "成交额占比",
                    "negotiablessharesum1": "流通市值",
                    "negotiablessharesum2": "平均流通市值",
                    "dp": "股息率",
                },
                inplace=True,
            )
            big_df["发布日期"] = pd.to_datetime(big_df["发布日期"], errors="coerce").dt.date
            big_df["收盘指数"] = pd.to_numeric(big_df["收盘指数"], errors="coerce")
            big_df["成交量"] = pd.to_numeric(big_df["成交量"], errors="coerce")
            big_df["涨跌幅"] = pd.to_numeric(big_df["涨跌幅"], errors="coerce")
            big_df["换手率"] = pd.to_numeric(big_df["换手率"], errors="coerce")
            big_df["市盈率"] = pd.to_numeric(big_df["市盈率"], errors="coerce")
            big_df["市净率"] = pd.to_numeric(big_df["市净率"], errors="coerce")
            big_df["均价"] = pd.to_numeric(big_df["均价"], errors="coerce")
            big_df["成交额占比"] = pd.to_numeric(big_df["成交额占比"], errors="coerce")
            big_df["流通市值"] = pd.to_numeric(big_df["流通市值"], errors="coerce")
            big_df["平均流通市值"] = pd.to_numeric(big_df["平均流通市值"], errors="coerce")
            big_df["股息率"] = pd.to_numeric(big_df["股息率"], errors="coerce")
            big_df.sort_values(by=["发布日期"], inplace=True, ignore_index=True)
            return big_df
        except requests.RequestException as e:
            print(f"getAnalyzeIndexData: {e}")
            return None


# 全局数据源实例
fundDataSource = DataSource()
