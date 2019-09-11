class Human:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def present(self):
        print("{0}:{1} cm".format(self.name,self.size))

class Worker(Human):
    def __init__(self, name, size, job):
        super().__init__(name, size)
        self.job = job

    def present(self):
        super().present()
        print(self.job)
class Engineer(Worker):
    def __init__(self, name, size, job, skill):
        super().__init__(name, size, job)
        self.skill = skill

w = Worker("Bob", 185, "trader")
w.present()

e = Engineer("Tim", 170, "Programmer", "Python")
e.present()
