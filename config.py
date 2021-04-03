# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/11 14:50
# Description:

__author__ = "BeiYu"

import os
import pandas as pd


def reader(file_path=os.path.join("database", "group_list.xlsx")):
    df = pd.read_excel(file_path)
    # print(df.head())
    # print(df['组别'].unique())
    return df


class Config(object):
    def __init__(self):
        self.debug = True
        self.host = '0.0.0.0'
        self.port = '5000'
        # self.mysql_host = 'localhost'
        # self.mysql_username = 'root'
        # self.mysql_password = 'root'
        self.info = reader(file_path=os.path.join('database', 'group_list.xlsx'))
        self.group_num = len(self.info['组别'].unique())
        self.group_list = self.info['组别'].unique()
        self.name_list = []
        self.info_list = []
        self.name_list_all = []
        for i in self.group_list:
            # print(i)
            new_df = self.info[self.info['组别'] == i]
            _group_info_cached = []
            _name_cached = []
            # print(new_df)
            for idx, x in new_df.iterrows():
                # print(x)
                stu_info = {'学号': x['学号'], '姓名': x['姓名'], '组别': x['组别'], '是否是组长': x['备注']}
                _group_info_cached.append(stu_info)
                _name_cached.append(x['姓名'])
                self.name_list_all.append(x['姓名'])
                # print(stu_info)
            self.info.append(_group_info_cached)
            self.name_list.append(_name_cached)

        self.submit_table = None
        # print(self.name_list[1])


config = Config()


def dprint(param):
    if config.debug:
        print(param)


if __name__ == '__main__':
    reader()
