# Incomplete



def printboard(x,y):
    print("| 0 | 1 | 2 |")
    print("----|---|----")
    print("| 3 | 4 | 5 |")
    print("----|---|----")
    print("| 6 | 7 | 8 |")

 


x = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
z = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
turn = 1  # 1 for X and 0 for 0
while True:
    printboard(x,z)
    if turn == 1 :
        print("X's chance ")
        value = int(input("Please Enter a value : "))
        x[value] = 1
    else:
        print("Z's Chance")
        value = int(input("Please Enter a value : "))
        z[value] = 0
    break
