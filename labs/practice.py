def dev_by_zero():
    x = 10/1


try:
    dev_by_zero()
except Exception as e:
    print(e)
else:
    print("nothing went wrong")    