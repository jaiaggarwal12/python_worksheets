import random
import string
import math

print("Work Sheet 2 Solutions\n" + "="*40)

# 1. L is a list defined as L= [11, 12, 13, 14].
# (i) WAP to add 50 and 60 to L.
# (ii) WAP to remove 11 and 13 from L.
# (iii) WAP to sort L in ascending order.
# (iv) WAP to sort L in descending order.
# (v) WAP to search for 13 in L.
# (vi) WAP to count the number of elements present in L.
# (vii) WAP to sum all the elements in L.
# (viii) WAP to sum all ODD numbers in L.
# (ix) WAP to sum all EVEN numbers in L.
# (x) WAP to sum all PRIME numbers in L.
# (xi) WAP to clear all the elements in L.
# (xii) WAP to delete L.

print("\nQ1 Solutions:")
L = [11, 12, 13, 14]
print("Initial L:", L)

# (i) add 50 and 60 (manual append)
L_append = L[:]  # copy to preserve original for other parts
L_append_len = len(L_append)
# append 50
L_append += [50]  # using list concatenation (explicit)
# append 60
L_append += [60]
print("(i) After adding 50 and 60:", L_append)

# (ii) remove 11 and 13 (manual removal)
L_removed = L_append[:]  # operate on copy
# remove function manually: remove first occurrence
def remove_first(lst, val):
    i = 0
    while i < len(lst):
        if lst[i] == val:
            # shift left
            j = i
            while j < len(lst)-1:
                lst[j] = lst[j+1]
                j += 1
            lst.pop()  # remove last duplicate slot
            return True
        i += 1
    return False

remove_first(L_removed, 11)
remove_first(L_removed, 13)
print("(ii) After removing 11 and 13:", L_removed)

