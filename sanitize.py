'''
函数sanitizer，接受一个字符串，将其中的：和-替换为.。
'''
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)
