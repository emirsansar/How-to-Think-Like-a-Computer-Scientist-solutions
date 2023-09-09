s = "If we took the bones out, it wouldn't be crunchy, would it?"

print(s.split())
# ['If', 'we', 'took', 'the', 'bones', 'out,', 'it', "wouldn't", 'be', 'crunchy,', 'would', 'it?']

print(type(s.split()))
# <class 'list'>

print(s.split("o"))
# ['If we t', '', 'k the b', 'nes ', 'ut, it w', "uldn't be crunchy, w", 'uld it?']

print(s.split("i"))
# ['If we took the bones out, ', "t wouldn't be crunchy, would ", 't?']

print("0".join(s.split("o")))
# If we t00k the b0nes 0ut, it w0uldn't be crunchy, w0uld it?

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    yeni = new.join(s.split(old))
    return yeni

print (myreplace(",", ";", "this, that, and some other thing") == "this; that; and some other thing")
print (myreplace(" ", "**","Words will now      be  separated by stars.") == "Words**will**now**be**separated**by**stars.")