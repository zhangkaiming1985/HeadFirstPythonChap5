# 函数sanitizer，接受一个字符串，将其中的：和-替换为.。
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + '.' + secs


# 函数get_coach_data,接受选手成绩文件名，去除前后空白，以，为分界符分割成绩，返回成绩列表。
# chap6升级函数，使得函数返回一个包含选手姓名、生日和成绩的字典

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data_list = f.readline().strip().split(',')
			data_dict = {
				'name' : data_list.pop(0),
				'dob' : data_list.pop(0),
				'times': sorted(set(sanitize(t) for t in data_list))
			}
			return data_dict
	except IOError as io_err:
		print("file error:" + str(io_err))
		return None
