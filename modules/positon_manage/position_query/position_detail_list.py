import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def position_detail_list(positionIds):
    url_ = url + "/app/v1.0/lumi/position/detail/list"
    params_ = {"positionIds": positionIds.split(",")}
    # for i in positionId:
    #     params_["positionIds"] = i
    print("请求数据：%s" % params_)
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}
    r = requests.get(url=url_, params=params_, proxies=proxies, headers=header_Gary, verify=False)
    return r


if __name__ == '__main__':
    result_main = position_detail_list("real2.611223399695552512,real2.611173955740295168")
    print(result_main.text)
