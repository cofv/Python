

class student:
    def __init__(self, f_name, l_name, age, gender):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender

class teacher:
    def __init__(self, f_name, l_name, age, gender):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender

class group:
    def __init__(self, subject, teachers, students[]):
        self.subject = subject
        self.teachers = teachers
        self.students = students

choice = []
choice.append(student)
choice.append(teacher)
choice.append(group)

print("välj Student, lärare eller grupp(1,2,3)")

for i in range(len(choice)):
    print(i, choice[i].name)



"""
int(input("student=1, lärare=2, grupp=3 "))
    if = 1:
        print("Du har valt att skriva in en student")
        input("Vad är hens förstanamn? ") 
        input("vad är hens efternamn? ")
        input("vad är hens ålder? ")
        input("Vad är hens kön? ")
    if = 2:
        print("Du har valt att skriva in en lärare")
        input("Vad är hens förstanamn? ")
        input("vad är hens efternamn? ")
        input("vad är hens ålder? ")
        input("Vad är hens kön? ")
    elif
"""