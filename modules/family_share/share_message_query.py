import requests
import json
from common.connect_db import ExecuteSQL, ExecuteSQLAll
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def message_query(size=None, start_index=None, start_time=None, end_time=None, state=None):
    url_ = url + "/app/v1.0/lumi/position/share/message/query"
    json_ = {
        "size": size,
        "startIndex": start_index,
        "startTime": start_time,
        "endTime": end_time,
        "state": state
    }
    list_ = ["size", "startIndex", "startTime", "endTime", "state"]
    num = 0
    for i in (size, start_index, start_time, end_time, state):
        if i is None:
            json_.pop(list_[num])
        num += 1
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r.text


def get_result_from_sql():
    name = "iot_test"
    sql = "SELECT * FROM iot_position_share_record WHERE " \
          "host_user_id = '38715a6d7c0608f7.606065919364653057' AND state IN (1, 7) " \
          "AND create_time BETWEEN '2019-8-1 12:00:00' AND '2019-8-30 12:0:0' LIMIT 100;"
    connect = ExecuteSQLAll(name, sql)
    execute_result = connect.execute_sql()
    return execute_result


if __name__ == '__main__':
    result_main = message_query(size="100", start_index=0, start_time="1564632000000", end_time="1567137600000", state="[17]")
    print(result_main)
    result_main_length = len(json.loads(result_main)["result"])
    print(result_main_length)
    # result_main = get_result_from_sql()
    # print(len(result_main))
