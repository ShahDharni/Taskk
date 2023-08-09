# Armstrong Number = 153 -- 1*1*1=1, 5*5*5=125, 3*3*3=27, 1+125+27=153

n=int(input("Enter number :"))                                                            # n=153
i=n                                                                                       # i=153
count=0
while i>0:                 ## This code is used to count the digits of the number
    i=i//10                ## i= 153//10 =15//10= 1//10=0 
    count=count+1          ## count=1,2,3

i=n
sum=0
while i>0: 
    digit=i%10             ## digit= 153%10 = 3
    x=1              
    prod=1
    while(x <= count):     ## 1 <= 3
        prod=prod*digit    ## prod = 1*3 = 3
        x=x+1              ## x= 1+1=2
    sum=sum + prod
    i=i//10

if sum==n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number") 
