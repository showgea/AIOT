import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def res_statistics_support_query(subjectModel=None):
    url_ = url + "/app/v1.0/lumi/res/statistics/support/query"
    params = {
        "subjectModel": subjectModel
    }
    if subjectModel is None:
        params.pop("subjectModel")
    print("请求数据：%s" % params)
    r = requests.get(url=url_, params=params, headers=header_Gary)
    return r


if __name__ == '__main__':
    result_main = res_statistics_support_query()
    print(result_main.text)
