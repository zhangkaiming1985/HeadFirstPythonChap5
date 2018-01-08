import pickle
import func
from cla_Athlete import AthleteList


# 函数get_coach_data3,接受选手成绩文件名，去除前后空白，以，为分界符分割成绩，返回成绩列表。
# chap6升级函数3，返回继承类

def get_coach_data3(filename):
	try:
		with open(filename) as f:
			data_list = f.readline().strip().split(',')
			cla = AthleteList(data_list.pop(0), data_list.pop(0), data_list)
			return cla
	except IOError as io_err:
		print("file error:" + str(io_err))
		return None


# 函数put_to_store(),按照名字为索引，将选手信息储存在字典中，之后腌制
def put_to_store(files_list):
	all_athletes = dict()
	for each_file in files_list:
		ath = get_coach_data3(each_file)
		all_athletes[ath.name] = ath

	try:
		with open('athletes.pickle', 'wb') as athf:
			pickle.dump(all_athletes, athf)
	except IOError as ioerr:
		print("file error:" + ioerr)
	return all_athletes


# 函数get_from_store(),将腌制的数据提取，放入字典并返回
def push_from_store():
	all_athletes = dict()
	try:
		with open('athletes.pickle', 'rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print("file error:" + ioerr)
	return all_athletes

the_files = ["ch6_data/james2.txt", "ch6_data/julie2.txt", "ch6_data/mikey2.txt", "ch6_data/sarah2.txt"]
data = put_to_store(the_files)
# print(data)
print("data:")
for each_ath in data:# each_ath的值为data的键值（姓名）
	print(data[each_ath].name + "'s birthday is " + data[each_ath].dob)

data_copy = push_from_store()
print("data_copy:")
for each_ath in data_copy:
	print(data_copy[each_ath].name + "'s birthday is " + data_copy[each_ath].dob)
