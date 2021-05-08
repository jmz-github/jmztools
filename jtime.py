import time
from datetime import datetime
from datetime import timedelta


def isDate_YYYYMMDD(s):
    s = str(s)
    if 0 < int(getMonth(s)) < 13 and 0 < int(getDay(s)) < 31 and 0 < int(getYear(s)) < 9999:
        return True
    else:
        return False


def getYesterday(n=10):
    yesterday = datetime.today() + timedelta(-1)
    return str(yesterday)[:n]


def getTomorrow(n=10):
    tomorrow = datetime.today() + timedelta(+1)
    return str(tomorrow)[:n]


def getToday(n=10):
    today = datetime.today()
    return str(today)[:n]


def getDay(s, i=2):
    return respilt(s, i)


def getYear(s, i=0):
    return respilt(s, i)


def getMonth(s, i=1):
    return respilt(s, i)


def respilt(s, i):
    import re
    try:
        s = str(s)
        n = re.split('-| |/', s)
        n = n[i]
    except:
        return False
    else:
        return n


def get_day_begin(ts=time.time(), N=0):
    """
    N为0时获取时间戳ts当天的起始时间戳，N为负数时前数N天，N为正数是后数N天
    24 时(小时)=86400 000 毫秒
    """
    return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d', time.localtime(ts)), '%Y-%m-%d'))) + 86400 * N


def get_week_begin(ts=time.time(), N=0):
    """
    N为0时获取时间戳ts当周的开始时间戳，N为负数时前数N周，N为整数是后数N周，此函数将周一作为周的第一天
    """
    w = int(time.strftime('%w', time.localtime(ts)))
    return get_day_begin(int(ts - (w - 1) * 86400)) + N * 604800


if __name__ == "__main__":
    s = "2020-01/01 22:22"
    print(getDay(s))
