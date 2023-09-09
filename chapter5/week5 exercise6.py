#Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to this scheme

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

def exam_grade(n):
    for i in n:
        if i>=75:
            print(str(i) + " First. ")
        elif 75>i and  i>= 70:
            print(str(i) + " Upper Second. ")
        elif 70>i and i>=60 :
            print(str(i) + " Second")
        elif 60>i and i>=50 :
            print(str(i) + " Third")
        elif 50>i and i>=45 :
            print(str(i) + " F1 Supp")
        elif 45>i and i>=40 :
            print(str(i) + " F2")
        else:
            print(str(i) + " F3")

exam_grade(xs)