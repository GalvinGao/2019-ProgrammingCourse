# enumerate - Logic Control

a = [42, "foo", 73]
# print(list(enumerate(a)))
for index, obj in enumerate(a):
    print(f"{index} : {obj}")
