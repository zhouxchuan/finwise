import mysql.connector
from utils.logger import log
import hashlib
import pandas as pd
import json
from datetime import date
import pandas as pd

from utils.utils import format_convert

# -----------------------------------------------------------------------------
# 数据库连接池类


class MySQLDatabase:
    '''
    数据库连接池类，用于管理数据库连接
    '''
    connection_pool = None

    @staticmethod
    def initialize(config):
        ''' 
        初始化数据库连接池
        :param config: 数据库配置字典，包含 host, port, database, user, password等
        :return: 初始化成功返回True，失败返回False
        '''

        pool_config = {
            'host': config['host'],
            'port': config['port'],
            'database': config['database'],
            'user': config['user'],
            'password': config['password'],
            'pool_name': 'fund_pool',
            'pool_size': 10,  # 连接池大小
            'pool_reset_session': True,
            'charset': 'utf8mb4',
            'autocommit': True
        }

        try:
            MySQLDatabase.connection_pool = mysql.connector.pooling.MySQLConnectionPool(**pool_config)
            log.info("数据库连接池初始化成功")
            return True
        except Exception as e:
            log.error(f"创建连接池失败: {e}")
            return False

    @staticmethod
    def execute_query(sql, params=None):
        """执行查询，使用连接池"""
        connection = None
        cursor = None
        try:
            # 从连接池获取连接
            connection = MySQLDatabase.connection_pool.get_connection()
            cursor = connection.cursor(dictionary=True)

            # 执行查询
            cursor.execute(sql, params)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"查询执行失败: {e}")
            return None
        finally:
            # 确保资源被正确释放
            if cursor:
                cursor.close()
            if connection:
                connection.close()  # 归还连接到池

    @staticmethod
    def execute_update(sql, params=None):
        """执行更新操作，使用连接池"""
        connection = None
        cursor = None
        try:
            # 从连接池获取连接
            connection = MySQLDatabase.connection_pool.get_connection()
            cursor = connection.cursor(prepared=True)

            # 执行更新
            cursor.execute(sql, params)

            # self.cnx.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"更新执行失败: {e}")
            return -1
        finally:
            # 确保资源被正确释放
            if cursor:
                cursor.close()
            if connection:
                connection.close()  # 归还连接到池

    @staticmethod
    def checkLogin(userid, password):
        sql = "SELECT COUNT(*) FROM `user_account` WHERE `user_id` = %s AND user_password = %s"
        password_md5 = hashlib.md5()
        password_md5.update(password.encode('utf-8'))
        password_md5_hex = password_md5.hexdigest()
        params = (userid, password_md5_hex,)
        result = MySQLDatabase.execute_query(sql, params)
        return result[0]['COUNT(*)'] > 0 if result else False

    @staticmethod
    def getFundAccountList():
        '''
        获取基金账户列表
        '''
        sql = "SELECT * FROM `fund_account` ORDER BY `order` ASC"
        result = MySQLDatabase.execute_query(sql)
        return result

    @staticmethod
    def getFundAccount(code):
        '''
        获取指定基金账户数据
        :param code: 基金代码
        '''
        sql = "SELECT * FROM `fund_account` WHERE `code`=%s"
        params = (code,)
        result = MySQLDatabase.execute_query(sql, params=params)
        return result[0] if result else None

    @staticmethod
    def addFundAccount(code, name):
        '''
        添加基金账户数据
        :param code: 基金代码
        :param name: 基金名称
        '''
        sql = "INSERT INTO fund_account (`code`, `name`) VALUES (%s, %s)"
        params = (code, name,)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def deleteFundAccount(code):
        '''
        删除基金账户数据
        :param code: 基金代码
        '''
        sql = "DELETE FROM fund_account WHERE code = %s"
        params = (code,)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def setFundAccountBasicInfo(code, data):
        sql = "UPDATE fund_account SET `basic_info`=%s WHERE `code`=%s"
        params = (json.dumps(data, ensure_ascii=False), code)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def setFundAccountListOrder(code, order):
        sql = "UPDATE fund_account SET `order`=%s WHERE `code`=%s"
        params = (order, code)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def getFundHistoryData(code):
        sql = "SELECT * FROM fund_history WHERE code = %s"
        params = (code,)
        result = MySQLDatabase.execute_query(sql, params=params)
        return result

    @staticmethod
    def getFundHistoryNetValues(code, start_date='1993-01-01', end_date='2099-12-31'):
        sql = "SELECT * FROM fund_history WHERE code = %s AND trade_date BETWEEN %s AND %s"
        params = (code, start_date, end_date)
        result = MySQLDatabase.execute_query(sql, params=params)
        return result

    @staticmethod
    def setFundHistoryAssetNetValues(code, row):
        trade_date = row['净值日期'].strftime('%Y-%m-%d')
        asset_net_value = row['单位净值'] if pd.notna(row['单位净值']) else 0.0
        growth_rate = row['日增长率'] if pd.notna(row['日增长率']) else 0.0

        sql = "SELECT `trade_date` FROM `fund_history` WHERE `code` = %s AND `trade_date` = %s"
        params = (code, trade_date)
        result = MySQLDatabase.execute_query(sql, params=params)
        if result is not None and len(result) > 0:
            return 0

        sql = "INSERT INTO fund_history (`code`, `trade_date`, `asset_net_value`,`growth_rate`) VALUES (%s, %s, %s, %s)"
        params = (code, trade_date, asset_net_value, growth_rate)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def setFundHistoryCumNetValues(code, row):
        trade_date = row['净值日期'].strftime('%Y-%m-%d')
        cum_net_value = row['累计净值'] if pd.notna(row['累计净值']) else 0.0

        sql = "SELECT `trade_date` FROM `fund_history` WHERE `code` = %s AND `trade_date` = %s"
        params = (code, trade_date)
        result = MySQLDatabase.execute_query(sql, params=params)
        if result is None or len(result) == 0:
            return 0

        sql = "UPDATE `fund_history` set `cum_net_value`=%s WHERE `code`=%s AND `trade_date`=%s"
        params = (cum_net_value, code, trade_date)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def getFundLatestNetValue(code):
        sql = "SELECT * FROM `fund_history` WHERE `code` = %s ORDER BY `trade_date` DESC LIMIT 1"
        params = (code,)
        result = MySQLDatabase.execute_query(sql, params=params)
        return result[0] if result else None

    @staticmethod
    def getFundNetValue(code, trade_date):
        sql = "SELECT asset_net_value FROM `fund_history` WHERE `code` = %s AND `trade_date` = %s"
        params = (code, trade_date)
        result = MySQLDatabase.execute_query(sql, params=params)
        return result[0] if result else None

    @staticmethod
    def getFundNetValue(code, start_date, end_date):
        sql = "SELECT `trade_date`,`asset_net_value`, `cum_net_value` FROM `fund_history` WHERE `code` = %s AND `trade_date` BETWEEN %s AND %s ORDER BY `trade_date` DESC"
        params = (code, start_date, end_date)
        result = MySQLDatabase.execute_query(sql, params=params)
        return result

    @staticmethod
    def getFundTradingData(code):
        sql = "SELECT `trade_date`, `trade_type`, `amount`, `remark` FROM `fund_trade` WHERE `code` = %s ORDER BY `trade_date`"
        params = (code,)
        result = MySQLDatabase.execute_query(sql, params=params)
        return result

    @staticmethod
    def setFundTradingData(code, trade_date, trade_type, amount):
        sql = "REPLACE INTO `fund_trade` (`code`, `trade_date`, `trade_type`, `amount`, `remark`) VALUES (%s, %s, %s, %s, '未执行')"
        params = (code, trade_date, trade_type, amount)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def deleteFundTradingData(code, trade_date):
        sql = "DELETE FROM `fund_trade` WHERE `code` = %s AND `trade_date` = %s"
        params = (code, trade_date)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def executeFundTradingData(code, trade_date):
        '''
        执行基金买卖操作
        :param code: 基金代码
        :param trade_date: 交易日期
        '''
        sql = "SELECT `trade_type`, `amount` FROM `fund_trade` WHERE `code` = %s AND `trade_date` = %s AND `remark` = '未执行'"
        params = (code, trade_date)
        result = MySQLDatabase.execute_query(sql, params=params)
        trade_type = result[0]['trade_type'] if result else None
        amount = result[0]['amount'] if result else None
        if trade_type is None or amount is None:
            return 0
        amount = format_convert.float_to_decimal(amount, 2)

        # 查询指定日期的净值
        sql = "SELECT `asset_net_value` FROM `fund_history` WHERE `code` = %s AND `trade_date` = %s"
        params = (code, trade_date)
        result = MySQLDatabase.execute_query(sql, params=params)
        asset_net_value = result[0]['asset_net_value'] if result else None
        if asset_net_value is None:
            return 0
        asset_net_value = format_convert.float_to_decimal(asset_net_value, 4)

        # 查询操作前的持仓成本及持仓份额
        sql = "SELECT `cost`, `share` FROM `fund_holding` WHERE `code` = %s ORDER BY `holding_date` DESC LIMIT 1"
        params = (code,)
        result = MySQLDatabase.execute_query(sql, params=params)
        holding_cost = result[0]['cost'] if result else None
        holding_share = result[0]['share'] if result else None
        if holding_cost is None or holding_share is None:
            return 0
        holding_cost = format_convert.float_to_decimal(holding_cost, 2)
        holding_share = format_convert.float_to_decimal(holding_share, 2)

        # 计算操作后的资产净值
        if trade_type == '买入':
            holding_cost = holding_cost + amount
            holding_share = holding_share + amount / asset_net_value
            holding_share = format_convert.float_to_decimal(holding_share, 2)
        elif trade_type == '卖出':
            holding_share = holding_share - amount
            holding_cost = holding_cost - amount * asset_net_value
            holding_cost = format_convert.float_to_decimal(holding_cost, 2)
        else:
            return 0

        # 更新持仓成本及持仓份额
        holding_date = date.today().strftime("%Y-%m-%d")
        sql = "REPLACE INTO `fund_holding` (`code`, `holding_date`, `cost`, `share`) VALUES (%s, %s, %s, %s)"
        params = (code, holding_date, holding_cost, holding_share)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        if rowcount == 0:
            return 0

        # 更新操作后的资产净值
        sql = "UPDATE `fund_trade` SET `remark` = '已执行' WHERE `code` = %s AND `trade_date` = %s"
        params = (code, trade_date)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def updateFundHoldingData(code, cost, share):
        '''
        更新基金持仓数据
        :param code: 基金代码
        :param cost: 持仓成本
        :param share: 持仓份额
        '''
        holding_date = date.today().strftime("%Y-%m-%d")
        sql = "SELECT `holding_date` FROM `fund_holding` WHERE `code` = %s ORDER BY `holding_date` ASC LIMIT 1"
        params = (code,)
        result = MySQLDatabase.execute_query(sql, params=params)
        if result is not None and len(result) > 0:
            holding_date = result[0]['holding_date']

        sql = "REPLACE INTO `fund_holding` (`code`, `holding_date`, `cost`, `share`) VALUES (%s, %s, %s, %s)"
        params = (code, holding_date, cost, share)
        rowcount = MySQLDatabase.execute_update(sql, params=params)
        return rowcount

    @staticmethod
    def getFundLastestHoldingData(code):
        '''
        获得基金最新持仓数据
        :param code: 基金代码
        '''
        sql = "SELECT `code`, `holding_date`,`cost`, `share` FROM `fund_holding` WHERE `code` = %s ORDER BY `holding_date` DESC"
        params = (code,)
        result = MySQLDatabase.execute_query(sql, params=params)
        return result[0] if result else None
