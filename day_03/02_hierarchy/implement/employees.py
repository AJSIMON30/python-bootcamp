class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)

class Recruiter(Employee):
    def recruit(self):
       return super().add_work()

class Developer(Employee):
    def code(self):
        return super().add_work()

class Manager(Employee):
    def manage(self):
        return super().add_work()

# Names1 = Employee("Aeros","223042")
# Names2 = Employee("Aeden", "223043")
# Names3 = Employee("AJ","223044")
#
# Names1.add_work("recruiting")
# Names2.add_work("Developing")
# Names3.add_work("Managing")

recruit = Recruiter("Aeros","223042")
recruit.recruit()

develop = Developer("Aeden", "223043")
develop.code()

manage = Manager("AJ","223044")
manage.manage()

