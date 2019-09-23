import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def res_statistics_query():
    url_ = url + "/app/v1.0/lumi/res/statistics/query"
    json_ = {
        "data":
        [
            {
            "did": "lumi.158d00031aedcd",
            "attrs":["device_lqi"],
            "aggrTypes":[4]
            }
        ],
        "dimension": "1h",
        "startTime": "1548950400000",
        "endTime": "1568188490000"
    }
    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary)
    return r


if __name__ == '__main__':
    result_main = res_statistics_query()
    print(result_main.text)
