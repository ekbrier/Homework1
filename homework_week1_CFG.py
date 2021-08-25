#TASK 2

class Student:
    def __init__(self, name, nickname, age, unique_id):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.unique_id = unique_id
        self.modules = dict()


class CFGStudent(Student):

    def __init__(self, name, nickname, age, unique_id, specialisation):
        super().__init__(name, nickname, age, unique_id)
        self.average_mark = sum(self.modules.values()) / len(self.modules)
        self.modules = None
        self.overall_mark = 0
        self.specialisation = specialisation

    def add_module(self, module, grade):
        self.modules[module] = grade

    def remove_module(self, module):
        del self.modules[module]

    def view_subject(self):
        print(self.modules)

    def average_mark(self):
        print(self.overall_mark)

    def view_module(self):
        pass


student1 = CFGStudent('Eleanor', 'Ellie', 22, 10273889, 'Software')
student1.add_module('Homework', 80)
student1.add_module('Theory 1', 100)
student1.add_module('Exam 1', 62)
student1.remove_module('Homework')
student1.view_module()
student1.average_mark()

student2 = CFGStudent('Katherine', 'Kat', 22, 10137499, 'Covid_scientist')
student2.add_module('Homework', 90)
student2.add_module('Theory 1', 58)
student2.add_module('Exam 1', 69)
student2.remove_module('Theory 1')
student2.view_module()
student2.average_mark()