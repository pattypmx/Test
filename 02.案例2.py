"""
一共有10名老师
老师 分别有  名字 年龄 性别 这些特征
罗元, 王梦涵、刘子怡、孙长胜、张成基 张志远、徐广来、张一山、王海, 陈阳
22, 26, 21, 26, 27, 33, 29, 44, 29, 31
"男", "女", "女", "男", "男", "男", "男", "男", "男", "男"
把这些老师保存到列表中
"""

# 定义一个输出类
class Person(object):
    # 定义需要输出的属性
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    # 输出结果
    def __str__(self):
        return "姓名:%s 年龄:%s 性别:%s" %(self.name, self.age, self.sex)

# 定义一个存放结果类
class Teacher(object):
    # 将列表定义属性
    def __init__(self):
        self.__name_list = ["罗元", "王梦涵", "刘子怡", "孙长胜", "张成基", "张志远", "徐广来", "张一山", "王海", "陈阳"]
        self.__age_list = [22, 26, 21, 26, 27, 33, 29, 44, 29, 31]
        self.__sex_list = ["男", "女", "女", "男", "男", "男", "男", "男", "男", "男"]

    def get_teacher_list(self):

        # 定义一个变量，用来保存老师对象
        teacher_list = []

        # 通过变量循环从列表中获取老师的名字 年龄 性别
        # enumerate可获取到下标i及对应的元素
        for i, name in enumerate(self.__name_list):
            # 定义变量保存老师的名字 年龄 性别值
            my_name = name
            my_age = self.__age_list[i]
            my_sex = self.__sex_list[i]

            # 将得到的数据存入输出类中
            p = Person(my_name, my_age, my_sex)
            # print(p)
            # 将得到的数据添加到list中
            teacher_list.append(p)
        # 返回list值
        return teacher_list

t = Teacher()
# print(t.get_teacher_list())-----[<__main__.Person object at 0x101c295e0>....
teacher_list = t.get_teacher_list()
for teacher in teacher_list:
    print(teacher)
