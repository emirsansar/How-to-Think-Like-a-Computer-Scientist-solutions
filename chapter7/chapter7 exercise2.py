#Sum up all the even numbers in a list.

list = [1,2,3,4,5]
sum = 0

for i in list:
    if i%2 == 0:
        sum = sum + i

print("The sum of even numbers is {}".format(sum))