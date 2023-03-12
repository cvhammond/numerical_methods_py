import sys

def newton_raphson_method(f, df, x_0):
    x_r_old = sys.maxsize
    x_r = x_0
    counter = 0
    while counter < 1e5:
        x_r = x_r - f(x_r) / df(x_r)
        counter += 1
        if x_r != 0 and abs((x_r - x_r_old) / x_r) < 1e-9:
            return x_r
        x_r_old = x_r
    return x_r

def main():

    def f(x):
        return x ** 2 + 2 * x - 3

    def df(x):
        return 2 * x + 2

    print(newton_raphson_method(f, df, 0))

if __name__ == "__main__":
    main()
