a= 0 
total = 0
times = 0
while True:
    num=int(input("成績? 如果想退出請打'99999'"))
    if num==99999:
        break
    else:
        total += num
        times += 1
    

print("總分是"+ str(total),"平均是"+ str(total/times)[:1:3])
        