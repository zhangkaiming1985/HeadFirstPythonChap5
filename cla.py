import func


class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def top3(self):
		return sorted(set([func.sanitize(t) for t in self.times]))[0:3]

	def add_time(self, new_time):
		self.times.append(str(new_time))

	def add_times(self, new_times):
		self.times.extend(new_times)



# 函数get_coach_data2,接受选手成绩文件名，去除前后空白，以，为分界符分割成绩，返回成绩列表。
# chap6升级函数2，使得函数返回对象

def get_coach_data2(filename):
	try:
		with open(filename) as f:
			data_list = f.readline().strip().split(',')
			data_object = Athlete(data_list.pop(0), data_list.pop(0), data_list)
			return data_object
	except IOError as io_err:
		print("file error:" + str(io_err))
		return None


sarah = get_coach_data2("ch6_data/sarah2.txt")
julie = get_coach_data2("ch6_data/julie2.txt")
mikey = get_coach_data2("ch6_data/mikey2.txt")
james = get_coach_data2("ch6_data/james2.txt")

sarah.add_time(5.1)
sarah.add_times(['6.1', '0.2'])

print(sarah.name + "'s fastest times are " + str(sarah.top3()))
print(julie.name + "'s fastest times are " + str(julie.top3()))
print(mikey.name + "'s fastest times are " + str(mikey.top3()))
print(james.name + "'s fastest times are " + str(james.top3()))


print(sarah.times)