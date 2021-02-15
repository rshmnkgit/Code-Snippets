class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avgscore = sum(self.scores) / len(self.scores)
        if (avgscore>=90 and avgscore<=100):
            grade = 'O'
        elif (avgscore>=80 and avgscore<90):
            grade = 'E'
        elif (avgscore>=70 and avgscore<80):
            grade = 'A'
        elif (avgscore>=55 and avgscore<70):
            grade = 'P'
        elif (avgscore>=40 and avgscore<55):
            grade = 'D'
        else:
            grade = 'T'
        return grade                                
            




line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())