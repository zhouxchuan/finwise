

def string_to_float(text):
    """将字符串转换为浮点数，移除千分位分隔符"""
    try:
        res = float(text.replace(',', ''))
        return res
    except ValueError:
        return None


def format_time(time):
    """格式化时间，返回HH:mm:ss格式"""
    return time.toString('HH:mm:ss')


def format_datetime(datetime):
    """格式化日期时间，返回yyyy-MM-dd HH:mm:ss格式"""
    return datetime.toString('yyyy-MM-dd HH:mm:ss')


def format_date(date):
    """格式化日期，返回yyyy-MM-dd格式"""
    return date.toString('yyyy-MM-dd')


def format_int(value):
    """格式化整数，添加千分位分隔符"""
    return f"{value:,}"


def format_float(value, precision=2):
    """格式化浮点数，保留指定位数的小数"""
    return f"{value:,.{precision}f}"
