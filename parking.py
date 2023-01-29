import math
in_hr=60*int(input("เวลาเข้า(ชั่วโมง) : "))
in_m=int(input("เวลาเข้า(นาทั) : "))
out_hr=60*int(input("เวลาออก(ชั่วโมง) : "))
out_m=int(input("เวลาออก(นาที) : "))
sum_in=in_hr+in_m
sum_out=out_hr+out_m
result=u=sum_out-sum_in
res=sum_out-sum_in
hours = res/60
hours = math.ceil(hours)
fee = 0
for i in range(0,1):
    if res<=30:
        fee = 0
        print("เวลาจอด", res, "นาที","ค่าจอดรถ", fee * hours,"บาท")
    elif hours>0.30 and hours<=3:
        fee = 10
        print("เวลาจอด", hours,"ชั่วโมง","ค่าจอดรถ", fee * hours,"บาท")
    elif hours>=4 and hours<=6:
        fee = 20
        print("เวลาจอด", hours,"ชั่วโมง","ค่าจอดรถ", fee * hours,"บาท")
    else:
        fee = 300
        print("เวลาจอด", hours,"ชั่วโมง" ,"ค่าจอดรถ", fee,"บาท")




# in_hr=60*int(input("เวลาเข้า(ชั่วโมง) : "))
# in_m=int(input("เวลาเข้า(นาทั) : "))
# out_hr=60*int(input("เวลาออก(ชั่วโมง) : "))
# out_m=int(input("เวลาออก(นาที) : "))
#
# sum_in=in_hr+in_m
# sum_out=out_hr+out_m
# result=u=sum_out-sum_in
#
# res=sum_out-sum_in
# fee = 0
# for i in range(0,1):
#     if res<=30:
#         print("ฟรี")
#     elif res>30 and res<=180:
#         print("10 บาท")
#     elif res>=240 and res<=360:
#         print("20")
#     else:
#         print("300 บาท")
