'''
注册的测试脚本(pytest)
'''

import pytest
from Zonghe.caw import  DataRead
from Zonghe.baw import Member, DbOp


# 测试前置：获取测试数据，为列表，通过readyaml读取而来
from Zonghe.test_script.conftest import db


@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/register_fail.yaml"))
def fail_data(request): # 固定写法
    return request.param

@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/register_pass.yaml"))
def pass_data(request): # 固定写法
    return request.param

@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/register_repet.yaml"))
def repet_data(request):# 固定写法
    return  request.param

# 注册失败
def test_register_fail(fail_data,url,baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")
    # 发送请求
    r = Member.register(url,baserequests,fail_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert r.json()['status'] == fail_data['expect']['status']
    assert r.json()['code'] == fail_data['expect']['code']

# 注册成功
def test_register_pass(pass_data,url,db,baserequests):
    print(f"预测结果为：{pass_data['casedata']}")
    print(f"预测结果为：{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']
    # 初始化环境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url,baserequests,pass_data['casedata'])
    # 检查响应结果
    assert r.json()['msg'] == pass_data['expect']['msg']
    assert r.json()['status'] == pass_data['expect']['status']
    assert r.json()['code'] == pass_data['expect']['code']
    # 2、检查实际有没有注册成功(1、查数据库，2、获取用户列表，3、用注册的用户登录）
    r = Member.getlist(url,baserequests)
    assert str(phone) in r.text
    # 清理环境、根据手机号删除注册用户
    DbOp.deleteUser(db,phone)



# 重复注册
def test_register_repeat(repet_data,url,db,baserequests):
    print(f"预测结果为： {repet_data['casedata']}")
    print(f"预测结果为： {repet_data['expect']}")
    phone = repet_data['casedata']['mobilephone']
    DbOp.deleteUser(db,phone)
    # 发送请求
    r = Member.register(url,baserequests,repet_data['casedata'])
    r = Member.register(url,baserequests,repet_data['casedata'])
    # 检查响应
    assert r.json()['msg'] == repet_data['expect']['msg']
    assert r.json()['status'] == repet_data['expect']['status']
    assert r.json()['code'] == repet_data['expect']['code']
    DbOp.deleteUser(db,phone)

