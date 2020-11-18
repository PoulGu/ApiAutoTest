'''
对requests的get、post的方法进行一层包装
1、增加异常处理
2、增加日志打印
3、创建一个session，确保能自动管理cookie
'''

import requests



class BaseRequests:

    def __init__(self):
        # 创建一个session，赋值给属性session
        self.session =requests.session()

    def get(self,url,**kwargs):
        try:
            # 使用session的方式调用requests中的get接口
            r = self.session.get(url,**kwargs)
            print(f"发送get请求：{url},参数：{kwargs}成功")
            return r
        except Exception as e:
            print(f"发送get请求：{url},参数：{kwargs}异常，异常信息为：{e}")

    def __init__(self):
        # 创建一个session，赋值给属性session
        self.session =requests.session()

    def post(self,url,**kwargs):
        try:
            # 使用session的方式调用requests中的post接口
            r = self.session.post(url,**kwargs)
            print(f"发送post请求：{url},参数：{kwargs}成功")
            return r
        except Exception as e:
            print(f"发送post请求：{url},参数：{kwargs}异常，异常信息为：{e}")


# 测试代码，用完即删
if __name__ == '__main__':
    r = BaseRequests().get("http://www.httpbin.org/get?username=root&pwd=123123")
    print(r.text)

    r = BaseRequests().post("http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=18829299292&pwd=123456")

