'''
充值的测试脚本
'''

import pytest

from Zonghe.caw import DataRead
from Zonghe.baw import Member,DbOp

@pytest.fixture(params=DataRead.readyaml("Zonghe/data_case/recharge_data.yaml"))
def recharge_data(request):
    return  request.param

def test_recharge(recharge_data,url,baserequests):
    print(f"测试数据为：{recharge_data['casedata']}")
    print(f"预测结果为：{recharge_data['expect']}")
    # 充值
    r = Member.recharge(url,baserequests,recharge_data['casedata'])
    # 检查充值结果
    assert r.json()['msg'] == recharge_data['expect']['msg']
    assert r.json()['code'] == recharge_data['expect']['code']
    assert r.json()['status'] == recharge_data['expect']['status']
