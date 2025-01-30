def bisectionMethod(a,b,N,f,TOL): # a and b initial values, N is maxIterations
                                # f functions to find root for and TOL is degree of tolerance
    iterations = 1
    while iterations <= N:
        m = a + (b - a) / 2
        FM = f(m)
        if abs(FM) < TOL:
            print(f"Convergence after {iterations} iterations")
            return m

    print("Method failed")
def newtonsMethod(p0,f,fd,TOL,N): # p0 is initial value and TOL degree of tolerance
                                # f is function to find root for and fd is derivative
    iterations = 1              # N is max iterations

    p = p0
    while iterations <= N:
        p = p - f(p) / fd(p)
        if abs(f(p)) < TOL:
            print(f"Convergence after {iterations} iterations")
            return p
        iterations += 1
    print("Method failed")
def fixedPointMethod(p0,f,TOL,N): #p0 is initial value and f is function to find fixed point
                                  # N is max iterations
    iterations = 1
    while iterations <= N:
        p = f(p0)
        if abs(p - p0) < TOL:
            print(f"Convergence after {iterations} iterations")
            return p0
        iterations += 1
        p0 = p
    print("Method failed")

def iterationsAlgorithm(x0,TOL): #x is initial value
    iterations = 0
    diff = 0
    x = x0

    while diff >= TOL:
        iterations += 1

        y = x
        x = (x / 2) + 1 / x

        diff = abs(y - x)

    print(f"Convergence after {iterations} iterations")
    return x              
    