import sys

def fixed_point_iteration(g, x_0):
    x_r_old = sys.maxsize
    x_r = x_0
    counter = 0
    while counter < 1e5:
        x_r = g(x_r)
        counter += 1
        if x_r != 0 and abs((x_r - x_r_old) / x_r) < 1e-9:
            return x_r
        x_r_old = x_r
    return x_r

def main():
    # x^2 + 2x - 3 = 0 rearranges to x = (-x^2 + 3) / 2
    def g(x):
        return (-x ** 2 + 3) / 2

    print(fixed_point_iteration(g, 0))

if __name__ == "__main__":
    main()
