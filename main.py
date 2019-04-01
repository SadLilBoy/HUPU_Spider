from urllib import request
import spider
import counter

top = 175274883164927

# 999999999999999

usernumber = 0
gender = {'male': 0, 'female': 0, 'null': 0}
address = {'null': 0}
max_credit = 0
max_level = 0
total_online_time = 0
avg_online_time = 0
oldest_man = 99999999
activity = {'pos': 0, 'neg': 0}

for i in range(175274883161927, top):
    html = request.urlopen('https://my.hupu.com/' + str(i)).read().decode('utf-8')
    if spider.find_name(html):
        usernumber = counter.c_user(usernumber, html)
        counter.c_address(address, html)
        counter.c_gender(gender, html)
        max_credit = counter.c_credit(max_credit, html)
        max_level = counter.c_level(max_level, html)
        total_online_time = counter.c_plus_online_time(total_online_time, html)
        oldest_man = counter.c_join_time(oldest_man, html)
        counter.c_offline_time(activity, html)
        print('正在爬取用户： ' + str(i) + ' 的个人简介')
avg_online_time = total_online_time / (top-175274883161927)

f = open("hupu_user_data.txt", "w")
f.write("注册用户数量：    " + str(usernumber) + '\r\n')
f.write("性别比例：    " + str(gender) + '\r\n')
f.write("用户所在的地区：    " + str(address) + '\r\n')
f.write("最高的社区声望：    " + str(max_credit) + '\r\n')
f.write("最高的社区等级：    " + str(max_level) + '\r\n')
f.write("用户在线时长：    " + str(avg_online_time) + '\r\n')
f.write("第一个用户的注册时间：    " + str(oldest_man) + '\r\n')
f.write("活跃用户占比：    " + str(activity) + '\r\n')
f.close()
