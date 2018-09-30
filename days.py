import datetime

a = int(input("第一個日期的年:"))
b = int(input("第一個日期的月:"))
c = int(input("第一個日期的天:"))
d = int(input("第二個日期的年:"))
e = int(input("第二個日期的月:"))
f = int(input("第二個日期的天:"))

first_day = datetime.date(a,b,c)
second_day = datetime.date(d,e,f)
result = second_day-first_day
print ("總共是:",(int(result.days)),"天")
