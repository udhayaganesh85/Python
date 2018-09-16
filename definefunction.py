def maxList1(num):
    max1 = 0
    for i in num:
        if max1 < i:
            max1 = i
    print(max1)
maxList1([1,2,3,4])