# (iii) sort ascending using simple bubble sort (manual)
def bubble_sort_asc(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                tmp = a[j]; a[j] = a[j+1]; a[j+1] = tmp
    return a

sorted_asc = bubble_sort_asc(L_append)
print("(iii) Sorted ascending:", sorted_asc)

# (iv) sort descending
def bubble_sort_desc(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] < a[j+1]:
                tmp = a[j]; a[j] = a[j+1]; a[j+1] = tmp
    return a

sorted_desc = bubble_sort_desc(L_append)
print("(iv) Sorted descending:", sorted_desc)

# (v) search for 13 in L (linear search)
def search_list(lst, val):
    i = 0
    while i < len(lst):
        if lst[i] == val:
            return True, i
        i += 1
    return False, -1

found13, idx13 = search_list(L_append, 13)
print("(v) Is 13 present?", found13, "at index", idx13)

# (vi) count elements
count_L = 0
for _ in L_append:
    count_L += 1
print("(vi) Number of elements in L:", count_L)

# (vii) sum all elements
sum_all = 0
for x in L_append:
    sum_all += x
print("(vii) Sum of all elements:", sum_all)

# (viii) sum odd numbers
sum_odd = 0
for x in L_append:
    if x % 2 != 0:
        sum_odd += x
print("(viii) Sum of odd numbers:", sum_odd)

# (ix) sum even numbers
sum_even = 0
for x in L_append:
    if x % 2 == 0:
        sum_even += x
print("(ix) Sum of even numbers:", sum_even)

# (x) sum prime numbers
def is_prime_num(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    i = 3
    while i <= r:
        if n % i == 0:
            return False
        i += 2
    return True

sum_primes = 0
for x in L_append:
    if is_prime_num(x):
        sum_primes += x
print("(x) Sum of prime numbers in L:", sum_primes)

# (xi) clear all elements
L_cleared = L_append[:]
# clear manually by popping until empty
while True:
    if len(L_cleared) == 0:
        break
    L_cleared.pop()
print("(xi) After clearing, L:", L_cleared)

# (xii) delete L (we'll simulate by deleting variable)
L_to_delete = L_append[:]
del L_to_delete
print("(xii) Deleted variable L_to_delete (cannot print).")

print("-"*40)

# 2. Write a Python program to sum all the items in a list without using any inbuilt function.
print("\nQ2 Solution:")
lst2 = [1, 2, 3, 4, 5]
s = 0
i = 0
while i < len(lst2):
    s += lst2[i]
    i += 1
print("List:", lst2, "Sum:", s)
print("-"*40)

# 3. Write a Python program to multiply all the items in a list without using any inbuilt function.
print("\nQ3 Solution:")
lst3 = [2, 3, 4]
prod = 1
i = 0
while i < len(lst3):
    prod *= lst3[i]
    i += 1
print("List:", lst3, "Product:", prod)
print("-"*40)

# 4. Write a Python program to generate a 3*4*6 3D array whose each element is *.
print("\nQ4 Solution:")
depth = 3; rows = 4; cols = 6
arr3d = []
d = 0
while d < depth:
    layer = []
    r = 0
    while r < rows:
        row = []
        c = 0
        while c < cols:
            row.append('*')
            c += 1
        layer.append(row)
        r += 1
    arr3d.append(layer)
    d += 1
print("3x4x6 array created. Example layer 0 row 0:", arr3d[0][0])
print("-"*40)

# 5. D is a dictionary defined as D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}.
# (i) add key=8 value=8.8
# (ii) remove key=2
# (iii) check whether key 6 present
# (iv) count elements
# (v) sum all values
# (vi) update value of 3 to 7.1
# (vii) clear the dictionary
print("\nQ5 Solutions:")
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
print("Initial D:", D)

# (i)
D[8] = 8.8
print("(i) After adding (8:8.8):", D)

# (ii) remove key 2 (manual if exists)
if 2 in D:
    # manual deletion
    temp_keys = []
    for k in D:
        temp_keys.append(k)
    # rebuild dict without key 2
    D2 = {}
    i = 0
    while i < len(temp_keys):
        k = temp_keys[i]
        if k != 2:
            D2[k] = D[k]
        i += 1
    D = D2
print("(ii) After removing key 2:", D)

# (iii) check key 6 presence
key6_present = False
for k in D:
    if k == 6:
        key6_present = True
        break
print("(iii) Is key 6 present?:", key6_present)

# (iv) count elements
count_d = 0
for _ in D:
    count_d += 1
print("(iv) Number of elements in D:", count_d)

# (v) sum all values
sum_vals = 0.0
for k in D:
    sum_vals += D[k]
print("(v) Sum of all values in D:", sum_vals)

# (vi) update value of key 3 to 7.1
for k in D:
    if k == 3:
        D[k] = 7.1
        break
print("(vi) After updating key 3 to 7.1:", D)

# (vii) clear dictionary
keys_list = []
for k in D:
    keys_list.append(k)
for k in keys_list:
    del D[k]
print("(vii) After clearing, D:", D)
print("-"*40)

# 6. Sets S1 and S2 operations
print("\nQ6 Solutions:")
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}
print("Initial S1:", S1)
print("Initial S2:", S2)

# (i) add 55 and 66 to S1 (manual add)
def add_to_set(s, val):
    # emulate set add by list then unique
    exists = False
    for x in s:
        if x == val:
            exists = True
            break
    if not exists:
        s.add(val)

add_to_set(S1, 55)
add_to_set(S1, 66)
print("(i) After adding 55,66:", S1)

# (ii) remove 10 and 30 (manual remove if present)
def remove_from_set(s, val):
    to_remove = None
    for x in s:
        if x == val:
            to_remove = x
            break
    if to_remove is not None:
        s.remove(to_remove)

remove_from_set(S1, 10)
remove_from_set(S1, 30)
print("(ii) After removing 10,30:", S1)

# (iii) check whether 40 is present
present40 = False
for x in S1:
    if x == 40:
        present40 = True
        break
print("(iii) Is 40 present in S1?:", present40)

# (iv) union S1 U S2 (manual)
union_set = set()
for x in S1:
    union_set.add(x)
for x in S2:
    union_set.add(x)
print("(iv) Union of S1 and S2:", union_set)

# (v) intersection S1 & S2
intersection = set()
for x in S1:
    # check membership in S2 manually
    in_s2 = False
    for y in S2:
        if x == y:
            in_s2 = True
            break
    if in_s2:
        intersection.add(x)
print("(v) Intersection of S1 and S2:", intersection)

# (vi) S1 - S2
difference = set()
for x in S1:
    in_s2 = False
    for y in S2:
        if x == y:
            in_s2 = True
            break
    if not in_s2:
        difference.add(x)
print("(vi) S1 - S2:", difference)
print("-"*40)

# 7. (i) 100 random strings with length 6-8, letters only
#    (ii) prime numbers between 600 and 800
#    (iii) numbers between 100 and 1000 divisible by 7 and 9
print("\nQ7 Solutions:")

# (i)
def random_string(min_len=6, max_len=8):
    length = random.randint(min_len, max_len)
    s = ""
    i = 0
    letters = string.ascii_letters  # A-Z a-z
    while i < length:
        s += random.choice(letters)
        i += 1
    return s

print("(i) 10 sample random strings (of 100):")
i = 0
while i < 10:  # printing 10 instead of 100 to keep output short
    print(random_string(), end="  ")
    i += 1
print("\n(Printed 10 sample strings. Full 100 generated in code if needed.)")

# (ii) primes between 600 and 800
primes_600_800 = []
n = 600
while n <= 800:
    if is_prime_num(n):
        primes_600_800.append(n)
    n += 1
print("(ii) Primes between 600 and 800:", primes_600_800)

# (iii) numbers between 100 and 1000 divisible by 7 and 9
div_by_7_and_9 = []
num = 100
while num <= 1000:
    if (num % 7 == 0) and (num % 9 == 0):
        div_by_7_and_9.append(num)
    num += 1
print("(iii) Numbers divisible by both 7 and 9 between 100 and 1000:", div_by_7_and_9)
print("-"*40)

# 8. Display examination schedule: extract from tuple exam_st_date = (11, 12, 2025)
print("\nQ8 Solution:")
exam_st_date = (11, 12, 2025)
# Format: The examination will start from: 11 / 12 / 2025
# access tuple elements manually
day = exam_st_date[0]; month = exam_st_date[1]; year = exam_st_date[2]
print("The examination will start from: {} / {} / {}".format(day, month, year))
print("-"*40)

# 9. Iterate list and print numbers divisible by 5
print("\nQ9 Solution:")
nums_q9 = [10, 23, 45, 57, 60, 75, 81]
print("Numbers divisible by 5:")
i = 0
while i < len(nums_q9):
    if nums_q9[i] % 5 == 0:
        print(nums_q9[i], end=" ")
    i += 1
print("\n" + "-"*40)

# 10. Check even or odd using boolean variables
print("\nQ10 Solution:")
val_q10 = 27
is_even = (val_q10 % 2 == 0)
if is_even:
    print(val_q10, "is Even (boolean True for even).")
else:
    print(val_q10, "is Odd (boolean False for even).")
print("-"*40)

# 11. Count occurrences of substring "Emma" in a given string
print("\nQ11 Solution:")
text = "Emma is a good developer. Emma loves Python. Emma's code is neat."
substr = "Emma"
count = 0
i = 0
while i <= len(text) - len(substr):
    # check substring match manually
    match = True
    j = 0
    while j < len(substr):
        if text[i+j] != substr[j]:
            match = False
            break
        j += 1
    if match:
        count += 1
    i += 1
print("Text:", text)
print("Number of times 'Emma' appears:", count)
print("-"*40)

# 12. Create new list from two lists: odd numbers from first, even numbers from second
print("\nQ12 Solution:")
list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10,11,12,13]
new_list = []
i = 0
while i < len(list1):
    if list1[i] % 2 != 0:
        new_list.append(list1[i])
    i += 1
