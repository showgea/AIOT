import requests
import json
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_execute_query_detail(executeCode):
    url_ = url + "/app/v1.0/lumi/ifttt/execute/query/detail"
    json_ = {
        "executeCode": executeCode
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


def get_code():
    url_code = url + "/app/v1.0/lumi/ifttt/linkage/query/log"
    json_code = {'positionId': 'real1.615940701625851904'}
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    res = requests.post(url=url_code, json=json_code, headers=header_Gary, proxies=proxies, verify=False)
    executeCode = json.loads(res.text)["result"]["resultList"][0]["executeCode"]
    return executeCode


if __name__ == '__main__':
    r = get_code()
    # result_main = ifttt_execute_query_detail("7ff52a9d-6b9f-4515-a938-8dab498b3673")
    print(r)
