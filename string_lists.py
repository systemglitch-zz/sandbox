a = [1,2,3,2,1]
b = [3]
c = [1,2,3,4,3,2,1]
d = [1,2,3,4,5,3,2,1]
e = "thisissisiht"
f = "thisisnotthis"
g = [1,3,1]

def isPalindrome(myList):
    while len(myList) >= 0:
        print(len(myList))
        print(myList)

        if len(myList) <= 1:
            print("your list is a palindrome")
            break
        
        elif myList[0] != (myList[len(myList)-1]):
            print("your list is NOT a palindrome")
            break

        else:
            myList = myList[1:(len(myList)-1)]


