class Student:
    def __init__(self, name):
        # __name -> GraduateStudent에서 사용 못함
        self.name = name

    def __str__(self):
        return '이름: {}'.format(self.name)


class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def __str__(self):
        super().__str__()
        return '이름: {}, 전공: {}'.format(self.name, self.major)


std = Student('홍길동')
print(std)

g_std = GraduateStudent('이순신', '컴퓨터')
print(g_std)
