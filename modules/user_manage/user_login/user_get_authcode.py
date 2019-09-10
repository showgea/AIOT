import requests
import json
from common.get_result_db import get_result_from_sql
from config import readcfg

header = readcfg.header
url = readcfg.url
sql = "select request_msg from iot_send_record where app_id='7be1984f0556276133336839' " \
          "order by create_time DESC limit 1;"


def user_get_authcode(account, countryCode=None, authCodeType=None):
    url_ = url + "/app/v1.0/lumi/user/get/authcode"
    json_ = {
        "account": account,
        "countryCode": countryCode,
        "authCodeType": authCodeType
    }
    list_ = ["account", "countryCode", "authCodeType"]
    num = 0
    for i in (account, countryCode, authCodeType):
        if "@" in account:
            json_ = {"account": account, "authCodeType": authCodeType}
        else:
            if i is None:
                json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_get_authcode("18682246872", "+86", "1")
    # result_sql_ = get_result_from_sql(sql)[0]
    # code_ = json.loads(result_sql_)["code"]
    print(result_main.text)
