import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def ifttt_subject_trigger_query(subjectModel):
    url_ = url + "/app/v1.0/lumi/ifttt/subject/trigger/query"
    params_ = {
        "subjectModel": subjectModel
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = ifttt_subject_trigger_query("lumi.gateway.aqhm01")
    print(result_main.text)
