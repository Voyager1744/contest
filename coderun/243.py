import threading


def print_num():
    for i in range(33):
        print(i)


def print_letter():
    for i in "abcdefghijklmnopqrstuvwxyz":
        print(i)


t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)

t1.start()
t2.start()
