import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_report_info(nickName=None, gender=None, birthday=None, area=None):
    url_ = url + "/app/v1.0/lumi/user/report/info"
    json_ = {
        "nickName": nickName,
        "gender": gender,
        "birthday": birthday,
        "area": area
    }
    list_ = ["nickName", "gender", "birthday", "area"]
    num = 0
    for i in (nickName, gender, birthday, area):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    # sql_ = "select nick_name,gender,birthday,area from iot_user where user_id='38715a6d7c0608f7.606065919364653057';"
    # res = user_report_info()
    # print(res)
    result_main = user_report_info(nickName="gary", gender=None, birthday=None, area=None)
    print(result_main.text)
