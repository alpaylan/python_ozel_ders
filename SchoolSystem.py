class College:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_departments(self, departments):
        self.departments = self.departments + departments

    def enroll_student(self, student, department):
        s_dep = None
        for dep in self.departments:
            if dep == department:
                s_dep = dep

        if s_dep is None:
            raise Exception("department not found")

        term_dict = {
            1: 'freshman',
            2: 'sophomore',
            3: 'junior',
            4: 'senior'
        }
        department.terms[term_dict[student.grade]].students.append(student)
class Term:
    def __init__(self):
        self.must_courses = []
        self.elective_courses = []
        self.students = []

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.terms = {
        "freshman" : Term(),
        "sophomore" : Term(),
        "junior" : Term(),
        "senior" : Term(),
        }
        self.abbreviation = str.upper(name.split(' ')[0][0] + name.split(' ')[-1][0:3])

class Course:
    code = {
        'freshman': 0,
        'sophomore': 0,
        'junior': 0,
        'senior': 0,
    }
    def __init__(self, name, department, instructor, term):
        self.name = name
        self.department = department
        self.code = self.generate_code(term)
        self.instructor = instructor
        self.enrolled_students = []

    def generate_code(self, term):
        term_dict = {
            1: 'freshman',
            2: 'sophomore',
            3: 'junior',
            4: 'senior',
        }
        Course.code[term_dict[term]] += 1
        return str(self.department.code) + str(term) + str(Course.code[term_dict[term]])

    def add_student(self, student):
        self.enrolled_students.append(student)

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Instructor(Person):
    def __init__(self, name, age, gender, title):
        super().__init__(name, age, gender)
        self.title = title

class Student(Person):
    sid = 0
    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.student_id = Student.sid
        Student.sid = Student.sid + 1
        self.grade = grade




if __name__ == "__main__":
    alp = Student("Alp", 21, 'male', 4)
    gokturk = Instructor("Gokturk", 62, 'male', 'Professor')
    ceng = Department('Computer Engineering', 571)
    eee = Department('Electrics and Electronics Engineering', 562)
    # print(ceng.abbreviation)
    # print(eee.abbreviation)
    ceng424 = Course('Logic for CS', ceng, gokturk, 4)
    ceng350 = Course('Software Engineering', ceng, gokturk, 3)
    ceng351 = Course('Databases', ceng, gokturk, 3)
    print(ceng424.code)
    print(ceng350.code)
    print(ceng351.code)
    metu = College('Middle East Technical University')
    metu.add_departments([ceng, eee])
    # mete = Department('Materials Engineering', 537)
    metu.enroll_student(alp, ceng)




"""
METU
    CENG
        CENG424
            Gokturk
            5711
            CENG
    EEE
"""
