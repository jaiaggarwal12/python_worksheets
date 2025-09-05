# 1. Write a Python function to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference.

def diff_from_17(n):
    # compute absolute difference
    if n >= 17:
        d = n - 17
    else:
        d = 17 - n
    if n > 17:
        return 2 * d
    else:
        return d

print("Q1 Examples:")
print("diff_from_17(22) ->", diff_from_17(22))  # expected 10
print("diff_from_17(10) ->", diff_from_17(10))  # expected 7
print("-"*60)

# 2. Write a Python function test_range(n) that returns True if the number is within 100–1000 or 2000, otherwise returns False.

def test_range(n):
    # return True if 100 <= n <= 1000 or n == 2000
    if (n >= 100 and n <= 1000) or (n == 2000):
        return True
    return False

print("Q2 Examples:")
print("test_range(150) ->", test_range(150))
print("test_range(2000) ->", test_range(2000))
print("test_range(50) ->", test_range(50))
print("-"*60)

# 3. Write a Python function to reverse a string. Example: Input = 'robot', Output = 'tobor'.

def reverse_string(s):
    # manual reversal using loop
    res = ""
    i = len(s) - 1
    while i >= 0:
        res += s[i]
        i -= 1
    return res

print("Q3 Examples:")
print("reverse_string('robot') ->", reverse_string("robot"))
print("-"*60)

# 4. Write a Python function that accepts a string and counts the number of uppercase and lowercase letters. Return the counts as a dictionary.

def count_case(s):
    upper = 0
    lower = 0
    i = 0
    while i < len(s):
        ch = s[i]
        # check uppercase by ASCII ranges
        if 'A' <= ch <= 'Z':
            upper += 1
        elif 'a' <= ch <= 'z':
            lower += 1
        i += 1
    return {"uppercase": upper, "lowercase": lower}

print("Q4 Example:")
print("count_case('Hello World!') ->", count_case("Hello World!"))
print("-"*60)

# 5. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def distinct_list(lst):
    res = []
    i = 0
    while i < len(lst):
        val = lst[i]
        # check if val already in res
        found = False
        j = 0
        while j < len(res):
            if res[j] == val:
                found = True
                break
            j += 1
        if not found:
            res.append(val)
        i += 1
    return res

print("Q5 Example:")
print("distinct_list([1,2,2,3,1,4]) ->", distinct_list([1,2,2,3,1,4]))
print("-"*60)

# 6. Write a Python program to return the even numbers from a given list.
# Sample List : [1,2,3,4,5,6,7,8,9] Expected Result : [2,4,6,8]

def evens_from_list(lst):
    ev = []
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            ev.append(lst[i])
        i += 1
    return ev

print("Q6 Example:")
print("evens_from_list([1,2,3,4,5,6,7,8,9]) ->", evens_from_list([1,2,3,4,5,6,7,8,9]))
print("-"*60)

# 7. Write a Python program to define a function inside another function and call it.
# Example: Outer function = robot(), Inner function = move().

def robot():
    def move(direction):
        # simple inner function prints move
        return "Moving " + direction
    # call inner function
    return move("forward")

print("Q7 Example:")
print("robot() ->", robot())
print("-"*60)

# 8. Define a Python function student(name, age, course). Using function attributes, display the names of all arguments.

def student(name, age, course):
    # attach attributes to function to list argument names
    # this is a demonstration: set an attribute 'argnames'
    student.argnames = ["name", "age", "course"]
    # function body can return a tuple
    return {"name": name, "age": age, "course": course}

print("Q8 Example:")
_ = student("Asha", 20, "Mech")
# display argument names stored on function
print("Argument names for student():", getattr(student, "argnames", None))
print("student(...) returns ->", student("Asha", 20, "Mech"))
print("-"*60)

# 9. Write a Python function move_robot(x, y, direction) that takes robot's position and a direction.
# Should return the new position.

def move_robot(x, y, direction):
    if direction == "up":
        return (x, y+1)
    elif direction == "down":
        return (x, y-1)
    elif direction == "left":
        return (x-1, y)
    elif direction == "right":
        return (x+1, y)
    else:
        # unknown direction -> no move
        return (x, y)

print("Q9 Examples:")
print("move_robot(0,0,'up') ->", move_robot(0,0,"up"))
print("move_robot(1,2,'left') ->", move_robot(1,2,"left"))
print("-"*60)

# 10. Write a Python function classify_temperature(temp) that classifies temperature.

def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif temp <= 30:
        return "Moderate"
    else:
        return "Hot"

