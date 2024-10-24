"""Две команды."""

def main():
    A = int(input())
    B = int(input())
    N = int(input())

    if B % N == 0:
        min_B = B // N
    else:
        min_B = B // N + 1

    if A > min_B:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()