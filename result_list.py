try:
    with open("ch5_data/james.txt", "r") as james_list:
        james = james_list.readline().strip().split(",")
    with open("ch5_data/julie.txt", "r") as julie_list:
        julie = julie_list.read().strip().split(",")
    with open("ch5_data/mikey.txt", "r") as mikey_list:
        mikey = mikey_list.read().strip().split(",")
    with open("ch5_data/sarah.txt", "r") as sarah_list:
        sarah = sarah_list.read().strip().split(",")

    print(james)
    print(julie)
    print(mikey)
    print(sarah)
except IOError as io_err:
    print("file error:" + str(io_err))
except ValueError as var_err:
    print("value error:" + str(var_err))
