from decimal import Decimal


class format_convert:
    @staticmethod
    def string_to_decimal(text):
        """将字符串转换为Decimal类型，移除千分位分隔符"""
        try:
            text = text.replace(',', '')
            res = Decimal(text)
            return res
        except (ValueError, Decimal.InvalidOperation):
            return None

    @staticmethod
    def float_to_decimal(value, precision=2):
        """浮点数转Decimal类型"""
        return Decimal(f"{value:.{precision}f}")

    @staticmethod
    def time_to_string(time):
        """格式化时间，返回HH:mm:ss格式"""
        return time.toString('HH:mm:ss')

    @staticmethod
    def datetime_to_string(datetime):
        """格式化日期时间，返回yyyy-MM-dd HH:mm:ss格式"""
        return datetime.toString('yyyy-MM-dd HH:mm:ss')

    @staticmethod
    def date_to_string(date):
        """格式化日期，返回yyyy-MM-dd格式"""
        return date.toString('yyyy-MM-dd')

    @staticmethod
    def to_currency(value):
        """格式化整数，添加千分位分隔符"""
        return f"{value:,}"

    @staticmethod
    def decimal_to_string(value, precision=2):
        """格式化浮点数，保留指定位数的小数"""
        return f"{value:,.{precision}f}"
