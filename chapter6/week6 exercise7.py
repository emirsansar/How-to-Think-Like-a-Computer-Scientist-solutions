#Write a function to_secs that converts hours, minutes and seconds to a total number of seconds.

def to_secs(hours,minutes,seconds):
    sum = hours*60*60 + minutes*60 + seconds
    return sum

print(to_secs(2,30,10))