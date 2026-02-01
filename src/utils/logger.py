import logging

# 日志类
class Logger:
    def __init__(self, name=__name__):
        self.__name = name
        self.logger = logging.getLogger(self.__name)
        self.logger.setLevel(level=logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('[[%(asctime)s]%(levelname)s][%(filename)s:%(lineno)d]: %(message)s')

        # 创建一个handler，用于将日志输出到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    @property
    def instance(self):
        return self.logger

# 全局日志实例
log = Logger(__name__).instance