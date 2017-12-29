import func

sarah = func.get_coach_data("ch6_data/sarah2.txt")

# dob:date of birthday
# 用普通列表实现，缺点是当数据量变大时，需要设置过多变量名称。

# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are:" + str(sorted(set(func.sanitize(t) for t in sarah))[0:3]))
