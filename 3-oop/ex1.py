class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"My name is {self.name}, I'm {self.age} years old, and I'm {self.gender}.")


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre


class Student:
    def __init__(self, name, age, major, GPA):
        self.name = name
        self.age = age
        self.major = major
        self.GPA = GPA

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_major(self):
        return self.major

    def get_GPA(self):
        return self.GPA

    def calculate_grade(self):
        if self.GPA >= 4.0:
            return "A+"
        elif self.GPA >= 3.7:
            return "A"
        elif self.GPA >= 3.3:
            return "B+"
        elif self.GPA >= 3.0:
            return "B"
        elif self.GPA >= 2.7:
            return "C+"
        elif self.GPA >= 2.3:
            return "C"
        elif self.GPA >= 2.0:
            return "D"
        else:
            return "F"


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def eat(self, food):
        print(f"{self.name} is eating {food}...")

    def sleep(self):
        print(f"{self.name} is sleeping...")