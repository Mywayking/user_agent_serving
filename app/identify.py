"""
-------------------------------------------------
   Author :       galen
   date：          2018/3/20
-------------------------------------------------
   Description:
-------------------------------------------------
"""
from app import utils
import os


class UaIdentify:
    def __init__(self):
        self.precise = {}
        self.pattern = {}
        self.path_precise = "device_ua_precise.txt"
        self.path_pattern = "ua2device_pattern.txt"
        # 项目根路径
        self.RESOURCE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/resources/"

    def data_to_dict(self, data_dic, name):
        # Zte^yuanhang 4^2^ZTE BA610C|ZTE BA610T|ZTE BLADE A610C
        path = self.RESOURCE_PATH + name
        for line in utils.read_txt(path):
            model_dict = {}
            lines = utils.format_device_ua(line).split("^")
            model_dict["brand"] = lines[0]
            model_dict["model"] = lines[1]
            model_dict["type"] = lines[2]
            model_dict["keywords"] = lines[3]
            keywords = lines[3].split("|")
            for k in keywords:
                if k not in data_dic:
                    data_dic[k] = model_dict
                    # print(self.atlas[k])

    # def device_model_detect(sekf, ua):
    #     data_dict_precise, data_dict_pattern = load_dict_precise()
    #     for prk in data_dict_precise.keys():
    #         if prk.lower() in ua.lower().replace("+", " "):
    #             return True
    #     for pak in data_dict_pattern.keys():
    #         if pak.lower() in ua.lower().replace("+", " "):
    #             return True
    #     return False
    def load_data(self):
        self.data_to_dict(self.precise, self.path_precise)
        self.data_to_dict(self.pattern, self.path_pattern)

    def identify(self, data):
        device = utils.get_device_ua(data)
        if "Windows" in device:
            return {"brand": "Windows", "model": "Windows"}
        elif "Macintosh" in device:
            return {"brand": "Apple", "model": "MacBook"}
        # (iPhone; CPU iPhone OS 10_3_2 like Mac OS X)
        # (iPad; CPU iPhone OS 10_3_2 like Mac OS X)
        elif "iphone" in device.lower() and "like Mac OS".lower() in device.lower():
            return {"brand": "Apple", "model": "iPhone"}
        elif "iPad".lower() in device.lower() and "like Mac OS".lower() in device.lower():
            return {"brand": "Apple", "model": "iPad"}
        elif "android" in device.lower():
            device_ua = utils.get_keywords(device)
            # print(self.precise)
            if device_ua is None:
                return {"brand": "", "model": ""}
            device_ua = device_ua.upper()
            if device_ua in self.precise:
                return self.precise[device_ua]
            if device_ua in self.pattern:
                return self.pattern[device_ua]
            # return {"brand": "", "model": ""}
            return None


if __name__ == '__main__':
    cu = UaIdentify()
    cu.load_data()
    print(cu.identify(
        "EDalvik/2.1.0 (Linux; U; Android 5.1; vivo V3M A Build/LMY47I)1521071999CN_20180201_MONPARIS_LPD_YSL_FR_PROGRAMMATIC_OTV_PC_MOqqPhone_15sOT"))
