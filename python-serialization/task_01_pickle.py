import pickle
import os

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nis_student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self,f)
        except Exception as ex:
            print(f"Error during serialization: {ex}")

    @classmethod
    def deserialize(cls, filename):
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            raise ValueError("File is not exists or empty")
        with open(filename, "rb") as file:
            try:
                return pickle.load(file)
            except EOFError:
                raise ValueError("File is empty or corrupt")
                return None
