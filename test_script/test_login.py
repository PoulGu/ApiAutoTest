'''
测试登录功能
'''
import pytest

from Zonghe.baw import Member, DbOp
from Zonghe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/login_data.yaml"))
def login_data(request):
    return  request.param

@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/login_setup.yaml"))
def setup_data(request):
    return  request.param


# 测试前置和后置
@pytest.fixture()
def register(setup_data,url,baserequests,db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db,phone)
    Member.register(url,baserequests,setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.deleteUser(db,phone)


def test_login(register,login_data,url,baserequests):
    print(f"测试数据为：{login_data['casedata']}")
    print(f"预测结果为：{login_data['expect']}")
    # 登录
    r = Member.Login(url,baserequests,login_data['casedata'])
    # 检查登录结果
    assert  r.json()['msg'] == login_data['expect']['msg']
    assert r.json()['code'] == login_data['expect']['code']
    assert r.json()['status'] == login_data['expect']['status']