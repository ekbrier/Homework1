"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random


class CFGStudent:

    def __init__(self, name, surname, age, email, student_id=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id

    @staticmethod
    def generate_id():
        return str(random.randrange(1000, 10000))

    def get_id(self):
        return self.generate_id()

    def get_fullname(self):
        return f"{self.name} {self.surname}"


class NanoStudent(CFGStudent):

    def __init__(self, degree, name, surname, age, email, student_id=None):
        super().__init__(degree, name, surname, age, email, student_id=None)
        self.specialization = degree
        self.course_grades = dict()

    @staticmethod
    def generate_id():
        return 'nano' + super().generate_id()

    def add_new_grade(self, assignment, grade):
        self.course_grade[assignment] = grade

    def get_course_grades(self):
        return self.course_grades


example_s = CFGStudent('Ellie', 'Brierley', 22, 'elliebrierley@exam.com')
print(example_s.generate_id())
print(example_s.get_fullname())


"""TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_even_fibonacci(limit):
    indexes = [x for x in range(10)]
    print(indexes)

    even_fibonacci_numbers = [fibonacci(i) for i in indexes if fibonacci(i) % 2 == 0]
    print('Even Fibonacci values within the limit are:', even_fibonacci_numbers)

    return 'Sum of the even numbers and the final result:', sum(even_fibonacci_numbers)


print(sum_of_even_fibonacci(limit=10))

"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""


def is_valid_subsequence(array, sequence):
    seqIdx = 0
    for num in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == num:
            seqIdx += 1
    return seqIdx == len(sequence)


array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, -2]

print(is_valid_subsequence(array1, sequence1)) #FALSE (WORKS)

array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [1, 6, -1, 10]

print(is_valid_subsequence(array2, sequence2)) #TRUE

array3 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3)) #TRUE

"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""
"""ANSWER: Whilst the code is somewhat well written, 
there are a lot of functions within the class "Employee" and I think it would
be beneficial to use the inheritance technique to divide it into a parent
class, which in this case would be Employee and then a child class to perform
the functions of adding and removing employees from the database engine and so that it inherits all the methods and properties from the parent class."""