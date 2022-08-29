import os
# dirr = "chlen"
# print(os.listdir(dirr))
#
# dirr2 = "chlen/chlenix"
# print(os.listdir(dirr2))
#
# curfilepath = os.getcwd()
# print(curfilepath)


# print(os.path.join(dirr, 'chlenix'))

# listfiles = []
# for file in os.listdir(os.getcwd()):
#     if os.path.isfile(file):
#         listfiles.append(file)
# print(listfiles)

# dirfiles = "chlen"
# listfiles = []
# for file in os.listdir(dirfiles):
#     if os.path.isfile(os.path.join(dirfiles, file)):
#         listfiles.append(file)
# print(listfiles)


# try:
#     os.mkdir("MILAN STAR - Ne takaya")
# except FileExistsError:
#     print("Path already created!")


# os.makedirs("MILAN STAR/POLNOLUNIE", exist_ok=True)


# for file in os.listdir("chlen/chlenix"):
#     if os.path.isfile(os.path.join("chlen/chlenix", file)):
#         print(file)
#     else:
#         print("no")


# with open ("lesson 10.py", "r") as txt_file:
#     # data = txt_file.read()
#     data = txt_file.readlines()
# print(data)

# with open ("lesson 10(test).py", "w") as txt_file:
#     data = "# TESTING NEW FEATURE (WRITING IN TXT)\n# SECOND STRING"
#     txt_file.writelines(data)



# def write_list(filename, my_list):
#     with open (filename, "w") as txt_file:
#         txt_file.writelines(str(my_list))
#
# def read_list(filename):
#     with open (filename, "r") as txt_file:
#         data = txt_file.read()
#         return data
#
# filename = "newtest.py"
# my_list = [1,2,3,4,5]
#
# write_list(filename,my_list)
# data_new = read_list(filename)
# print(data_new)

# import json
#
# def list_writer(filename, data):
#     with open(filename, "w") as json_file:
#         json.dump(data, json_file)
#
#
# def list_reader(filename):
#     with open(filename, "r") as json_file:
#         data = json.load(json_file)
#     return data
#
# filename = "test.json"
# data = [1,2,{3: 3.14},4,(5, 6)]
# print(data)
# list_writer(filename, data)
# data_new = list_reader(filename)
# print(type(data_new))
