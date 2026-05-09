# recursion 
#Head Recursion 
# num = 0
# def fun():
#     global num
#     if num == 4:
#         return
#     print("Aatif Kay Hal Chaal...")
#     num += 1

#     fun()
    
# fun()


#Tail Recresion 
num = 0
def tail():
    global num
    if num == 4: 
        return
    num  += 1
    tail()
    print("Aatif")

tail()
