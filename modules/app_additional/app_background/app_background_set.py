import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def app_background_set(positionId=None):
    url_ = url + "/app/v1.0/lumi/app/background/set"
    json_ = {
        "backPicUrl": "https://cdn.cnbj2.fds.api.mi-img.com/lumiaiot/service/icon/background/igkKS08A6AWCeg3ueKhoYkOxJKWSw93VGucYFl5R2622870976499307.20190802182729.jpg",
        "positionId": positionId
    }
    if positionId is None:
        json_.pop("positionId")

    print("请求数据：%s" % json_)
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = app_background_set(positionId=None)
    print(result_main.text)
