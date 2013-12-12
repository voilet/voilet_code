#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================


import datetime

date1 = datetime.datetime.now()
this_week_start_dt = str(date1-datetime.timedelta(days=date1.weekday())).split()[0]
this_week_end_dt = str(date1+datetime.timedelta(days=6-date1.weekday())).split()[0]
print this_week_start_dt,this_week_end_dt







#上个星期一和星期天的日期
last_week_start_dt = date1-datetime.timedelta(days=date1.weekday()+7)
last_week_end_dt = date1-datetime.timedelta(days=date1.weekday()+1)




#本月一号和最后一天的日期

y=date1.year
m = date1.month
month_start_dt = datetime.date(y,m,1)
print month_start_dt

if m == m:
    month_end_dt = datetime.date(y+1,1,1) - datetime.timedelta(days=1)
    print month_end_dt

else:
    month_end_dt = datetime.date(y,m+1,1) - datetime.timedelta(days=1)
    print month_end_dt





#上个月的第一天和最后一天

if m==1:                    #如果是1月
    start_date=datetime.date(y-1,12,1)
else:
    start_date=datetime.date(y,m-1,1)
end_date=datetime.date(y,m,1) - datetime.timedelta(days=1)




#这个季度的第一天和最后一天的日期
y=date1.year
month = date1.month
if month in (1,2,3):
    quarter_start_dt = datetime.date(y,1,1)
    quarter_end_dt = datetime.date(y,4,1) - datetime.timedelta(days=1)
elif month in (4,5,6):
    quarter_start_dt = datetime.date(y,4,1)
    quarter_end_dt = datetime.date(y,7,1) - datetime.timedelta(days=1)
elif month in (7,8,9):
    quarter_start_dt = datetime.date(y,7,1)
    quarter_end_dt = datetime.date(y,10,1) - datetime.timedelta(days=1)
else:
    quarter_start_dt = datetime.date(y,10,1)
    quarter_end_dt = datetime.date(y+1,1,1) - datetime.timedelta(days=1)


#本季度天数 及 本季度剩余的天数
# quarter_days = (quarter_end_dt - quarter_start_dt).days + 1
# quarter_rem = (quarter_end_dt - date1).days

