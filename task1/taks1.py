
def check_data(n, m):
    if n < 0:
        return False
    else:
        return True 

def taks1(n, m):

    if not check_data(n, m):
        print("n не может быть меньше 0")
        return

    i = 1
    while True:
        print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break

print("Введите два числа в одной строке:")
n = int(input("Введите n: "))
m = int(input("Введите m: "))
taks1(n, m)

























