def out(n):
    if(n>=10 and n<40):
        return 'X', n//10, n%10
    elif(n>=40 and n<50):
        return 'XL', n//40, n%40
    elif(n>=50 and n<90):
        return 'L', n//50, n%50
    elif(n>=90 and n<100):
        return 'XC', n//90, n%90
    elif(n==100):
        return 'C', n//100, n%100
n = int(input("Enter a number between 1-100: "))
numbers = [1,2,3,4,5,6,7,8,9]
romans = ['I','II','III','IV','V','VI','VII','VIII','IX']
#quotient for number of times
#remainder for adding
flag = True
tot = ''
t=n
rem=1000
while flag == True:
    if(rem!=0):
        romn,quo,rem = out(t)  
        tot += quo*(romn)
    if(rem==0):#if rem=0 we get that roman
        flag = False
    elif(rem in numbers):
        tot+= romans[rem-1]
        rem=0#since we found rem-1 in numbers its the last
        #step so we put rem =0 and very next loop flag will
        #be false
    else:
        t=rem
print("The integer you entered in roman number: ",tot)
    
 
