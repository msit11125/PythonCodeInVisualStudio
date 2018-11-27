# coding=utf-8

import sys

# 1 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

n=4
r=3
for i in range(1,r+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if(i!=j and j!=k and i!=k):
                print("{} {} {}".format(i,j,k))


#2 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


money = 1200000  #int(input( ' 淨利潤: ' ))
moneyRange = [1000000,600000,400000,200000, 100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]

total = 0
for idx,standard in enumerate(moneyRange):
    if(money > standard):
        total += (money - moneyRange[idx]) * rat[idx]
        print("%d * %.3f" % ((money - moneyRange[idx]), rat[idx]) )
        money = moneyRange[idx]

print("總計 %d" % total)
     
    
#3 一個整數，它加上100後是一個完全平方數，再加上168又是一個完全平方數，請問該數是多少？

# 假設該數為x。
# 1、則：x + 100 = n 2 , x + 100 + 168 = m 2
# 2、計算等式：m 2 - n 2 = (m + n)(m - n) = 168
# 3、設置： m + n = i，m - n = j，i * j =168，i 和j 至少一個是偶數
# 4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和j 要么都是偶數，要么都是奇數。
# 5、從3 和4 推導可知道，i 與j 均是大於等於2 的偶數。
# 6、由於i * j = 168， j>=2，則1 < i < 168 / 2 + 1。
# 7、接下來將i 的所有數字循環計算即可。

for i in range(1, int(168/2) +1):
    if(168 % i ==0):
        j = 168/i
        if( i > j and (i+j)%2==0 and (i-j)%2 ==0 ): # 不重複:i>j，且i,j都是偶數
            m = ( i + j ) / 2
            n= ( i - j ) / 2 
            x = n * n - 100 
            print ( x )


#4 输入某年某月某日，判断这一天是这一年的第几天？
# 以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天
import datetime
nowDateTime = datetime.datetime.now()

year = nowDateTime.year
month = nowDateTime.month
day = nowDateTime.day
print('Today is %s' % nowDateTime.date())
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)


#5 輸入三個整數x,y,z，請把這三個數由小到大輸出。

xyz=[1,3,2]

biggest = ~sys.maxsize

for i in xyz:
    if(i> biggest):
        biggest = i

print(biggest)


#6 Fibonacci
#F0 = 0     (n=0)
#F1 = 1    (n=1)
#Fn = F[n-1]+ F[n-2](n=>2)

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
 
def fibList(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [0, 1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print("--- 費氏數列 ---")
print(fibonacci(10))
print(fib(10))
print(fibList(10))

#7 将一个列表的数据复制到另一个列表中
a = [1, 2, 3]
b = a[:]

#9 暂停一秒输出
import time
 
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1) # 暂停 1 秒

#10 格式化当前时间
print( time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )

#11 有一對兔子，從出生後第3個月起每個月都生一對兔子，小兔子長到第三個月後每個月又生一對兔子，
#假如兔子都不死，問每個月的兔子總數為多少？
#兔子的规律为数列1,1,2,3,5,8,13,21....
f1 = 1
f2 = 1
for i in range(1,20):
    if i == 1 or i ==2 :
        print('%d月後: %d對' % (i, 1))
    else:
        print('%d月後: %d對' % (i, f1))
    previos = f1
    f1 = f1 + f2 # f(n)
    f2 = previos # f(n-1)
    
#輾轉相除法 gcd(a,b) = gcd(b,r) , r= a(mod b) a除以b的餘數
def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)

ans = gcd(41,24);

print(ans)
        

#河內塔
#一環(奇數,第一步移到C):1 
#二環(偶數,第一步移到B):1 2 1 
#三環(奇數,第一步移到C):1 2 1 3 1 2 1 
#四環(偶數,第一步移到B):1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 
#五環(奇數,第一步移到C):1 2 1 2 1 2 1 4 1 2 1 3 1 2 1 5 1 2 1 2 1 2 1 4 1 2 1 3 1 2 1 
#六環:以此類推先重複一次五環的步驟(把上面五環移到B)再移6號環(移到C),然後重複一遍五環的步驟(把上面五環移到C) ...
def hanoi(n,start,temp,end):
    if(n>0):
        hanoi(n-1, start, end, temp ) # A to B
        print("move %s to %s" % (start,end))
        hanoi(n-1, temp, start, end)  # B to C

hanoi(4,"A", "B", "C")
