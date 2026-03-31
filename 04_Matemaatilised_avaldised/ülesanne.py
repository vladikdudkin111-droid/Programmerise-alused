"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Initialize a Person with default values."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Initialize a Student with given firstname, lastname and age."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # Empty usage
    empty_obj = Empty()

    # 3 x Person usage
    person1 = Person()
    person1.firstname = "Alice"
    person1.lastname = "Smith"
    person1.age = 30

    person2 = Person()
    person2.firstname = "Bob"
    person2.lastname = "Johnson"
    person2.age = 25

    person3 = Person()
    person3.firstname = "Charlie"
    person3.lastname = "Brown"
    person3.age = 40

    # 3 x Student usage
    student1 = Student("David", "Miller", 20)
    student2 = Student("Eva", "Davis", 22)
    student3 = Student("Frank", "Wilson", 21)

    # Näidisprintimiseks (valikuline)
    print(f"{person1.firstname} {person1.lastname}, age {person1.age}")
    print(f"{student1.firstname} {student1.lastname}, age {student1.age}")