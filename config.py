# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/11 14:50
# Description:

__author__ = "BeiYu"


class Config(object):
    def __init__(self):
        self.debug = True
        self.host = '0.0.0.0'
        self.port = '5000'
        self.mysql_host = 'localhost'
        self.mysql_username = 'root'
        self.mysql_password = 'root'
        self.group_num = 12
        self.group_list = [str(i) for i in range(1, self.group_num+1)]
        self.name_list = [[] for i in range(1, self.group_num+1)]
        self.name_list[0] = ['闫冰洁', '吴水海', '平静怡', '蒋英奇', '刘莉萍', '闫梦帆', '张琬涓', '谢品浩', '滕畅', '王楠']


config = Config()
