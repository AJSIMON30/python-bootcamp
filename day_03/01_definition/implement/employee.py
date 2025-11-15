class Employee:
    def __init__(self,name, id):
        self.var1 = name
        self.var2 = id
        self.var3 = []
        print(f"Employee {name} created with {id}")

    def work(self,task):
        print(f"{self.var1} is doing the {task}")
        self.var3.append(task)

employee1 = Employee("AJ", "123")


employee2 = Employee("Aeros", "456")


employee3 = Employee("Aeden", "789")

employee1.work("report")
employee2.work("analysis")
employee3.work("sustaining")