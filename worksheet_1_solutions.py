# 1. Write a Python program to print the following string in a specific format...
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above 
# the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are".

print("Q1 Solution:")
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
print("-"*60)

# 2. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
print("Q2 Solution:")
first = input("Enter first name: ")
last  = input("Enter last name: ")
# print in reverse order with a space
print(last + " " + first)
print("-"*60)

# 3. Write a Python program that calculates the area of a circle based on the radius entered by the user.
print("Q3 Solution:")
# avoid using pow(); implement square manually
def square(x):
    return x * x

radius_str = input("Enter radius (number): ")
# basic conversion without fancy functions
try:
    radius = float(radius_str)
    pi = 3.141592653589793
    area = pi * square(radius)
    print("Area of circle with radius", radius, "is", area)
except:
    print("Invalid input for radius.")
print("-"*60)

# 4. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
print("Q4 Solution:")
colors = ["Red", "Green", "White", "Black"]
# get first and last manually
if len(colors) > 0:
    first_color = colors[0]
    last_color = colors[len(colors)-1]
    print("First color:", first_color)
    print("Last color:", last_color)
else:
    print("List is empty.")
print("-"*60)

# 5. Write a Python program that accepts an integer (n) and computes the value of n + nn + nnn.
# Sample value of n is 5
print("Q5 Solution:")
n_str = input("Enter an integer n (e.g., 5): ")
# build nn and nnn as strings then convert to int (manually convert)
def str_to_int(s):
    # simple function to convert numeric string to int (handles negative)
    if s == "":
        return 0
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    total = 0
    for ch in s:
        if '0' <= ch <= '9':
            total = total * 10 + (ord(ch) - ord('0'))
        else:
            raise ValueError("Non-digit found")
    return sign * total

try:
    n_int = str_to_int(n_str.strip())
    nn = str(n_int) + str(n_int)
    nnn = nn + str(n_int)
    result = n_int + str_to_int(nn) + str_to_int(nnn)
    print(n_int, "+", nn, "+", nnn, "=", result)
except Exception as e:
    print("Invalid input.", e)
print("-"*60)

# 6. Write a Python program that accepts a sequence of comma-separated numbers and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
print("Q6 Solution:")
seq = input("Enter comma-separated numbers (e.g., 3,5,7,23): ")
items = []
num_str = ""
for ch in seq:
    if ch == ',':
        if num_str.strip() != "":
            items.append(num_str.strip())
        num_str = ""
    else:
        num_str += ch
if num_str.strip() != "":
    items.append(num_str.strip())

# convert to integers where possible
nums = []
for s in items:
    try:
        nums.append(str_to_int(s))
    except:
        # if conversion fails, keep as string
        nums.append(s)

print("List:", nums)
# build tuple manually (we'll use built-in tuple constructor because creating tuple by hand is same as conversion)
tup = tuple(nums)
print("Tuple:", tup)
print("-"*60)

# 7. Write a program that will convert celsius value to Fahrenheit.
print("Q7 Solution:")
c_str = input("Enter temperature in Celsius: ")
try:
    c = float(c_str)
    # F = C * 9/5 + 32 -> avoid division by using integers where possible
    f = (c * 9.0) / 5.0 + 32.0
    print(c, "Celsius =", f, "Fahrenheit")
except:
    print("Invalid Celsius input.")
print("-"*60)

# 8. User will input (2 numbers). Write a program to swap the numbers. Add incrementally in any one variable.
print("Q8 Solution:")
a_str = input("Enter first number a: ")
b_str = input("Enter second number b: ")
try:
    a = str_to_int(a_str)
    b = str_to_int(b_str)
    print("Before swap: a =", a, ", b =", b)
    # swap without using tuple swap: use temp
    temp = a
    a = b
    b = temp
    # increment one variable by 1
    b = b + 1
    print("After swap and incrementing second value by 1: a =", a, ", b =", b)
except Exception as e:
    print("Invalid input.", e)
print("-"*60)

# 9. Write a program that will tell whether the number entered by the user is odd or even.
print("Q9 Solution:")
num_str = input("Enter integer to check odd/even: ")
try:
    num = str_to_int(num_str)
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
except:
    print("Invalid integer.")
print("-"*60)

