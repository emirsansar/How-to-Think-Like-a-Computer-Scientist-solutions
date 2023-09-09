#Print a neat looking multiplication table like this:

layout = "{0:4}{1}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>5}{12:>5}"
print(layout.format("","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
print("\t:-----------------------------------------------")

for i in range(1,13):
    print(layout.format(str(i)+":", i, i * 2, i * 3, i * 4, i * 5, i * 6, i * 7, i * 8, i * 9, i * 10, i * 11, i * 12))