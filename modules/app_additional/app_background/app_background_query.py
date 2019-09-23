import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def app_background_query(positionId=None):
    url_ = url + "/app/v1.0/lumi/app/background/query"
    params_ = {
        "positionId": positionId
    }
    if positionId is None:
        params_.pop("positionId")

    print("请求数据：%s" % params_)
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_background_query(positionId=None)
    print(result_main.text)
