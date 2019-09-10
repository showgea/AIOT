import requests
from config import readcfg

header_Gary = readcfg.header_Gary
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def user_feedback_query_detail(feedbackId):
    url_ = url + "/app/v1.0/lumi/user/feedback/query/detail"
    params_ = {
        "feedbackId": feedbackId
    }
    proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'}

    print("请求数据：%s" % params_)
    r = requests.get(url=url_, params=params_, headers=header_Gary, proxies=proxies, verify=False)
    return r


if __name__ == '__main__':
    result_main = user_feedback_query_detail("FB.611159953679773696")
    print(result_main.text)
