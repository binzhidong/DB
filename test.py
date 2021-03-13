# -*- coding: UTF-8 -*-
'''
@Project ：DB 
@File ：test.py
@Author ：binzhidong
@Date ：2021/3/10 20:03 
'''
from concern.config import Config
import yaml
'''
file_name = './experiments/seg_detector/ic15_resnet18_deform_thre.yaml'
conf_test = Config()
#conf_test.load(data)
#print(conf_test.compile(conf_test.load(file_name)))
with open('./result.yaml', "w", encoding="utf-8") as f:
    yaml.dump(conf_test.compile(conf_test.load(file_name)), f)

'''
'''

def trace(func):
    def callfunc(self, *args, **kwargs):
        debug_log = open('debug_log.txt', 'a')
        debug_log.write('Calling %s: %s ,%s\n' % (func.__name__, args, kwargs))
        result = func(self, *args, **kwargs)
        debug_log.write('%s returned %s\n' % (func.__name__, result))
        debug_log.close()
        return result

    return callfunc


class LogMeta(type):
    def __new__(cls, name, bases, dct):
        print('name: ', name)
        print('bases: ', bases)
        print(('dct: ', dct))
        for k, v in dct.items():
            if k.startswith('__'):
                continue
            if not callable(v):
                continue
            dct[k] = trace(v)
        return type.__new__(cls, name, bases, dct)


class Foo(metaclass= LogMeta):

    num = 0

    def spam(self):
        print(Foo.num)
        Foo.num += 1
        return Foo.num


a = Foo()
a.spam()
'''


