size = int(input("Insert triangle size: ")) + 1

for x in range(1, size):
    print("*"*x, " "*size) #Triangle on left side
    #print(" "*size, "*"*x) Triange on right side

    size-=1