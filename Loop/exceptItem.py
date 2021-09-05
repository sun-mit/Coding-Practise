# Prints all the numbers from 0 to 10 except 3 and 6
for x in range(10):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")
	