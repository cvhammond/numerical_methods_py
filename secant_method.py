import sys

def secant_method(f, x_l, x_u):
    x_r = x_l
    x_r_old = x_u
    counter = 0
    while counter < 1e5:
        x_r_old_old = x_r_old
        x_r_old = x_r
        x_r = x_r - (f(x_r) * (x_r_old_old - x_r)) / (f(x_r_old_old) - f(x_r))
        counter += 1
        if x_r != 0 and abs((x_r - x_r_old) / x_r) < 1e-9:
            return x_r
    return x_r

def main():

    def f(x):
        return x ** 2 + 2 * x - 3

    print(secant_method(f, 0, 5))

if __name__ == "__main__":
    main()
