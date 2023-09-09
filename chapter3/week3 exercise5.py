# Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#a
for a in xs:
    print(a)

#b
for b in xs:
    print(str(b) + "\t" + str(b*b))

#c
sum = 0
for c in xs:
    sum += c
print(sum)

#d
multi = 1
for d in xs:
    multi *= d
print(multi)