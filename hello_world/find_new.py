# coding=utf-8
import os
def find_newfile(result_dir):
    """寻找根文件夹result_dir下的最新文件，返回的是文件路径"""
    # 获取根目录下的所有文件
    lists = os.listdir(result_dir)
    # 将根目录下的文件按创建时间升序排序；
    lists.sort(key=lambda fn:   os.path.getatime(result_dir+"\\"+fn)if not os.path.isdir(result_dir+"\\"+fn) else 0)
    # -1 表示文件列表中的最大值
    print ('最新文件为：'+ lists[-1])
    # join连接字符串，得到文件的完整路径；
    filepath = os.path.join(result_dir,lists[-1])
    print filepath