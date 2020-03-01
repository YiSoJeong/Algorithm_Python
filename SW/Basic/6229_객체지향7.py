class Person:
    def __init__(self):
        self.gender = 'Unknown'

    def getGender(self):
        return self.gender


class Male(Person):
    def __init__(self):
        self.gender = 'Male'

    def getGender(self):
        return self.gender


class Female(Person):
    def __init__(self):
        self.gender = 'Female'

    def getGender(self):
        return self.gender


male = Male()
female = Female()

print(male.getGender())
print(female.getGender())
