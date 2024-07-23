import math
a=1
sum=0
temp=a
while(temp>0):
    digit=temp%10
    sum+=math.factorial(digit)
    temp//=10
if(sum==a):
    print('strong number')
else:
    print('not strong number')
