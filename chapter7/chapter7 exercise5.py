#Sum all the elements in a list up to but not including the first even number. (Write your unit tests. What if there is no even number?)

list = [1,2,3,4,5]
sum = 0
control = 0

for i in list:
    if control == 0:
        if i%2 == 0:
            control = control + 1
            continue
    sum = sum + i

print("The sum of the numbers not including the first even number is {}".format(sum))