# Simple Calculator
# A string consisting of Numbers and Basic Mathematical Operators
# No parenthesis
# calc("3 + 7 + 2 + 9") -> 21

# Parsing String -> Meaningful Object
# Handling Operator Precedence
# Compute Results

# Start with the simplest problem
# 2 operands, both digit(0..9), and only plus operator
def simplest_calc1(operation): # a+b "3+7","7+9"
    # Parsing
    a = int(operation[0])
    b = int(operation[2])
    # Handling Operator Precedence
    # Compute Results
    return a + b

# print(simplest_calc1("3+7"))
# print(simplest_calc1("7+9"))
# print(simplest_calc1("7+99"))  -> False

# 2 operands, both integers(-inf, +inf), and only plus operator
def simplest_calc2(operation): # a+b "33+71","75+93"
    # Parsing
    operands = operation.split("+")
    a = int(operands[0])
    b = int(operands[1])
    # Handling Operator Precedence
    # Compute Results
    return a + b

# print(simplest_calc2("33+71"))
# print(simplest_calc2("75+93"))

# 2 operands, both integers(-inf, +inf), and all for operators
def simplest_calc3(operation): # a+b "33+71","75*93"
    # Parsing
    # Handling Operator Precedence
    # Compute Results
    operands = operation.split("+")
    if len(operands) > 1:
        a = int(operands[0])
        b = int(operands[1])
        return a + b

    operands = operation.split("*")
    if len(operands) > 1:
        a = int(operands[0])
        b = int(operands[1])
        return a * b

    operands = operation.split("-")
    if len(operands) > 1:
        a = int(operands[0])
        b = int(operands[1])
        return a - b

    operands = operation.split("/")
    if len(operands) > 1:
        a = int(operands[0])
        b = int(operands[1])
        return a / b


# print(simplest_calc3("50*100"))
# print(simplest_calc3("75+93"))

# n operands, all integers(-inf, +inf), and only plus operator
def simplest_calc4(operation):  # "3+77+11+45"
    operands = operation.split("+")
    result = 0
    for operand in operands:
        result = result + int(operand)

    return result


# print(simplest_calc4("50+100+3+8"))
# print(simplest_calc4("75+93+11"))

# AST(Abstract Syntax Tree)
# Precedence( / * - + )
# Tree -> (Node [Tree] | Node)
#                   1
#               /   |   \
#               2   3   4
#                   |   |
#                   5   6
# Tree(a)
# a (1 [(2), (3 [(5)]), (4 [(6)])])
#                  +
#               /     \
#              75      +
#                    /   \
#                   93   11
# AST(a) (Node AST AST | Node)
class AST:
    def __init__(self, value, leftAST = None, rightAST = None):
        self.value = value
        self.left = leftAST
        self.right = rightAST

    def compute(self):
        if self.value.node_type == 'operation':
            return self.compute_as_operation()
        else:
            return self.value.val

    def compute_as_operation(self):
        if self.value == '+':
            return self.left.compute() + self.right.compute()
        if self.value == '-':
            return self.left.compute() - self.right.compute()
        if self.value == '*':
            return self.left.compute() * self.right.compute()
        if self.value == '/':
            return self.left.compute() / self.right.compute()




class ASTNode:
    def __init__(self, value):  # value = "+"
        self.node_type = self.get_type(value)
        self.val = self.get_val(value)

    def get_type(self, value):
        operation_list = ['+', '-', '*', '/']
        if value in operation_list:
            return 'operation'
        else:
            return 'operand'

    def get_val(self, value):
        if self.node_type == 'operation':
            return value
        else:
            return int(value)

print(AST(ASTNode("+"), AST("63"), AST("79")).compute())
# AST(ASTNode("+"), AST("63"), AST("79"))
# 63 + 79
# plus = ASTNode("+")
# print(plus.node_type)
# print(plus.val)
#
# thirtytwo = ASTNode("32")
# print(thirtytwo.node_type)
# print(thirtytwo.val)




#                  +
#               /     \
#              75      +
#                    /   \
#                   93   11

# AST(
#     ASTNode('+')
#     (AST(
#       ASTNode('75')
#       None
#       None)
#     )
#     (AST(
#       ASTNode('+')
#       (AST(
#           ASTNode('93')
#           None
#           None)
#       )
#       (AST(
#           ASTNode('11')
#           None
#           None)
#       )
#       ))  )


# School System
# Courses
# - Department
# - Code
# - Lecturer
# Departments
# - Teachers
# Teacher
# - Name
# - Title
# - Experience
# Title
# (Dr. | Asst. Prof | Assoc. Prof | Prof)
# Students
# - EnrolledCourses
# - Name
# - Advisor(Teacher)
# - StudentNumber

# Given a course name, give the enrolled student list
