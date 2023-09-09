#Write three functions that are the “inverses” of to_secs:

def hours_in(passed_seconds):
    hours = int(passed_seconds / (60*60))
    return hours

def minutes_in(passed_seconds):
    hours = int(passed_seconds / (60 * 60))
    minutes = int( ( (passed_seconds - hours*(60*60)) / 60 ))
    return minutes

def seconds_in(passed_seconds):
    hours = int(passed_seconds / (60 * 60))
    minutes = int( ( (passed_seconds - hours*(60*60)) / 60 ))
    seconds = int ( ( (passed_seconds - hours*(60*60) - minutes*60) ))
    return seconds

print(hours_in(9010))
print(minutes_in(9010))
print(seconds_in(9010))