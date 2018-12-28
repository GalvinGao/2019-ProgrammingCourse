
def main(x):
    if x <= 150:
        return x * .4463
    elif x <= 400:
        return (x - 150) * .4663 + 150 * .4463
    else:
        return 250 * .4663 + 150 * .4463 + (x - 400) * .5663

print("{0:.2f}".format(main(int(input()))))
