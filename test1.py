import os
array1 = ['think', 'thought', 'thought']
lst = []
def input_list():
    k=0
    n = 2
    for i in range(0, n):
        if k < 1:
            list1 = str(input("Enter thee times: "))
            lst.append(list1)
            k += 1
            if k == 1:
                list1 = str(input("second time: "))
                lst.append(list1)
                k += 1
            if k == 2:
                list1 = str(input("Past time: "))
                lst.append(list1)
                k += 1
    print(lst)
def cmparisson():
    if array1 == lst:
        print("These two lists are similar")
    else:
        print("These two lists are different")
        print("Please compare these two lists:")
        print("correct answer:")
        print(array1)
        print("your answer:")
        print(lst)

print(input_list(), cmparisson())

