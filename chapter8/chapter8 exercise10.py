#Write a function that recognizes palindromes. (Hint: use your reverse function to make this easy!):

import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def reverse(kelime):
    bos = ""
    for i in kelime[::-1]:   # en sondan başlayıp birer birer harfleri bos' a aktarır
        bos = bos + i
    return bos

def is_palindrome(kelime):
    tersten_kelime = reverse(kelime)

    if tersten_kelime == kelime:
        return True

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))