# 10. Write a program that will tell whether the given year is a leap year or not.
print("Q10 Solution:")
yr_str = input("Enter year (e.g., 2024): ")
try:
    yr = str_to_int(yr_str)
    # leap year rule: divisible by 4 and (not divisible by 100 unless divisible by 400)
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        print(yr, "is a Leap Year")
    else:
        print(yr, "is NOT a Leap Year")
except:
    print("Invalid year.")
print("-"*60)

# 11. Write a program to find the Euclidean distance between two coordinates.
print("Q11 Solution:")
print("Enter coordinates of point 1 (x1,y1):")
x1s = input("x1: "); y1s = input("y1: ")
print("Enter coordinates of point 2 (x2,y2):")
x2s = input("x2: "); y2s = input("y2: ")
try:
    x1 = float(x1s); y1 = float(y1s); x2 = float(x2s); y2 = float(y2s)
    dx = x2 - x1
    dy = y2 - y1
    # compute sqrt manually using simple Newton's method
    def my_sqrt(x):
        if x < 0:
            raise ValueError("negative")
        if x == 0:
            return 0.0
        guess = x / 2.0
        for _ in range(20):
            guess = (guess + x/guess) / 2.0
        return guess
    dist = my_sqrt(dx*dx + dy*dy)
    print("Euclidean distance =", dist)
except Exception as e:
    print("Invalid coordinate input.", e)
print("-"*60)

# 12. Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
print("Q12 Solution:")
a_str = input("Angle 1: ")
b_str = input("Angle 2: ")
c_str = input("Angle 3: ")
try:
    a = float(a_str); b = float(b_str); c = float(c_str)
    # angles must be positive and sum to 180
    if a > 0 and b > 0 and c > 0 and abs((a + b + c) - 180.0) < 1e-6:
        print("Yes, angles form a triangle.")
    else:
        print("No, angles do NOT form a triangle.")
except:
    print("Invalid angles.")
print("-"*60)

# 13. WAP to find compound interest for given values.
print("Q13 Solution:")
p_str = input("Principal amount P: ")
r_str = input("Annual rate of interest (percent) r (e.g., 5 for 5%): ")
t_str = input("Time in years t: ")
n_str = input("Number of times interest applied per year n (e.g., 1 for yearly): ")
try:
    P = float(p_str); r = float(r_str); t = float(t_str); n = float(n_str)
    # compound interest formula A = P * (1 + r/(100*n))**(n*t)
    # implement power via loop (no **)
    base = 1.0 + (r / 100.0) / n
    exp = int(n * t)
    # compute base^exp manually (if exp is large we use float multiply in loop)
    power = 1.0
    for _ in range(exp):
        power = power * base
    A = P * power
    CI = A - P
    print("Amount after", t, "years =", A)
    print("Compound Interest =", CI)
except Exception as e:
    print("Invalid input.", e)
print("-"*60)

# 14. Given a positive integer N, check if the number is prime or not.
print("Q14 Solution:")
N_str = input("Enter positive integer N to check prime: ")
try:
    N = str_to_int(N_str)
    if N <= 1:
        print(N, "is not prime.")
    else:
        is_prime = True
        # check divisibility from 2 to sqrt(N)
        def int_sqrt(x):
            # integer sqrt via binary search
            if x < 0: return 0
            low = 0; high = x
            while low <= high:
                mid = (low + high) // 2
                if mid*mid <= x:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        limit = int_sqrt(N)
        i = 2
        while i <= limit:
            if N % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(N, "is PRIME")
        else:
            print(N, "is NOT prime")
except Exception as e:
    print("Invalid input.", e)
print("-"*60)

# 15. Given a positive integer N. The task is to find 1^2 + 2^2 + 3^2 + ... + N^2.
print("Q15 Solution:")
N2_str = input("Enter positive integer N to compute sum of squares: ")
try:
    N2 = str_to_int(N2_str)
    if N2 < 0:
        print("N should be non-negative.")
    else:
        total = 0
        i = 1
        while i <= N2:
            total += i * i
            i += 1
        print("Sum of squares up to", N2, "=", total)
except Exception as e:
    print("Invalid input.", e)
print("-"*60)

print("All questions completed in this single file. Thank you!")
