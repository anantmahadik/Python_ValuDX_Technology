with open("day9_file_1.py","r") as file_read:
    f2 = open("day9_ass_2_Output.py","w")
    while True:
        data = file_read.readline()
        print(data)
        if len(data) == 0:
            break
        if data[0] == '#':
            continue
        else:
            f2.write(data)

