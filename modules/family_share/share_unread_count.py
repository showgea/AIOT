import requests
import json
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def unread_count():
    url_ = url + "/app/v1.0/lumi/position/share/message/unread/count"
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    r = requests.get(url=url_, headers=header_Gary, proxies=proxies, verify=False)
    # count = json.loads(r.text)["result"]["count"]
    return r.text


if __name__ == '__main__':
    result_main = unread_count()
    print(result_main)
