import spider
import re
import datetime


def c_user(n, html):
    if spider.find_name(html):
        n += 1
    return n


def c_gender(g, html):
    if spider.find_gender(html) == '男':
        g['male'] += 1
    elif spider.find_gender(html) == '女':
        g['female'] += 1
    else:
        g['null'] += 1


def c_address(add, html):
    place = spider.find_address(html)
    if place == 'null':
        add['null'] += 1
    elif place in add:
        add[place] += 1
    else:
        add[place] = 1


def c_credit(c, html):
    current = int(spider.find_credit(html))
    if current > c:
        return current
    else:
        return c


def c_level(l, html):
    current = int(spider.find_level(html))
    if current > l:
        return current
    else:
        return l


def c_plus_online_time(ot, html):
    ot += int(spider.find_online_time(html))
    return ot


def c_join_time(o, html):
    newer = int(re.sub(r'\-', '', spider.find_join_time(html), re.S | re.M))#0629
    older = o
    if newer <= older:
        return newer
    else:
        return older


def c_offline_time(activity, html):
    offt = spider.find_offline_time(html)
    t = datetime.datetime.strptime(offt, "%Y-%m-%d")
    diff = (datetime.datetime.now() - t).days
    if diff > 365:
        activity['neg'] += 1
    else:
        activity['pos'] += 1


