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


def app_additional_file_upload():
    url_ = url + "/app/v1.0/lumi/app/additional/file/upload"
    file = {"file": open("C:\\AIOT\\test.jpg", "rb")}
    print(file)
    upload_data = {"file": "C:\\AIOT\\test.jpg"}
    r = requests.post(url_, upload_data, headers=header_Gary, files=file)
    return r


if __name__ == '__main__':
    result_main = app_additional_file_upload()
    print(result_main.text)
