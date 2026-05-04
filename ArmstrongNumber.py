n = 251
num = n
total = 0
nod = len(str(n))  #Total number of digit lenth

while num > 0 :
    ld = num % 10
    total = total + (ld ** nod)
    num = num // 10
if total == n:
    print(f"This is Armstrong Number : {total} ")
else:
    print(f"This is Not Armstrong Number : {total} ")
