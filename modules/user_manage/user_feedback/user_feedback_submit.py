import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_feedback_submit(type_, title, content, attachFileUrls=None, contactInfo=None):
    url_ = url + "/app/v1.0/lumi/user/feedback/submit"
    json_ = {
        "type": type_,
        "title": title,
        "content": content,
        "attachFileUrls": attachFileUrls,
        "contactInfo": contactInfo
    }
    list_ = ["type_", "title", "content", "attachFileUrls", "contactInfo"]
    num = 0
    for i in (type_, title, content, attachFileUrls, contactInfo):
        if i is None:
            json_.pop(list_[num])
        num += 1

    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_feedback_submit("0", "title123", "content123456", attachFileUrls=None, contactInfo=23)
    print(result_main.text)
