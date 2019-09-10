import random
import time
import string

random_string = ''.join(random.sample(string.ascii_letters, 4)) + str(int(time.time()))
random_lower_string = ''.join(random.sample(string.ascii_lowercase, 4)) + str(int(time.time()))
random_upper_string = ''.join(random.sample(string.ascii_letters, 16))
random_repository_name = ''.join(random.sample(string.ascii_letters, 8)) +\
                         ''.join(random.sample(string.digits, 4))


phone_pre = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
           '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']

random_phone = random.choice(phone_pre) + ''.join(random.sample(string.digits, 8))


def phone_num(num):
    """
    该方法用于生成手机号码
    num: 传入数量为生成手机号码数量
    :return: 保存到文件phone_num.txt中num个手机号

    """
    all_phone_nums = set()
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
           '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    for i in range(num):
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        res = start + end + '\n'
        all_phone_nums.add(res)
    with open('phone_num.txt', 'w', encoding='utf-8') as fw:
        fw.writelines(all_phone_nums)


if __name__ == '__main__':
    print(random_string, random_lower_string, random_phone, random_repository_name)
    # print(random_phone)
