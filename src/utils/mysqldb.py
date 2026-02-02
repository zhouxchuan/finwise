import mysql.connector
from utils.logger import log
import hashlib
import pandas as pd

mysql_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'finwise',
    'password': '123456',
    'database': 'finwise',
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci',
    'autocommit': True,
}

# -----------------------------------------------------------------------------
# 数据库连接池类


class MySQLDatabase:
    def __init__(self, config):
        # 创建连接池配置
        pool_config = {
            'pool_name': 'fund_pool',
            'pool_size': 10,  # 连接池大小
            'pool_reset_session': True,
            'host': config['host'],
            'user': config['user'],
            'password': config['password'],
            'database': config['database'],
            'charset': 'utf8mb4',
            'autocommit': True
        }

        try:
            self.pool = mysql.connector.pooling.MySQLConnectionPool(
                **pool_config)
        except Exception as e:
            print(f"创建连接池失败: {e}")
            raise

    def execute_query(self, sql, params=None):
        """执行查询，使用连接池"""
        connection = None
        cursor = None
        try:
            # 从连接池获取连接
            connection = self.pool.get_connection()
            cursor = connection.cursor(dictionary=True)

            # 执行查询
            cursor.execute(sql, params)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"查询执行失败: {e}")
            raise
        finally:
            # 确保资源被正确释放
            if cursor:
                cursor.close()
            if connection:
                connection.close()  # 归还连接到池

    def execute_update(self, sql, params=None):
        """执行更新操作，使用连接池"""
        connection = None
        cursor = None
        try:
            # 从连接池获取连接
            connection = self.pool.get_connection()
            cursor = connection.cursor(prepared=True)

            # 执行更新
            cursor.execute(sql, params)
            # self.cnx.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"更新执行失败: {e}")
            raise
        finally:
            # 确保资源被正确释放
            if cursor:
                cursor.close()
            if connection:
                connection.close()  # 归还连接到池

    def checkLogin(self, userid, password):
        sql = "SELECT COUNT(*) FROM `user_account` WHERE `user_id` = %s AND user_password = %s"
        password_md5 = hashlib.md5()
        password_md5.update(password.encode('utf-8'))
        password_md5_hex = password_md5.hexdigest()
        params = (userid, password_md5_hex,)
        result = self.execute_query(sql, params)
        return result[0]['COUNT(*)'] > 0 if result else False

    def getFundList(self):
        sql = "SELECT * FROM `fund_list` ORDER BY `order` ASC"
        result = self.execute_query(sql)
        return result

    def getFundAccountData(self, code):
        sql = "SELECT * FROM `fund_list` WHERE `code`=%s"
        params = (code,)
        result = self.execute_query(sql, params=params)
        return result[0] if result else None

    def getFundTradeData(self, trade_date):
        sql = "SELECT `code`,`trade_date`,`trade_text` FROM `fund_trade` WHERE `trade_date`=%s ORDER BY `code`"
        params = (trade_date,)
        result = self.execute_query(sql, params=params)
        return result

    def setFundTradeData(self, code, trade_date, trade_text):
        sql = "REPLACE INTO `fund_trade` (`code`, `trade_date`, `trade_text`) VALUES (%s, %s, %s)"
        params = (code, trade_date, trade_text)
        rowcount = self.execute_update(sql, params=params)
        return rowcount

    def removeFundTradeData(self, code, trade_date):
        sql = "DELETE FROM `fund_trade` WHERE `code`=%s AND `trade_date`=%s"
        params = (code, trade_date)
        rowcount = self.execute_update(sql, params=params)
        return rowcount

    def setFundItem(self, code, name):
        sql = "REPLACE INTO fund_list (`code`, `name`) VALUES (%s, %s)"
        params = (code, name,)
        rowcount = self.execute_update(sql, params=params)
        return rowcount

    def deleteFundItem(self, code):
        sql = "DELETE FROM fund_list WHERE code = %s"
        params = (code,)
        rowcount = self.execute_update(sql, params=params)
        return rowcount

    def getFundBasicData(self, code):
        sql = "SELECT * FROM fund_basic WHERE code = %s"
        params = (code,)
        result = self.execute_query(sql, params=params)
        return result[0] if result else None

    def setFundBasicData(self, data):
        code = data['基金代码']
        name = data['基金名称']
        fullname = data['基金全称']
        found_date = data['成立时间']
        scale = data['最新规模']
        company = data['基金公司']
        manager = data['基金经理']
        bank = data['托管银行']
        type = data['基金类型']
        rating = data['基金评级']
        investment_strategy = data['投资策略']
        investment_goal = data['投资目标']
        benchmark = data['业绩比较基准']

        sql = "REPLACE INTO fund_basic (`code`, `name`, `fullname`,`found_date`,`scale`,`company`,`manager`,`bank`,`type`,`rating`,`investment_strategy`,`investment_goal`,`benchmark`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (code, name, fullname, found_date, scale, company, manager, bank,
                  type, rating, investment_strategy, investment_goal, benchmark,)
        rowcount = self.execute_update(sql, params=params)
        return rowcount

    def getFundHistoryData(self, code):
        sql = "SELECT * FROM fund_history WHERE code = %s"
        params = (code,)
        result = self.execute_query(sql, params=params)
        return result

    def getFundHistoryNetValues(self, code, start_date='1993-01-01', end_date='2099-12-31'):
        sql = "SELECT * FROM fund_history WHERE code = %s AND trade_date BETWEEN %s AND %s"
        params = (code, start_date, end_date)
        result = self.execute_query(sql, params=params)
        return result

    def setFundHistoryAssetNetValues(self, code, row):
        trade_date = row['净值日期'].strftime('%Y-%m-%d')
        asset_net_value = row['单位净值'] if pd.notna(row['单位净值']) else 0.0
        growth_rate = row['日增长率'] if pd.notna(row['日增长率']) else 0.0

        sql = "SELECT `trade_date` FROM `fund_history` WHERE `code` = %s AND `trade_date` = %s"
        params = (code, trade_date)
        result = self.execute_query(sql, params=params)
        if result is not None and len(result) > 0:
            return 0

        sql = "INSERT INTO fund_history (`code`, `trade_date`, `asset_net_value`,`growth_rate`) VALUES (%s, %s, %s, %s)"
        params = (code, trade_date, asset_net_value, growth_rate)
        rowcount = self.execute_update(sql, params=params)
        return rowcount

    def setFundHistoryCumNetValues(self, code, row):
        trade_date = row['净值日期'].strftime('%Y-%m-%d')
        cum_net_value = row['累计净值'] if pd.notna(row['累计净值']) else 0.0

        sql = "SELECT `trade_date` FROM `fund_history` WHERE `code` = %s AND `trade_date` = %s"
        params = (code, trade_date)
        result = self.execute_query(sql, params=params)
        if result is None or len(result) == 0:
            return 0

        sql = "UPDATE `fund_history` set `cum_net_value`=%s WHERE `code`=%s AND `trade_date`=%s"
        params = (cum_net_value, code, trade_date)
        rowcount = self.execute_update(sql, params=params)
        return rowcount

    def getFundLatestNetValue(self, code):
        sql = "SELECT * FROM `fund_history` WHERE `code` = %s ORDER BY `trade_date` DESC LIMIT 1"
        params = (code,)
        result = self.execute_query(sql, params=params)
        return result[0] if result else None

    def getFundActionData(self, code):
        sql = "SELECT action_date, action_type, amount, remark FROM `fund_action` WHERE `code` = %s ORDER BY `action_date`"
        params = (code,)
        result = self.execute_query(sql, params=params)
        return result


# -----------------------------------------------------------------------------
MySQLDB = MySQLDatabase(mysql_config)
