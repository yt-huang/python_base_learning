class Student:
    def __init__(self, name, age, java, python, c):
        self.name = name
        self.age = age
        self.java = java
        self.python = python
        self.c = c
    def __str__(self):
        return "Student(name=%s, age=%d, java=%d, python=%d, c=%d)" % (self.name, self.age, self.java, self.python, self.c)
    def SetScore(self, **kwargs): # 通过**kwargs接收任意参数设置java python c的值
        for key, value in kwargs.items():
            if key == "java":
                self.java = value
            elif key == "python":
                self.python = value
            elif key == "c":
                self.c = value
    def printStudentInfo(self):
        print("%s\t%d\t\t%d\t\t%d\t\t%d" % (self.name, self.age, self.java, self.python, self.c))
if __name__ == '__main__':
    s1 = Student("张三", 18, 90, 80, 70)
    s1.printStudentInfo()
