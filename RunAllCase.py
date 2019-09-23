import os
import smtplib
import time
import unittest
from HTMLTestRunner_cn import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 设置保存报告名称和路径
current_date = time.strftime("%Y-%m-%d", time.localtime())
case_path = os.path.dirname(os.path.realpath(__file__))
report_name = 'report-' + current_date + '.html'
report_path = os.path.dirname(os.path.realpath(__file__)) + '\\report\\' + report_name


def run_all_case():
    """
    1、获取当前文件夹路径
    2、加载当前路径下所有以"test"开头的用例
    """
    discovery = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    # 定义报告路径、级别、标题、描述
    runner = HTMLTestRunner(stream=open(report_path, 'wb'),
                            verbosity=2,
                            title="AIOT-接口自动化测试报告",
                            description="测试结果",
                            retry=0,
                            save_last_try=False)
    # 运行所有用例
    runner.run(discovery)


def get_report():
    """
    获取最新报告
    """
    path = os.path.dirname(os.path.realpath(__file__)) + '\\report\\'
    list_report = os.listdir(path)
    list_report.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
    new_report = list_report[-1]
    report = os.path.join(path + new_report)
    return report


def send_mail(report):
    """
    定义邮箱服务器、端口、发送人、授权码、接收人
    """

    server = "smtp.163.com"
    port = 465
    sender = "tangguobing2019@163.com"
    psw = "Woshi74110"
    receiver_list = ["guobing.tang@aqara.com"]

    # 添加写信模板
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ";".join(receiver_list)
    msg["Subject"] = u"自动化测试报告。"

    # 加附件
    f = open(report, encoding='utf-8')
    mail_body = f.read()
    f.close()

    filename = os.path.basename(report)
    print(filename)
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment; filename=%s" % filename
    msg.attach(att)

    # 加正文
    body = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(body)

    # 写信流程 授权码登录
    smtp = smtplib.SMTP_SSL(server, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver_list, msg.as_string())
    smtp.quit()


if __name__ == "__main__":
    # 运行所有用例
    run_all_case()
    # 获取最新邮件
    report_name = get_report()
    # 发送邮件
    send_mail(report_name)
