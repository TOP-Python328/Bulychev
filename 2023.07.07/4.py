n,s,p=int(input()),0,1
while n>0: c=n%10; p*=c; s+=c; n//=10
print('Сумма цифр =',s)
print('Произведение цифр =',p)