global cin, count
cin = '''6
4 3 2 5 3 5'''
count = 0
cin = [int(x) for x in cin.splitlines()[1].split()]

while 0 not in cin:
    count += 1
    cin = [x-1 for x in cin]
