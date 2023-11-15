a = []
while True:
    num = input("請輸入數字，輸入no number結束")
    if num == "no number":
        break
    else :
        a.append(num)
    
a.sort()
print("最大值:",max(a))
print("最小值", min(a))
print("第四大的值",a[-4])
print("第二小的值",a[1])
