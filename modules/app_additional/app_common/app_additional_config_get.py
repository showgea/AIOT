import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def app_additional_config_get(key, type_):
    url_ = url + "/app/v1.0/lumi/app/additional/config/get"
    params_ = {
        "key": key,
        "type": type_
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_additional_config_get("xxx", "xxx")
    print(result_main.text)
