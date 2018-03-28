a = [1,2,3,2,1]
b = [1,2,3,4,3,2,1]
c = [1,2,3,4,5,3,2,1]
d = "thisissithis"
e = "thisisnotthis"

x = 0

for x in range(0, (len(a)-1)):
    newList = a[x:(x*(-1))]
    print(len(newList))
    print(newList)
    if newList[x] == newList[x*(-1)]:
        x += 1
    elif len(newList) == 0 or len(newList) == 1:
        print("your list is a palindrome")
        break
    else:
        print("your list is NOT a palindrome")
        x = len(a) + 1


