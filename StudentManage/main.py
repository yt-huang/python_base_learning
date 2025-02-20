from po.Student import Student
if __name__ == '__main__':
    count = 0
    students = []
    while True:
        print("""
        1、录入学生信息
        2、查找学生信息
        3、删除学生信息
        4、修改学生信息
        5、排序
        6、统计学生总人数
        7、显示所有学生信息
        0、退出系统""")
        try:
            num = int(input("请输出菜单项0-7的数字： "))
            if num == 0:
                print("已经安全退出系统")
                break
            elif num ==1:
                flag = True
                print("录入学生信息")
                name = input("请输入学生的姓名")
                for s in students:
                    if s.name == name:
                        print("学生已存在")
                        flag = False
                        break
                if not flag:
                    continue
                age = int(input("请输入学生的年龄"))
                java = int(input("请输入学生的java成绩"))
                python = int(input("请输入学生的python成绩"))
                c = int(input("请输入学生的c成绩"))
                student = Student(name, age, java, python, c)
                students.append(student)
                continue
            elif num ==2:
                print("查找学生信息")
                student_name = input("请输入学生姓名")
                for s in students:
                    if s.name == student_name:
                        s.printStudentInfo()
                        break
                    else:
                        print("没有这个学生")
                continue
            elif num ==3:
                print("删除学生信息")
                student_name = input("请输入学生姓名")
                for s in students:
                    if s.name == student_name:
                        students.remove(s)
                        break
                    else:
                        print("没有这个学生")
                continue
            elif num ==4:
                print("修改学生信息")
                student_name = input("请输入学生姓名")
                for s in students:
                    if s.name == student_name:
                        s.SetScore(java=int(input("请输入新的java成绩")), python=int(input("请输入新的python成绩")), c=int(input("请输入新的c成绩")))
                        print("修改后的学生信息如下")
                        s.printStudentInfo()
                continue
            elif num ==5:
                sort_students = []
                print("选择名字年龄各科的成绩排序")
                num = int(input("请分别输入0-4 分别表示名字 年龄 java python c的排序方式"))
                if num == 0:
                    sort_students = sorted(students, key=lambda x: x.name)
                if num == 1:
                    sort_students = sorted(students, key=lambda x: x.age)
                if num == 2:
                    sort_students = sorted(students, key=lambda x: x.java)
                if num == 3:
                    sort_students = sorted(students, key=lambda x: x.python)
                if num ==4:
                    sort_students = sorted(students, key=lambda x: x.c)
                print("排序后的数据：")
                print("姓名\t年龄\tjava\tpython\tc")
                for s in sort_students:
                    s.printStudentInfo()
            elif num ==6:
                print("学生总人数为：", len(students))
            elif num ==7:
                print("显示所有学生信息")
                print("姓名\t年龄\tjava\tpython\tc")
                for s in students:
                    s.printStudentInfo()
                continue
            else:
                print("请输入正确的菜单项")
        except ValueError:
            print("请输出数字 0-7")
        count = count + 1
        if count == 5:
            print("输入错误次数过多，系统退出")
            exit()