import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        '''
        某些软件在保存一个以UTF-8编码的文件时，默认会在文件开始的地方插入三个不可见的字符（0xEF 0xBB 0xBF，即BOM）。
        在有些软件可以控制是否插入BOM。如果在有BOM的情况下，在读取时需要自己去掉这些字符，python中的codecs module定义了这个常量'''
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")  # 重写覆盖原文件
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(configPath, 'w+') as f:
            self.cf.write(f)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
