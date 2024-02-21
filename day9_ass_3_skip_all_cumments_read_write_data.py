# with open("day9_file_1.py","r") as file_read:
#     f2 = open("day9_ass_3_Output.py","w")
#     while True:
#         data = file_read.readline()
#         print(data)
#         for i in data:
#             if len(data) == 0:
#                 break
#             if i == '#':
#                 break
#             else:
#                 f2.write(i)

with open("day9_file_1.py", "r") as file_read:
    with open("day9_ass_3_Output.py", "w") as f2:
        while True:
            data = file_read.readline()
            if len(data) == 0:
                break
            data2 = data.split('#')[0]
            f2.write(data2 + '\n')



