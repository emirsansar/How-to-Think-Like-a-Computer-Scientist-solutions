#Extend to_secs so that it can cope with real values as inputs. It should always return an integer number of seconds (truncated towards zero):

def to_secs(hours,minutes,seconds):
    sum = int(hours*60*60 + minutes*60 + seconds)    # we should calculate "sum" as an integer.
    return sum

print(to_secs(2,30,10))