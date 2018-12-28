int_example = 42
float_example = 32.64
str_example = "Hello, World!"

list_example = [0, 1, 2, 3]
tuple_example = (0, 1, 2, 3)

a = "blah"
b = "blah"

# if two variables is not equal to each other:
if a != b:
    pass
# or (as the same as above)
if not a == b:
    pass

if a < b:
    # 满足 a < b
    pass
else:
    # 不满足 a < b
    pass

if a < b:
    # 满足 a < b
    pass
elif 2 * a < b:
    # 满足 2 * a < b
    pass
# ........
else:
    # 所有条件都不满足
    pass
