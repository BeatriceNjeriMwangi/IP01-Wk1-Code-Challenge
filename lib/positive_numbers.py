def positive_numbers(a ,b ,c):
    if( a>0 and b>0):#if number is greater that 0 its said to be positive number.  hence true
        return True
    elif( a<0 and b<0):#if number is less than 0 its said to be negative number.hence false
        return False
print(positive_numbers(2,4,-3)) 
print(positive_numbers(4,6,10) )
print(positive_numbers(-1,-2,-4))  