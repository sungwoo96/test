str_1 = []
str_2 = []

file = open('/Users/sungwoo/Desktop/객관식.txt', 'r')

lines = file.readlines()
for line in lines:
    print(line, end="")

# for i in range(len(lines)):
#     print(i)

file.close()