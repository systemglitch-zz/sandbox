x = int(input("please enter your #: "))

num_list = []

num_range = range(1,x+1)

for i in num_range:
    if x%i == 0:
        num_list.append(i)

print(num_list)
