import json
import requests
import time
from jsonpath_rw import parse
from common.connect_db import ExecuteSQL, ExecuteSQLAll
from config import readcfg

header = readcfg.header
header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
positionId_Gary = readcfg.positionId_real1_Gary
positionId_Jenny = readcfg.positionId_real1_Jenny
account_Gary = readcfg.account_Gary
account_Jenny = readcfg.account_Jenny
url = readcfg.url


def get_share_id():
    name = "iot_test"
    sql = "select share_id from iot_position_share_record where " \
          "position_id='%s' and state in (1 ,2) and expire_state=0;" % positionId_Gary
    connect = ExecuteSQL(name, sql)
    execute_result = connect.execute_sql()
    if execute_result:
        share_id = execute_result[0]
        return share_id
    else:
        depend_data = "shareId"
        url_invite = url + "/app/v1.0/lumi/position/share/invite"
        json_invite = {
            "positionId": positionId_Gary,
            "account": account_Jenny,
            "permission": 3,
            "hint": "hint",
            "remark": "remark"
        }
        res = requests.post(url=url_invite, json=json_invite, headers=header_Gary)
        response_data = json.loads(res.text)
        # print(response_data)
        if depend_data in response_data:
            json_exe = parse(depend_data)
            madle = json_exe.find(response_data)
            return [math.value for math in madle][0]
        else:
            response_data = response_data["result"]
            json_exe = parse(depend_data)
            madle = json_exe.find(response_data)
            return [math.value for math in madle][0]


def get_unreply_share_id():
    name = "iot_test"
    sql = "select share_id from iot_position_share_record where " \
          "position_id='%s ' and state=2 and expire_state=0;" % positionId_Gary
    connect = ExecuteSQL(name, sql)
    execute_result = connect.execute_sql()
    if execute_result:
        share_id = execute_result[0]
        return share_id
    else:
        depend_data = "shareId"
        url_invite = url + "/v1.0/lumi/position/share/invite"
        json_invite = {
            "positionId": positionId_Gary,
            "account": account_Jenny,
            "permission": 3,
            "hint": "hint",
            "remark": "remark"
        }
        res = requests.post(url=url_invite, json=json_invite, headers=header_Gary)
        response_data = json.loads(res.text)
        print(response_data)
        if depend_data in response_data:
            json_exe = parse(depend_data)
            madle = json_exe.find(response_data)
            return [math.value for math in madle][0]
        else:
            response_data = response_data["result"]
            json_exe = parse(depend_data)
            madle = json_exe.find(response_data)
            return [math.value for math in madle][0]


def get_result_from_sql(sql):
    name = "iot_test"
    sql = sql
    connect = ExecuteSQL(name, sql)
    execute_result = connect.execute_sql()
    return execute_result


def get_all_result_from_sql(sql):
    name = "iot_test"
    sql = sql
    connect = ExecuteSQLAll(name, sql)
    execute_result = connect.execute_sql()
    return execute_result


def get_code(account="18682246872"):
    sql = "select request_msg from iot_send_record where account='18682246872' order by create_time DESC limit 1;"
    url_ = url + "/app/v1.0/lumi/user/get/authcode"
    json_ = {
        "account": account
    }
    r = requests.post(url=url_, json=json_, headers=header)
    time.sleep(1)
    result_sql_ = get_result_from_sql(sql)[0]
    code_ = json.loads(result_sql_)["priParams"]["18682246872"]["code"]
    time.sleep(0.5)
    print("验证码为：%s" % code_)
    return code_


def get_common_code(account="guobing.tang@aqara.com", authCodeType="4"):
    sql = "select request_msg from iot_send_record where account='%s' order by create_time DESC limit 1;" % account
    url_ = url + "/app/v1.0/lumi/user/authcode"
    json_ = {
        "account": account,
        "authCodeType": authCodeType
    }
    r = requests.post(url=url_, json=json_, headers=header)
    time.sleep(2)
    result_sql_ = get_result_from_sql(sql)[0]
    code_ = json.loads(result_sql_)["code"]
    time.sleep(0.5)
    print("验证码为：%s" % code_)
    return code_


if __name__ == '__main__':
    r = get_code()
