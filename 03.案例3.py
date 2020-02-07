# 定义一个人类，包括属性：姓名、性别、年龄(age)、国籍；
# 包括方法：吃饭、睡觉，工作(work)。
# （1）根据人类，派生一个学生类，增加属性：学校、学号；重写工作方法（学生的工作是学习(study)）。
# （2）根据人类，派生一个工人类，增加属性：单位、工龄；重写工作方法（工人的工作是）。
# （3）根据学生类，派生一个学生干部类，增加属性：职务；增加方法：开会。
# （4）编写主函数分别对上述3类具体人物进行测试。
class Person(object):
    def __init__(self, name, sex, age, country):
        self.name = name
        self.sex = sex
        self.age = age
        self.country = country

    def eat(self):
        print("会吃饭")

    def sleep(self):
        print("回睡觉")

    def work(self):
        print("会工作")


# 1）根据人类，派生一个学生类，增加属性：学校、学号；重写工作方法（学生的工作是学习(study)）
class Student(Person):
    def __init__(self, name, sex, age, country, school, no):
        self.school = school
        self.no = no
        Person.__init__(self, name, sex, age, country)

    def study(self):
        print("会学习")

s1 = Student("小明", "男", 12, "中国", "大学", "001")
print(s1.name)
print(s1.sex)
print(s1.age)
print(s1.country)
print(s1.school)
print(s1.no)
s1.study()

# （3）根据学生类，派生一个学生干部类，增加属性：职务；增加方法：开会。
class Student_work(Student):
    def __init__(self, name, sex, age, country, school, no, zhiwu):
        self.zhiwu = zhiwu
        super().__init__(name, sex, age, country, school, no)

    def meeting(self):
        print("开会")

sw = Student_work("小明", "男", 12, "中国", "大学", "001", "职工")
print(sw.name, sw.sex, sw.age, sw.country, sw.school, sw.no, sw.zhiwu)
sw.study()
sw.meeting()