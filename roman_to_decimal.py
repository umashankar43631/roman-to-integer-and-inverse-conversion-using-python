n =input("Enter roman number: ")

numbers = [1,4,5,9,10,40,50,90,100]
romans = ['I','IV','V','IX','X','XL','L','XC','C']
length = len(n)
i=0
sum1=0
flag = True
while i<length and flag == True:
   
    for j in range(len(n)):
        if(i<length-1):
            if n[i]+n[i+1] in romans[1::2]:
                sum1 += numbers[romans.index(n[i]+n[i+1])]
                i+=2
                break
        if n[i] in romans[0::2]:
            sum1=sum1+numbers[romans.index(n[i])]#romans .index returns the index number
            i+=1
            break
        flag = False
print(sum1)
