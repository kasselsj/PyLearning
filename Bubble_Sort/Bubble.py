import random
num_list = []
for i in range(10):
    num_list.append(random.randint(0, 10))

print(num_list)


i = len(num_list) -1
while i > 1:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(num_list[j], num_list[j+1]))
        print()
        if num_list[j] > num_list[j+1]:
            print("Switch \n")
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
        else:
            print("Dont Switch \n")
        j += 1
        for k in num_list:
            print(k, end="")
        print("\nEnd of round \n")
        i -= 1
        for k in num_list:
            print(k, end="")
        print("")
