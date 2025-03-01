#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
tens = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(0,101):
    if i in tens:
        continue
    else:
        print(i)