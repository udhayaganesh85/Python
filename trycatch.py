while True:
    try:
        a = input("Number")
        print(5/int(a))
    except ZeroDivisionError:
        print("Try Again")
    except:
        print("Other Exception")