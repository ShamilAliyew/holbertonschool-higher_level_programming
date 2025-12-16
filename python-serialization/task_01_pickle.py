import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        return f"Name: {self.name}\nAge: {self.age}\nis_student: {self.is_student}"

    def serialize(self, filename):
        with open(filename, "w") as file:
            pickle.dump(self, file)

    @classmethod
    def deserilize(cls, filename):
        with open(filename, "r") as file:
            return pickle.load(file)
