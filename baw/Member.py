'''
用户模块的接口(注册、登录、充值、用户列表、取现...)
'''

def register(url,baserequests,data):
    '''
    发送注册接口
    :param url: http：//jy001:8081/  环境文件中读取
    :param baserequests:  是BaseRequests的一个实例
    :param data:  注册接口的参数
    :return: 响应信息
    '''
    url = url + "futureloan/mvc/api/member/register"
    r = baserequests.post(url,data=data)
    return r

def Login(url,baserequests,data):
    '''
    发送登录接口
    :param url: http：//jy001:8081/  环境文件中读取
    :param baserequests: 是BaseRequests的一个实例
    :param data: 注册接口的参数
    :return: 响应信息
    '''
    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url,data=data)
    return r

def recharge(url,baserequests,data):
    '''
    发送充值接口
    :param url:  http：//jy001:8081/ 环境文件中读取
    :param baserequests: 是BaseRequests的一个实例
    :param data: 充值接口的参数
    :return: 响应信息
    '''
    url = url + "futureloan/mvc/api/member/recharge"
    r = baserequests.post(url,data=data)
    return r

def getlist(url,baserequests):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.get(url)
    return r


# 测试代码，用完即删
if __name__ == '__main__':
    from  Zonghe.caw.BaseRequests import BaseRequests

    baserequests = BaseRequests()
    canshu = {"mobilephone":18223213123,"pwd":123987}
    r = register("http://jy001:8081/",baserequests,canshu)
    print(r.json())