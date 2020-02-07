"""
定义一个学生类。
有下面的对象属性：姓名,年龄,成绩（语文，数学，英语)[每课成绩的类型为整数]
对象方法：
获取学生的姓名：get_name() 返回类型:str;
获取学生的年龄：get_age() 返回类型:int;
返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:xm = Student('zhangming',22,[88,64,99])
返回结果：
小明
22
99
"""
# 01：
# class Student(object):
#     def __init__(self, name, age, score_list):
#         self.name = name
#         self.age = age
#         self.score_list = score_list
#
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#
#     def get_max(self):
#         my_max = max(self.score_list)
#         return my_max
#
# xm = Student('小明', 22, [88,64,99])
# print(xm.get_name())
# print(xm.get_age())
# print(xm.get_max())

# 02：
# class Student(object):
#     def __init__(self, name, age, score_list):
#         self.__name = name
#         self.__age = age
#         self.__score_list = score_list
#     # 获取学生的姓名
#     def __get_name(self):
#         return self.__name
#     # 获取学生的年龄
#     def __get_age(self):
#         return self.__age
#     # 返回3门科目中最高的分数
#     def __get_max(self):
#         return max(self.__score_list)
#
#     # 私有化之后，不能通过对象输出，只能在类中输出
#     def print_info(self):
#         print(self.__get_name())
#         print(self.__get_age())
#         print(self.__get_max())
#
# xm = Student('小明', 22, [88,64,99])
# xm.print_info()

# 03：
class Student(object):
    def __init__(self, name, age, score_list):
        self.__name = name
        self.__age = age
        self.__score_list = score_list

    # 获取学生的姓名
    def __get_name(self):
        return self.__name
    # 获取学生的年龄
    def __get_age(self):
        return self.__age
    # 返回3门科目中最高的分数
    def __get_max(self):
        return max(self.__score_list)
    # 私有化之后，不能通过对象输出，只能在类中输出
    def print_info(self):
        # 输出元组--('小明', 22, 99)
        return self.__get_name(), self.__get_age(), self.__get_max()
xm = Student('小明', 22, [88,64,99])
# print(xm.print_info())--('小明', 22, 99)
# 通过拆包分解
xm.name, xm.age, xm.score = xm.print_info()
print(xm.name)
print(xm.age)
print(xm.score)
