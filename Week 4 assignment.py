class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Your name is", self.name, ", Age:", self.age, "years, Gender:", self.gender)

firstPerson = Person("Neville", 13, "Male")
firstPerson.introduce()