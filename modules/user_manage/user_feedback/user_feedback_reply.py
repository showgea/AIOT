import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_feedback_reply(feedbackId, reply):
    url_ = url + "/app/v1.0/lumi/user/feedback/reply"
    json_ = {
        "feedbackId": feedbackId,
        "reply": reply
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % json_)
    r = requests.post(url=url_, json=json_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_feedback_reply("FB.613704809791098880", "reply123")
    print(result_main.text)
