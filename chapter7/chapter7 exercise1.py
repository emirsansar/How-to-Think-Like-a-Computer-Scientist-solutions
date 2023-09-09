#Write a function to count how many odd numbers are in a list.

def count_odd_numbers(list):
    count = 0
    for i in list:
        if i%2==1:
            count += 1
    return count

list_numbers = [1,2,3,4,5]

print( count_odd_numbers(list_numbers) )