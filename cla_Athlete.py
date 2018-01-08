# 建立继承于list的类AthleteList
import func


class AthleteList(list):
	def __init__(self, a_name, a_dob=None, a_times=[]):
		list.__init__([]) # 初始化类
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)

	def top3(self):
		return sorted(set([func.sanitize(t) for t in self]))[0:3]


# 函数get_coach_data3,接受选手成绩文件名，去除前后空白，以，为分界符分割成绩，返回成绩列表。
# chap6升级函数3，返回继承类

def get_coach_data3(filename):
	try:
		with open(filename) as f:
			data_list = f.readline().strip().split(',')
			cla = AthleteList(data_list.pop(0), data_list.pop(0), func.sanitize(data_list))
			return cla
	except IOError as io_err:
		print("file error:" + str(io_err))
		return None


# james = get_coach_data3("ch6_data/james2.txt")
# print(james.name + "'s fastest times are " + str(james.top3()))
