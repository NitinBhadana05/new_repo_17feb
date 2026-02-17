def reverse(num: int) -> int:
    temp = num
    digit = 0
    reverse_num = 0
    
    while (temp != 0):
        digit = temp % 10
        reverse_num = reverse_num* 10 + digit
        temp //= 10
    
    return reverse_num

num = int(input("enter a number "))
print("reverse of ",num,"is",reverse(num))



"""
Output

enter a number 234
reverse of  234 is 432


"""
