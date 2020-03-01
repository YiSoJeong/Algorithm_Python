class Student:
    def __init__(self, kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    def total(self):
        print('국어, 영어, 수학의 총점: {}'.format(self.__kor + self.__eng + self.__math))


a = list(map(int, input().split(', ')))

std = Student(a[0], a[1], a[2])
std.total()
