from math import sqrt
def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents('_google_foobar')


def f(x,l=[]):
    l.append(x)
    print(l) 

f(2)
f(3,[3,2,1])
f(3)


print("50 % 24 => {0}".format(50 % 24))
print("50 % 23 => {0}".format(50 % 23))
print("50 % 22 => {0}".format(50 % 22))
print("50 % 21 => {0}".format(50 % 21))
print("50 % 20 => {0}".format(50 % 20))
print("50 % 19 => {0}".format(50 % 19))
print("50 % 18 => {0}".format(50 % 18))
print("50 % 17 => {0}".format(50 % 17))
print("50 % 16 => {0}".format(50 % 16))
print("50 % 15 => {0}".format(50 % 15))
print("50 % 14 => {0}".format(50 % 14))
print("50 % 13 => {0}".format(50 % 13))
print("50 % 12 => {0}".format(50 % 12))
print("50 % 11 => {0}".format(50 % 11))
print("50 % 10 => {0}".format(50 % 10))
print("50 % 9 => {0}".format(50 % 9))
print("50 % 8 => {0}".format(50 % 8))
print("50 % 7 => {0}".format(50 % 7))
print("50 % 6 => {0}".format(50 % 6))
print("50 % 5 => {0}".format(50 % 5))
print("50 % 4 => {0}".format(50 % 4))
print("50 % 3 => {0}".format(50 % 3))
print("50 % 2 => {0}".format(50 % 2))

print(sqrt(50))



print(list(range(0,15,3)))
