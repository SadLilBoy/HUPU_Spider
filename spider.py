import re
import datetime


def find_name(html):
    res = r'itemprop="name">(.*?)<\/'
    return re.findall(res, html, re.S | re.M)


def find_gender(html):
    res = r'itemprop="gender">(.*?)<\/'
    final_gender = re.findall(res, html, re.S | re.M)
    if len(final_gender) > 0:
        return final_gender[0]
    else:
        return 'null'


def find_address(html):
    res = r'itemprop="address">(.*?)<\/'
    final_place = re.findall(res, html, re.S | re.M)
    if len(final_place) == 0:
        return 'null'
    elif len(re.findall(r'(.*?)省', final_place[0], re.S | re.M)) > 0:
        return re.findall(r'(.*?)省', final_place[0], re.S | re.M)[0]
    elif len(re.findall(r'(.*?)市', final_place[0], re.S | re.M)) > 0:
        return re.findall(r'(.*?)市', final_place[0], re.S | re.M)[0]
    elif len(re.findall(r'(.*?)自', final_place[0], re.S | re.M)) > 0:
        return re.findall(r'(.*?)自', final_place[0], re.S | re.M)[0]
    elif len(re.findall(r'(.*?)特', final_place[0], re.S | re.M)) > 0:
        return re.findall(r'(.*?)特', final_place[0], re.S | re.M)[0]


def find_credit(html):
    res = r'声望：</span>(\d+)'
    final_credit = re.findall(res, html, re.S | re.M)
    if len(final_credit) > 0:
        return final_credit[0]
    return 0


def find_level(html):
    res = r'等级：</span>(\d+)'
    final_level = re.findall(res, html, re.S | re.M)
    if len(final_level) > 0:
        return final_level[0]
    return 0


#   单位：小时
def find_online_time(html):
    res = r'在线时间：</span>(\d+)'
    final_ol_t = re.findall(res, html, re.S | re.M)
    if len(final_ol_t) > 0:
        return final_ol_t[0]
    return 0


def find_join_time(html):
    res = r'加入时间：</span>([\d\-]+)'
    final_jn_t = re.findall(res, html, re.S | re.M)
    if len(final_jn_t) > 0:
        return final_jn_t[0]
    return '9999-99-99'


def find_offline_time(html):
    res = r'上次登录：</span>([\d\-\u4e00-\u9fa5]+)'
    final_of_t = re.findall(res, html, re.S | re.M)
    if len(final_of_t) > 0:
        result = final_of_t[0]
    else:
        result = '1975-01-01'
    if result == '今天':
        return str(datetime.datetime.now()).split().pop(0)
    elif result == '昨天':
        return str(getYesterday())
    elif result == '前天':
        return str(getDayBeforeYesterday())
    else:
        return result


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

def getDayBeforeYesterday():
    today = datetime.date.today()
    twodays = datetime.timedelta(days=2)
    theday = today - twodays
    return theday