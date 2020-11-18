'''
读文件的公共方法
'''
import configparser
import os
import yaml


def getProjectpath():
    '''
    获取当前工程路径
    :return: 返回工程路径
    '''
    current_file_path = os.path.realpath(__file__) # 获取当前文件路径
    # print(current_file_path)
    dir_name = os.path.dirname(current_file_path) # 文件所在的目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name) # 上一级目录
    # print(dir_name)
    dir_name = os.path.dirname(dir_name) #上一级目录
    # print(dir_name)
    return dir_name + "\\"


def readini(filepath,key):
    '''
    读取ini文件
    :param filepath:文件路径
    :param key: ini中的关键字
    :return: key对应的value
    '''
    # 完整路径拼接
    real_path = getProjectpath()+filepath
    # 调用configparser来解析配置文件
    config = configparser.ConfigParser()
    # 读文件
    config.read(real_path)
    # env表示section，根据key在对应的section中取value
    value = config.get("env",key)
    return value

def readyaml(filePath):
    '''
    读取yaml文件
    :param filePath:文件路径
    :return: yaml中文件内容
    '''
    real_path = getProjectpath() + filePath
    with open(real_path,"r",encoding="utf-8") as f:
        content = yaml.load(f,Loader=yaml.FullLoader)
        return content


# 测试代码，用完即删
if __name__ == '__main__':
    # 预期返回 E\ApiAutoTest
    print(getProjectpath())
    # 预期返回http://jy001:8081/
    print(readini(r"Zonghe\data_env\env.ini","url"))
    print(readini(r"Zonghe\data_env\env.ini", "db"))
    content = readyaml(r"Zonghe/data_case/register_fail.yaml")
    print(content[0].get('expect'))


