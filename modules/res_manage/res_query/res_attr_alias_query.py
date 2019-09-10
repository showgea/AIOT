import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def res_attr_alias_query(subjectId, attrs):
    url_ = url + "/app/v1.0/lumi/res/attr/alias/query"
    json_ = {"subjectId": subjectId, "options": attrs}
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = res_attr_alias_query("real1.611208606918021120", "argb_value")
    print(result_main.text)
