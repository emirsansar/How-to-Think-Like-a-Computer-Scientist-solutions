# Which of these tests fail? Explain why.

test(3 % 4 == 0)    # it should equal to 3
test(3 % 4 == 3)
test(3 / 4 == 0)    # it should equal to 0.75
test(3 // 4 == 0)
test(3+4  *  2 == 14)     # it should equal to 3 + 8 = 11
test(4-2+2 == 0)        # it should equal to 4
test(len("hello, world!") == 13)