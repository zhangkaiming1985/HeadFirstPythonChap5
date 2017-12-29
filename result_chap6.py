import func

sarah = func.get_coach_data("ch6_data/sarah2.txt")
julie = func.get_coach_data("ch6_data/julie2.txt")
mikey = func.get_coach_data("ch6_data/mikey2.txt")
james = func.get_coach_data("ch6_data/james2.txt")

# dob:date of birthday
# (1)用普通列表实现，缺点是当数据量变大时，需要设置过多变量名称。

# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are:" + str(sorted(set(func.sanitize(t) for t in sarah))[0:3]))

# (2)用dictionary实现，让数据项彼此联系
# sarah_data = {
# 	'name' : sarah.pop(0),
# 	'dob' : sarah.pop(0),
# 	'times' : sarah
# }
# print(sarah_data['name'] + "'s fastest times are " +
# str(sorted(set(func.sanitize(t) for t in sarah_data['times']))[0:3]))

# (3)将（2）的功能写入函数get_coach_data
print(sarah['name'] + "'s fastest times are " + str(sarah['times'][0:3]))
print(julie['name'] + "'s fastest times are " + str(julie['times'][0:3]))
print(mikey['name'] + "'s fastest times are " + str(mikey['times'][0:3]))
print(james['name'] + "'s fastest times are " + str(james['times'][0:3]))
