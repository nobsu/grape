#!/usr/bin/python
# coding=utf-8

"""
common funcs
"""

from json2entity import jsonstr2entity
import datetime
import time

from math import pi, sin, cos, atan2, sqrt


class Xcrypt:

    def __init__(self, key=993.141592653589):
        self.key = key
        self.length = 12
        self.strbase = "5z1GydOFmAU2is7JQIk0BV9EuhWbwZXNjSo3cRgDqCtvfrK4xelanMpH8L6TPY"
        self.codelen = self.strbase[0:self.length]
        self.codenums = self.strbase[self.length:self.length + 10]
        self.codeext = self.strbase[self.length + 10:]

    def encode(self, nums):
        if not nums.isdigit():
            return nums
        rtn = ""
        numslen = len(nums)
        begin = self.codelen[numslen - 1:numslen]

        extlen = self.length - numslen - 1
        temp = "%.12f" % (int(nums) / self.key)
        temp = temp.replace('.', '')
        temp = temp[-extlen:]

        arrnumsTemp = list(self.codenums)
        arrnums = list(nums)

        for v in arrnums:
            rtn += arrnumsTemp[int(v)]

        arrextTemp = list(self.codeext)
        arrext = list(temp)
        for v in arrext:
            rtn += arrextTemp[int(v)]

        return begin + rtn

    def decode(self, code):
        if len(code) != self.length:
            return ''

        begin = code[0:1]
        rtn = ''
        length = self.codelen.find(begin)
        if length != -1:
            length += 1
            arrnums = list(code[1:1 + length])
            for v in arrnums:
                rtn += str(self.codenums.find(v))
        return rtn


def get_ip():
    """
    返回本机ip，字符串
    """
    from socket import socket, SOCK_DGRAM, AF_INET
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.connect(('baidu.com', 1))
    return sock.getsockname()[0]


def str2unixtime(strtime):
    """ 08/Jul/2014:10:29:46  2014-07-09 16:15:29"""

    publishtime = 0
    if len(strtime) == 20:
        publishtime = datetime.datetime.strptime(strtime, '%d/%b/%Y:%H:%M:%S')
    elif len(strtime) == 19:
        publishtime = datetime.datetime.strptime(strtime, '%Y-%m-%d %H:%M:%S')
    else:
        pass

    if (publishtime != 0):
        publishtime = int(time.mktime(publishtime.timetuple()))

    return publishtime


def get_now():
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return date


def get_ydat():
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-86400))
    return date


def keyword2latlngZH(keyword, city='110100'):
    """ 根据中文地址，返回经纬度

    jsonstr:
    {u'status': u'1',
     u'info': u'OK',
     u'count': u'1',
     u'geocodes': [{u'province': u'\u5317\u4eac\u5e02',
                    u'city': u'\u5317\u4eac\u5e02',
                    u'citycode': u'010',
                    u'neighborhood': {u'type': [], u'name': []},
                    u'building': {u'type': [], u'name': []},
                    u'district': u'\u4e1c\u57ce\u533a',
                    u'level': u'\u516c\u4ea4\u7ad9\u5730\u94c1\u7ad9',
                    u'adcode': u'110101',
                    u'number': [],
                    u'street': [],
                    u'location':
                    u'116.427173,39.905011',
                    u'township': [],
                    u'formatted_address': u'\u5317\\u94c1\u7ad9)'}]
     }
    """

    import urllib
    gaodeurl = 'http://restapi.amap.com/v3/geocode/geo'
    params = {}
    params.setdefault('address', keyword)
    params.setdefault('city', city)
    params.setdefault('s', 'rsv3')
    params.setdefault('key', 'dee28caa0fbbedbd93d87765c290df98')

    params_str = urllib.urlencode(params)
    url = '%s?%s' % (gaodeurl, params_str)

    try_times = 0
    content = ''
    while try_times < 5:
        try:
            url_file = urllib.urlopen(url)
            content = url_file.read()
            url_file.close()
            break
        except:
            try_times += 1
            time.sleep(try_times)
            print 'try_times: ', try_times,
            print url
            pass

    entity = jsonstr2entity(content)
    # print entity.geocodes[0].location
    if entity.count != '0':
        lng_lat = entity.geocodes[0].location.split(',')
    else:
        lng_lat = []
    return lng_lat  # 0：lng（经度），1：lat（维度）


def distance(lat1, lng1, lat2, lng2, unit='metre'):
    """ 计算两个经纬度之间的距离 """


    # 忽略微小的GPS漂移
    pi80 = pi / 180
    lat1 *= pi80
    lng1 *= pi80
    lat2 *= pi80
    lng2 *= pi80

    r = 6372.797  # mean radius of Earth in km
    dlat = lat2 - lat1
    dlng = lng2 - lng1
    a = sin(dlat / 2) * sin(dlat / 2) + cos(lat1) * \
        cos(lat2) * sin(dlng / 2) * sin(dlng / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    km = r * c
    return km * 1000


if __name__ == '__main__':
    print get_ip()
    print '北京天安门: ', keyword2latlngZH('北京天安门')
    print distance(39.941100, 116.39179, 39.907499, 116.391799)
    en = Xcrypt()
    print "20176: ", en.encode('20176')
    print "ys7BJkWwuXEZ: ", en.decode('ys7BJkWwuXEZ')
