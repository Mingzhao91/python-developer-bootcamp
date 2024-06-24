class Car:

    def __init__(self, make, model, year, tires, color):
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires
        self.color = color

    def start_car(self):
        print('car starting....')


my_car = Car('Toyota', 'Camry', 2020, 4, 'black')


class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    # getter
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print('Error, insufficient funds')
        else:
            self._balance -= amount
        return amount


tuomas_account = BankAccount('Tuomas', 1000)
tuomas_account.deposit(2000)
print(tuomas_account._balance)
tuomas_account.withdraw(1500)
print(tuomas_account._balance)


class Employee:
    def __init__(self, name, birth_date):
        self._name = name
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()


class Circle:

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2


circle1 = Circle(2)
print(circle1.diameter)


class Person:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value:
            self._first_name = value
        else:
            raise ValueError('First name cannot be empty')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value:
            self._last_name = value
        else:
            raise ValueError('Last name cannot be empty')

    def introduce(self):
        print(f"Hello, my name is {self._first_name} {self._last_name}")


class Employee(Person):

    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    def introduce(self):
        print(f"Hello, my name is {self._first_name} {self._last_name} and my employee ID is {self.employee_id}")


person1 = Person('fda#', 'fdas')
person1.first_name = 'Abc'
person1.last_name = 'Def'
print(person1.first_name)
print(person1.last_name)


class Shape:

    def __init__(self, color):
        self.color = color

    def description(self):
        print(f"This shape is {self.color}")


class Square(Shape):

    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def description(self):
        print(f"This shape is {self.color} and has a side length of {self.side_length}")


class Vehicle:

    def __init__(self, wheels):
        self.wheels = wheels

    def drive(self):
        print("The vehicle is driving")


class CarX(Vehicle):

    def __init__(self):
        super().__init__(wheels=4)

    def drive(self, speed=None):
        if speed:
            print(f"The car is driving at {speed} mph.")
        else:
            super().drive()


carX1 = CarX()
carX1.drive()


class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Width must be a positive number')

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError('Height must be a positive number')

    @property
    def area(self):
        return self._height * self._width


class Square(Rectangle):

    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def perimeter(self):
        return self.width * 4


class BankAccount:

    def __init__(self, account_number, initial_balance):
        self._account_number = account_number
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @property
    def is_overdrawn(self):
        return self._balance < 0

    def __str__(self):
        return f"Account Number: {self._account_number} | Balance: {self.balance}"


bc = BankAccount('12345', 100)
bc.withdraw(900)
print(bc.is_overdrawn)
print(str(bc))

class Car:
    def __init__(self, make, model, year, tires):
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires

    def start_engine(self):
        print(f"The {self.make} {self.model} {self.year} engine starts.")


class Tesla(Car):
    def __init__(self, make, model, year, tires, battery_life):
        super().__init__(make, model, year, tires)
        self.battery_life = battery_life

    def start_engine(self):
        print(f"The {self.make} {self.model} {self.year} {self.battery_life} engine starts.")

    def charge_battery(self):
        print("Charging.......")


"""
@staitcmethod
"""
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y


result = MathUtils.add(3, 5)
print(result)

"""
@classmethod
"""
class EmployeeX:
    _employee_count = 0

    def __init__(self, name, salary):
       self.name = name
       self.salary = salary
       EmployeeX._employee_count += 1

    @classmethod
    def employee_count(cls):
        return cls._employee_count

    @classmethod
    def from_string(cls, employee_string):
        name, salary = employee_string.split(',')
        return cls(name.strip(), salary.strip())


employee1 = EmployeeX('Alice', 50000)
employee2 = EmployeeX('Bob', 50000)
employee3 = EmployeeX.from_string('Charlie, 55000')
print(EmployeeX.employee_count())