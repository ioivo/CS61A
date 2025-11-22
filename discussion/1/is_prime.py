def is_Prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

if is_Prime(1):
    print("True")
else:
    print("False")