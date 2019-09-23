import requests
from config import readcfg

header_Gary = readcfg.header_Gary
url = readcfg.url


def app_position_query_detail(positionId):
    url_ = url + "app/v1.0/lumi/app/position/query/detail"
    params_ = {
        "positionId": positionId
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    print("请求地址：%s，请求参数：%s" % (url_, params_))
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_position_query_detail("real1.615945282405605376")
    print(result_main.text)
