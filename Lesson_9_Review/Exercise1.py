# def func():
#     pass
#
# print(type(func))
# print(type(3))
#
# l = list("hello")
# print(l)
# print(type(l))
#
# s = "-".join(l)
# print(s)
#
# print(dir(""))
# print(dir(list))

class Human:
    gender = "Unknown"

    def __init__(haha, name):
        haha.name = name

    def sing(hoho):
        print(hoho.name, "is singing")

    @classmethod
    def showGender(cls):
        print(cls.gender)

    @staticmethod
    def doMath(a, b):
        print(a + b)


khang = Human("Khang")
dung = Human("Dung")
dung.handsome = True
print(dung.handsome)

print(khang.gender)
print(dung.gender)
print(Human.gender)
# print(Human.name)
khang.gender = "Male"
dung.gender = "Male"
print(khang.gender)
print(dung.gender)

dung.sing()
# Human.sing()

dung.showGender()
Human.showGender()
Human.gender = "Invalid"
dung.showGender()
Human.showGender()

Human.doMath(1, 2)
dung.doMath(3, 4)
khang.doMath(5, 6)
