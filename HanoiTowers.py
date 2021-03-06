
'''The Tower of Hanoi is a mathematical game or puzzle.
 It consists of three rods and a number of disks of different sizes,
 which can slide onto any rod.
This is a recursive implementation of this problem in Python.
'''


def TowerOfHanoi(n, src, dest, aux):
    if n == 1:
        print("Move disk 1 from source", src, "to destination", dest)
        return
    TowerOfHanoi(n - 1, src, aux, dest)
    print("Move disk", n, "from source", src, "to destination", dest)
    TowerOfHanoi(n - 1, aux, dest, src)


if __name__ == "__main__":
    n = 4
    TowerOfHanoi(n, 'A', 'B', 'C')
