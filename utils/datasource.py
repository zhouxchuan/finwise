from bs4 import BeautifulSoup
import requests
# import tushare as ts
import pandas as pd
import akshare as ak

# TS_TOKEN = '31e5536e4d0ffbfb47a74e9832fd35c711fdaa2405bec6559b62d22d'
EFUND_LIST = 'http://fund.eastmoney.com/Company/80000229.html'

class DataSource:
    def __init__(self, name=__name__):
        self.__name = name
        # self.pro=ts.pro_api(TS_TOKEN)

    # 获取所有基金
    def getAllFunds(self):
        # 从东方财富获取易方达基金列表
        response = requests.get(EFUND_LIST)
        response.encoding = 'utf-8'
        html_content = response.text
        
        # 初始化BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 存储数据的列表
        data = []
        
        # 找到所有包含name和code的td元素
        td_elements = soup.find('div',id='kfsFundNetWrap').find_all('td', class_='fund-name-code')
    
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
            df = ak.fund_open_fund_info_em(symbol=code,indicator='单位净值走势')
            return df
        except:
            return None
    
    # 获取指定基金的累计净值走势
    def getFundCumulativeNetValues(self, code):
        try:
            df = ak.fund_open_fund_info_em(symbol=code,indicator='累计净值走势')
            return df
        except:
            return None
    
    # 获取指定基金的累计收益率走势
    # period :  {"1月", "3月", "6月", "1年", "3年", "5年", "今年来", "成立来"}
    def getFundCumulativeReturnTrend(self, code,period='成立来'):
        try:
            df = ak.fund_open_fund_info_em(symbol=code,indicator='累计收益率走势',period=period)
            return df
        except:
            return None

    # 获取指定基金的同类排名走势
    def getFundRankingTrend(self, code):
        try:
            df = ak.fund_open_fund_info_em(symbol=code,indicator='同类排名走势')
            return df
        except:
            return None

    # 获取指定基金的持仓比列(股票、债券、现金、其他比例)
    def getFundHoldRatio(self, code, date='20251231'):
        try:
            df = ak.fund_individual_detail_hold_xq(symbol=code, date=date)
            return df
        except:
            return None
        
    # 获取指定基金的持仓股票
    def getFundHoldShare(self, code, date='2025'):
        try:
            df = ak.fund_portfolio_hold_em(symbol=code, date=date)
            return df
        except:
            return None

    # 获取指定基金的持仓债券
    def getFundHoldBond(self, code, date='2025'):
        try:
            df = ak.fund_portfolio_bond_hold_em(symbol=code, date=date)
            return df
        except:
            return None
        
    # 获取指定基金的持仓行业
    def getFundHoldIndustry(self, code, date='2025'):
        try:
            df = ak.fund_portfolio_industry_allocation_em(symbol=code, date=date)
            return df
        except:
            return None
        
    def getAnalyzeIndexData(self, symbol='市场表征', start_date='20251231', end_date='20251231'):
        try:
            df = ak.index_analysis_daily_sw(symbol=symbol, start_date=start_date, end_date=end_date)
            return df
        except:
            return None

# 全局数据源实例
fundDataSource = DataSource()
