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

        if student.grade == 1:
            department.freshman.students.append(student)
        elif student.grade == 2:
            department.sophomore.students.append(student)
        elif student.grade == 3:
            department.junior.students.append(student)
        elif student.grade == 4:
            department.senior.students.append(student)

        # term_dict = {
        #     1: 'freshman',
        #     2: 'sophomore',
        #     3: 'junior',
        #     4: 'senior'
        # }
        # department.terms[term_dict[student.grade]].students.append(student)
    def find_student(self, student):
        for department in self.departments:
            if student in department.freshman.students:
                return (department, 'freshman')
            if student in department.sophomore.students:
                return (department, 'sophomore')
            if student in department.junior.students:
                return (department, 'junior')
            if student in department.senior.students:
                return (department, 'senior')

        return None

    def enrolled_course(self, student):
        (department, term) = self.find_student(student)
        print(f"EnrolledCourse {department.name} {term}\n", end="")

        enrolled_courses = []
        if term == 'freshman':
            for course in department.freshman.must_courses:
                if student in course.enrolled_students:
                    enrolled_courses.append(course)
            for course in department.freshman.elective_courses:
                if student in course.enrolled_students:
                    enrolled_courses.append(course)
        if term == 'sophomore':
            for course in department.sophomore.must_courses:
                if student in course.enrolled_students:
                    enrolled_courses.append(course)
            for course in department.sophomore.elective_courses:
                if student in course.enrolled_students:
                    enrolled_courses.append(course)
        if term == 'junior':
            for course in department.junior.must_courses:
                print(f"TermJunior {course.name}")
                if student in course.enrolled_students:
                    enrolled_courses.append(course.name)
            for course in department.junior.elective_courses:
                print(f"TermJunior {course.name}")
                if student in course.enrolled_students:
                    enrolled_courses.append(course.name)
        if term == 'senior':
            for course in department.senior.must_courses:
                if student in course.enrolled_students:
                    enrolled_courses.append(course.name)
            for course in department.senior.elective_courses:
                if student in course.enrolled_students:
                    enrolled_courses.append(course.name)

        return enrolled_courses

class Term:
    def __init__(self):
        self.must_courses = []
        self.elective_courses = []
        self.students = []

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

        self.freshman = Term()
        self.sophomore = Term()
        self.junior = Term()
        self.senior = Term()

        self.abbreviation = str.upper(name.split(' ')[0][0] + name.split(' ')[-1][0:3])
    def add_course(self, course):
        if course.term == 1:
            if course.course_type == 'must':
                self.freshman.must_courses.append(course)
            else:
                self.freshman.elective_courses.append(course)
        if course.term == 2:
            if course.course_type == 'must':
                self.sophomore.must_courses.append(course)
            else:
                self.sophomore.elective_courses.append(course)
        if course.term == 3:
            if course.course_type == 'must':
                self.junior.must_courses.append(course)
            else:
                self.junior.elective_courses.append(course)
        if course.term == 4:
            if course.course_type == 'must':
                self.senior.must_courses.append(course)
            else:
                self.senior.elective_courses.append(course)

class Course:
    freshman = 0
    sophomore = 0
    junior = 0
    senior = 0
    def __init__(self, name, department, instructor, term, course_type):
        self.name = name
        self.department = department
        self.code = self.generate_code(term)
        self.term = term
        self.instructor = instructor
        self.enrolled_students = []
        self.course_type = course_type
        department.add_course(self)

    def generate_code(self, term):
        # term_dict = {
        #     1: 'freshman',
        #     2: 'sophomore',
        #     3: 'junior',
        #     4: 'senior',
        # }
        # Course.code[term_dict[term]] += 1

        if term == 1:
            Course.freshman += 1
            course_code = Course.freshman
        elif term == 2:
            Course.sophomore += 1
            course_code = Course.sophomore
        elif term == 3:
            Course.junior += 1
            course_code = Course.junior
        elif term == 4:
            Course.senior += 1
            course_code = Course.senior

        return str(self.department.code) + str(term) + str(course_code)

    def add_student(self, student):
        self.enrolled_students.append(student)

    def does_student_take_course(self, student):
        if student in self.enrolled_students:
            return True
        else:
            return False

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
    alp = Student("Alp", 21, 'male', 3)
    gokturk = Instructor("Gokturk", 62, 'male', 'Professor')
    ceng = Department('Computer Engineering', 571)
    eee = Department('Electrics and Electronics Engineering', 562)
    # print(ceng.abbreviation)
    # print(eee.abbreviation)
    ceng424 = Course('Logic for CS', ceng, gokturk, 4, 'must')
    ceng350 = Course('Software Engineering', ceng, gokturk, 3, 'must')
    ceng351 = Course('Databases', ceng, gokturk, 3, 'must')
    print(ceng424.code)
    print(ceng350.code)
    print(ceng351.code)
    metu = College('Middle East Technical University')
    metu.add_departments([ceng, eee])
    # mete = Department('Materials Engineering', 537)
    metu.enroll_student(alp, ceng)
    ceng350.add_student(alp)
    ceng351.add_student(alp)
    print(metu.enrolled_course(alp))


"""
METU
    CENG
        CENG424
            Gokturk
            5711
            CENG
    EEE
"""
