class Stu:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age

    def __repr__(self):
        return "<Stu name:{} age:{}>".format(self.name, self.age)

    __str__ = __repr__

print(Stu("xm", "18"))