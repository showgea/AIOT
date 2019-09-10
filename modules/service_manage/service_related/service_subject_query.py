import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def service_subject_query(subjectIds):
    url_ = url + "/app/v1.0/lumi/service/subject/query"
    params_ = {"subjectIds": subjectIds.split(",")}

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = service_subject_query("S01615944318404558848,S01615944373496741888")
    print(result_main.text)
