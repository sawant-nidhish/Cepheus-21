cords={}
generic="Model_"
for i in range(1,51):
    for j in range(1,51):
	    cords[generic + str(10000+(i-1)+(j-1)*50 +1)[1:]] = (i,j)
a=""
a=input()
while a!="~":
    try:
        print(cords[a])
    except :
        print("Model does not exist please retry")
    a=input()