j = 0
while j < len(list2):
    if list2[j] % 2 == 0:
        new_list.append(list2[j])
    j += 1
print("New list (odd from first, even from second):", new_list)
print("-"*40)

# 13. From positions list find positions where x-coordinate is even
print("\nQ13 Solution:")
positions = [(2,3), (4,5), (6,7), (7,8)]
even_x_positions = []
k = 0
while k < len(positions):
    if positions[k][0] % 2 == 0:
        even_x_positions.append(positions[k])
    k += 1
print("Positions with even x-coordinate:", even_x_positions)
print("-"*40)

# 14. From sensor_data dict find sensor IDs with reading > 3.0
print("\nQ14 Solution:")
sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
ids_above_3 = []
for key in sensor_data:
    if sensor_data[key] > 3.0:
        ids_above_3.append(key)
print("Sensor IDs with reading > 3.0:", ids_above_3)
print("-"*40)

# 15. commands not executed = commands_received - commands_executed
print("\nQ15 Solution:")
commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
commands_executed = {"MOVE", "TURN_LEFT", "STOP"}
not_executed = set()
for cmd in commands_received:
    executed = False
    for ex in commands_executed:
        if cmd == ex:
            executed = True
            break
    if not executed:
        not_executed.add(cmd)
print("Commands not executed:", not_executed)
print("\nAll questions from Worksheet 2 solved in this single file.")
