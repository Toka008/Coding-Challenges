class Student():
    def __init__(self, name):
        self.name = name
        self.attend = 0
        self.marks = []
        print('Welcome to portal {}!!!'.format(name))

    def addmarks(self, mark):
        self.marks.append(mark)

    def attenddays(self):
        self.attend += 1

    def getavg(self):
        return sum(self.marks) / len(self.marks)


s = Student("John")
print(s.marks)
print(s.attend)
s.addmarks(100)
s.addmarks(100)
s.addmarks(95)
s.addmarks(97)
s.addmarks(87)
print(s.marks)
s.attenddays()
print(s.attend)
s.attenddays()
print(s.attend)
print(s.getavg())

