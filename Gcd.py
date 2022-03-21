def cal(x, y):
    if y == 0:
        return x
    else:
        return cal(y, x % y)


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print()
print(f"GCD of {a} & {b} is:  {cal(a, b)}")
