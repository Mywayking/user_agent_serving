"""
-------------------------------------------------
   Author :       galen
   date：          2018/3/19
-------------------------------------------------
   Description:
-------------------------------------------------
"""
import os
import re


def read_txt(filename):
    """读取文件"""
    with open(filename, 'r') as f:
        while True:
            lines = f.readline().strip('\n')
            if not lines:
                break
            yield lines


def save_to_data_file(data, filename, mode="a"):
    """保存文件"""
    with open(filename, mode)as f:
        f.write(data)


def save_to_datas_file(data_list, filename, mode="a"):
    """保存文件"""
    with open(filename, mode)as f:
        for data in data_list:
            f.write(data + "\n")


def deduplication_data(data_path):
    """数据shell命令去重"""
    command = "awk '!a[$0]++' {0}|sort -o {1}".format(data_path, data_path)
    print(command)
    os.system(command)


def delete_existed_file(path):
    """删除已存在文件"""
    if os.path.exists(path):
        print("删除已存在文件夹:{}".format(path))
        os.remove(path)
    else:
        print("不存在文件夹:{}".format(path))


def clean_space(content):
    """多个空格转一个"""
    return re.sub(' +', ' ', content)


def delete_space(content):
    """多个空格转无"""
    return re.sub(' +', '', content)


def whether_repeat(keywords, keyword):
    """匹配词 去重"""
    if keywords.upper() == keyword.upper():
        return True
    models = keywords.split("|")
    for m in models:
        if m.upper() == keyword.upper():
            return True
    return False


def format_device_ua(ua):
    """
    格式如下：Zte^yuanhang 4^2^ZTE BA610C|ZTE BA610T|ZTE BLADE A610C
    格式化规则：
    1.brand  长度小于4 全部大写
    2.model 全部为 title 格式
    3.keywords 全部大写
    :param ua:
    :return:
    """
    ua_list = ua.split("^")
    if len(ua_list[0]) >= 4:
        ua_list[0] = ua_list[0].title()
    else:
        ua_list[0] = ua_list[0].upper()
    ua_list[1] = ua_list[1].title()
    ua_list[3] = ua_list[3].upper()
    return "^".join(ua_list)


def get_device_ua(s):
    # m = re.match(".*\((.*)\).*", s)
    # return m.group(1)
    return re.findall(r'[^()]+', s)[1]


def get_keywords(device):
    device_list = device.split(";")
    for d in device_list:
        if "build/" in d.lower():
            build = d.lower().split("build/")[0].strip()
            if len(build) == 0:
                continue
            return build
        elif "miui/" in d.lower():
            build = d.lower().split("miui/")[0].strip()
            if len(build) == 0:
                continue
            return build
    return None

if __name__ == '__main__':
    print(get_device_ua("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 Chrome/65.0.3325.162 Safari/537.36"))
