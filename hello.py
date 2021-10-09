#a = [str(i) for i in input().split()]
list = open("words.txt", "r")
words = []
for k in list:
    striped_line = k.strip()
    line_list = striped_line.split()
    words.append(line_list)
list.close()
print(words)

words1 = []
del words[0]
for x in words:
    print(x[0])
    inp = input("Please enter answer: ")
    print(inp)
    if inp == x[1]:
        print("The correct answer :", inp)
        print("=============================")
    else:
        print("wrong input")
