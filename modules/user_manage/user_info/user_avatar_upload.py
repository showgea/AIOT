import requests
from config import readcfg

header_Gary = {
    'Appid': "1f1615ba596299024d73efc6",
    'Sign': "",
    'Userid': "38715a6d7c0608f7.606065919364653057",
    'Token': "5882be9c0054904df30a06b0e79dabdf51e8",
    'Lang': "zh",
    'Content-Type': "multipart/form-data",
    'cache-control': "no-cache"
    }
header_Jenny = readcfg.header_Jenny
url = readcfg.url


def avatar_upload():
    url_ = url + "/app/v1.0/lumi/user/avatar/upload"
    avatarFile = {"file": open("C:/AIOT/test.jpg", "rb")}
    print(avatarFile)
    # data_ = {
    #     "avatarFile": "%s" % avatar_file
    # }
    r = requests.post(url=url_, headers=header_Gary, files=avatarFile)
    return r


if __name__ == '__main__':
    # files = {'file': open(r"C:\AIOT\test.jpg", 'rb')}
    result_main = avatar_upload()
    print(result_main.text)
