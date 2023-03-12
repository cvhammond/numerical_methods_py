import sys

def bisection_method(f, x_l, x_u):

    x_r_old = sys.maxsize

    while abs(x_u - x_l) > 1e-15:
        x_r = (x_l + x_u) / 2
        if x_r != 0 and abs((x_r - x_r_old) / x_r) < 1e-9:
            return x_r
        x_r_old = x_r

        if f(x_r) * f(x_l) < 0:
            x_u = x_r
            continue
        if f(x_r) * f(x_l) > 0:
            x_l = x_r
            continue
        if f(x_r) * f(x_l) == 0:
            return x_r

def main():

    def f(x): # 2x^3 - 3x^2 + 1
       return (2 * (x ** 3)) - (3 * (x ** 2)) + 1

    print(bisection_method(f, -1, 0.5)) # -0.500000...

if __name__ == "__main__":
    main()
