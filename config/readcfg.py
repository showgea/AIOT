# coding:utf-8
import os
import configparser
import random
from common import data_file

#
cur_path = os.path.dirname(os.path.realpath(__file__))
cfg_path = os.path.join(cur_path, 'config.ini')
# print(cfg_path)
# 定义con
con = configparser.ConfigParser()
con.read(cfg_path, encoding="utf-8-sig")

# 发送邮件参数
server = con.get("email", "server")
port = con.get("email", "port")
sender = con.get("email", "sender")
psw = con.get("email", "psw")
receiver = con.get("email", "receiver")

# 测试环境信息
url = con.get("env", "url_test")
userId_Gary = "38715a6d7c0608f7.606065919364653057"
account_Gary = "18682246872"
password = "e10adc3949ba59abbe56e057f20f883e"
account_Jenny = "13798371391"
account_mail_Gary = "guobing.tang@aqara.com"
account_mail_Jenny = "yuzhen.peng@aqara.com"
account_wrong = "guobing.tana@aqara.com"
authCode_wrong = "123456"
bindKey_Gary = "lumiEPvHM1oii9Jx"
positionId_real1_Gary = "real1.615940701625851904"
positionId_real1_Gary2 = "real1.615945282405605376"
positionId_real2_Gary = "real2.615940701667794944"
positionId_real2_Gary2 = "real2.615945282455937024"
positionId_virtual_Gary = "virtual.615960161418027008"
positionId_real1_Jenny = "real1.595330038958653440"
positionId_virtual_Jenny = "virtual.564865285266341888"
positionId_wrong = "real1.615940701625851905"
subjectId_Gary_hub = "lumi.158d0003930b2a"
subjectId_Gary_cube = "lumi.158d00026e9e32"
subjectId_Jenny = "lumi.158d000317a108"
subjectId_wrong = "lumi.158d0003930b2e"
did_Gary_hub = "lumi.158d0003930b2a"
did_Gary_cube = "lumi.158d00026e9e32"
did_Gary_unbind = "lumi.158d0001de0a77"
did_Gary_nobind = "lumi.158d0002a8dc95"
did_Jenny_hub = "virtual.69665604233767"
did_wrong = "lumi.158d0003930b2f"
hub_Model = "lumi.gateway.aqhm01"
serviceId_on = "S01615944318404558848"
serviceId_off = "S01615944373496741888"
serviceId_cube = "S01615944652489261056"
serviceId_wrong = "S01615944318404558849"
linkageId_Gary = "L.624619159041404928"
linkageId_Jenny = "L.619498025691082755"
linkageId_wrong = "L.619498025691082753"
sceneId_Gary = "AL.615944318139310080"
sceneId_Jenny = "AL.615944318139310081"
sceneId_wrong = "AL.615944318139310082"
service_name_fuzzy = "灯"
startTime = "1567267200000"
endTime = "1569816000000"
startIndex = 0
size = 100
timeZone = "+8"
iconId = "ctrl_scene_default"

ifttt_name = "testIfttt" + data_file.random_4digits
scene_name = "testScene" + data_file.random_4digits
position_name = "测试位置" + data_file.random_4digits
position_virtual_name = "测试位置-虚拟位置" + data_file.random_4digits
position_timeZone_name = "测试位置-测试时区" + data_file.random_4digits
position_default_name = "默认位置"
remark = "remark " + data_file.random_string

# 按小时：hour；按天day；按周week；按月month
dimensionType_list = ["hour", "day", "week", "month"]
dimensionType = random.choice(dimensionType_list)
# max：最大  min：最小   average：平均  frequency：次数  difference：求和
aggrType_list = ["max", "min", "average", "frequency", "difference"]
aggrType = random.choice(aggrType_list)
# ifttt(删除自动化)，scene(删除场景)，both(两者都删除)
deleteLabel = "scene"
subjectModel = "lumi.gateway.aqhm01"
# 默认为0 0不删除该自动化的历史记录 1删除该自动化的历史记录
linkageRule = "0"
# 默认0 0不删除该场景的历史记录 1删除该场景的历史记录
sceneRule = "0"

sql_linkageId = "select linkage_id from iot_user_ifttt where linkage_name like 'testIfttt%';"

sql_linkageId_Jenny = "select linkage_id from iot_user_ifttt where user_id='649952c246de69f5.564773671348994049';"

sql_sceneId = "select scene_id from iot_user_scene where scene_name like 'testScene%';"

sql_sceneId_Jenny = "select scene_id from iot_user_scene where user_id='649952c246de69f5.564773671348994049';"

sql_position_create = "select position_id from iot_position where user_id='38715a6d7c0608f7.606065919364653057' " \
              "ORDER BY create_time desc limit 1;"

sql_position_create_timeZone = "select time_zone from iot_position where user_id='38715a6d7c0608f7.606065919364653057'" \
      " ORDER BY create_time desc limit 1;"

sql_position_delete = "select position_id from iot_position where user_id='38715a6d7c0608f7.606065919364653057' " \
           "AND name like '测试位置%' ORDER BY create_time desc;"

header = {
            "Appid": "1f1615ba596299024d73efc6",
            "Lang": "zh",
            "Content-Type": "application/json"
        }
header_Gary = {
            "Appid": "1f1615ba596299024d73efc6",
            "Sign": "",
            "Userid": "38715a6d7c0608f7.606065919364653057",
            "Lang": "zh",
            "Content-Type": "application/json"
        }
header_Gary_subscribe = {
            "Appid": "1f1615ba596299024d73efc6",
            "Sign": "",
            "Userid": "38715a6d7c0608f7.606065919364653057",
            "Clientid": "12345",
            "Lang": "zhj",
            "Content-Type": "application/json"
        }
header_Jenny = {
            "Appid": "1f1615ba596299024d73efc6",
            "Sign": "",
            "Userid": "649952c246de69f5.564773671348994049",
            "Lang": "zh",
            "Content-Type": "application/json"
        }
header_Jenny_subscribe = {
            "Appid": "1f1615ba596299024d73efc6",
            "Sign": "",
            "Userid": "38715a6d7c0608f7.606065919364653057",
            "Clientid": "12345",
            "Lang": "zhj",
            "Content-Type": "application/json"
        }
# 线上环境
# url = con.get("env", "url_product")


if __name__ == '__main__':
    print(remark)
