import func

try:
	# 打开四位选手的成绩列表，去除行首位空白，以逗号为分界符，取得成绩存入相应列表中
	# （1）一般方法
	# with open("ch5_data/james.txt", "r") as james_list:
	# 	james = james_list.readline().strip().split(",")
	# with open("ch5_data/julie.txt", "r") as julie_list:
	# 	julie = julie_list.read().strip().split(",")
	# with open("ch5_data/mikey.txt", "r") as mikey_list:
	# 	mikey = mikey_list.read().strip().split(",")
	# with open("ch5_data/sarah.txt", "r") as sarah_list:
	# 	sarah = sarah_list.read().strip().split(",")
	# （2）调用get_coach_data函数，读取选手成绩列表，并去除首尾空白，以逗号为分界符
	james = func.get_coach_data("ch5_data/james.txt")
	julie = func.get_coach_data("ch5_data/julie.txt")
	mikey = func.get_coach_data("ch5_data/mikey.txt")
	sarah = func.get_coach_data("ch5_data/sarah.txt")

	# 将选手成绩格式统一
	# （1）一般方法
	# james_format = []
	# julie_format = []
	# mikey_format = []
	# sarah_format = []
	#
	# for time_string in james:
	# 	james_format.append(sanitize.sanitize(time_string))
	# for time_string in julie:
	# 	julie_format.append(sanitize.sanitize(time_string))
	# for time_string in mikey:
	# 	mikey_format.append(sanitize.sanitize(time_string))
	# for time_string in sarah:
	# 	sarah_format.append(sanitize.sanitize(time_string))
	# （2）利用list comprehension
	james_format = [func.sanitize(time_string) for time_string in james]
	julie_format = [func.sanitize(time_string) for time_string in julie]
	mikey_format = [func.sanitize(time_string) for time_string in mikey]
	sarah_format = [func.sanitize(time_string) for time_string in sarah]

	# 去除列表中的重复值
	# (1)一般方法

	# james_unique = []
	# julie_unique = []
	# mikey_unique = []
	# sarah_unique = []
	# for item in james_format:
	# 	if item not in james_unique:
	# 		james_unique.append(item)
	# for item in julie_format:
	# 	if item not in julie_unique:
	# 		julie_unique.append(item)
	# for item in mikey_format:
	# 	if item not in mikey_unique:
	# 		mikey_unique.append(item)
	# for item in sarah_format:
	# 	if item not in sarah_unique:
	# 		sarah_unique.append(item)

	# （2）利用set去除重复项
	print(sorted(set(james_format))[0:3])
	print(sorted(set(julie_format))[0:3])
	print(sorted(set(mikey_format))[0:3])
	print(sorted(set(sarah_format))[0:3])

	# 将选手成绩排序后打印到屏幕上

	# print(sorted(james_format, reverse=True))# 降序排列
	# print(sorted(julie_format))
	# print(sorted(mikey_format))
	# print(sorted(sarah_format))


except IOError as io_err:
	print("file error:" + str(io_err))
except ValueError as var_err:
	print("value error:" + str(var_err))