print("Q10 Examples:")
print("classify_temperature(10) ->", classify_temperature(10))
print("classify_temperature(20) ->", classify_temperature(20))
print("classify_temperature(35) ->", classify_temperature(35))
print("-"*60)

# 11. Write a Python function is_goal_reached(path) where path is a list of moves.
# Return True if final position is (2,0) starting from (0,0)

def is_goal_reached(path):
    x = 0; y = 0
    i = 0
    while i < len(path):
        move = path[i]
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
        # ignore unknown moves
        i += 1
    return (x == 2 and y == 0)

print("Q11 Examples:")
print("is_goal_reached(['up','right','right','down']) ->", is_goal_reached(["up","right","right","down"]))
print("is_goal_reached(['right','right']) ->", is_goal_reached(["right","right"]))
print("-"*60)

# 12. Write a Python class named Student with two attributes: student_id, student_name.
# Add a new attribute: student_class. Create a function to display all attributes and their values.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        # student_class will be added later when needed

    def add_class(self, cls_name):
        self.student_class = cls_name

    def display_attributes(self):
        # collect attributes manually and print
        attrs = []
        # using __dict__ is allowed for simple display, but we'll loop through known names
        if hasattr(self, "student_id"):
            attrs.append(("student_id", self.student_id))
        if hasattr(self, "student_name"):
            attrs.append(("student_name", self.student_name))
        if hasattr(self, "student_class"):
            attrs.append(("student_class", self.student_class))
        # print attributes
        for name, val in attrs:
            print(name + ":", val)

print("Q12 Example:")
s = Student(101, "Ravi")
s.add_class("SE")
s.display_attributes()
print("-"*60)

# 13. Write a Python class named Student with two instances student1, student2 and assign values.
# Print all the attributes of the student1, student2 instances with their values in the given format.

class Student2:
    def __init__(self, student_id=None, student_name=None, student_class=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def __str__(self):
        # return formatted string of attributes
        return "student_id: {}, student_name: {}, student_class: {}".format(self.student_id, self.student_name, self.student_class)

print("Q13 Example:")
student1 = Student2(1, "Aman", "SE")
student2 = Student2(2, "Neha", "TE")
print("student1 ->", student1)
print("student2 ->", student2)
print("-"*60)

# 14. Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.141592653589793
        return pi * self.radius * self.radius

    def perimeter(self):
        pi = 3.141592653589793
        return 2 * pi * self.radius

print("Q14 Example:")
c = Circle(3)
print("Circle radius 3 -> area:", c.area(), "perimeter:", c.perimeter())
print("-"*60)

# 15. Write a Python class that has two methods: get_String and print_String,
# get_String accept a string from the user and print_String prints the string in upper case.

class StringHolder:
    def __init__(self):
        self.s = ""

    def get_String(self, s_in):
        # accept string (to keep non-interactive we pass string)
        self.s = s_in

    def print_String(self):
        # manual upper-case conversion
        res = ""
        i = 0
        while i < len(self.s):
            ch = self.s[i]
            # if lowercase letter, convert to uppercase by ASCII difference
            if 'a' <= ch <= 'z':
                # ord('A') - ord('a') = -32, so subtract 32
                res += chr(ord(ch) - 32)
            else:
                res += ch
            i += 1
        print(res)

print("Q15 Example:")
sh = StringHolder()
sh.get_String("hello World!")
sh.print_String()
print("-"*60)

# 16. Write a Python class named Robot that has attributes: name, task, and battery_level.
# Methods: perform_task() decreases battery by 10%, recharge() sets battery to 100, status() prints info.

class Robot:
    def __init__(self, name, task, battery_level=100):
        self.name = name
        self.task = task
        self.battery_level = float(battery_level)

    def perform_task(self):
        # prints task and decrease battery by 10%
        print(self.name + " is performing task:", self.task)
        # decrease by 10% of current battery or fixed 10 percent points? We'll reduce 10 percentage points
        self.battery_level -= 10.0
        if self.battery_level < 0:
            self.battery_level = 0.0
        print("Battery decreased by 10%. Current level:", self.battery_level, "%")

    def recharge(self):
        self.battery_level = 100.0
        print(self.name + " recharged to 100%.")

    def status(self):
        print("Robot:", self.name)
        print("Task:", self.task)
        print("Battery level:", str(self.battery_level) + "%")

print("Q16 Example:")
r = Robot("R2-D2", "cleaning", 50)
r.status()
r.perform_task()
r.status()
r.recharge()
r.status()
print("-"*60)

print("All questions from Work Sheet 3 solved in this single file.")
