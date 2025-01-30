from math import sqrt,sin,cos,pi
from src.assignment1 import iterationsAlgorithm,fixedPointMethod,newtonsMethod,bisectionMethod
def testIterationMethod():
    x0 = 1.5
    TOL = 0.000001
    x = iterationsAlgorithm(1.5,TOL)

    assert(abs(x - sqrt(2)) < TOL)
    print("Iteration Algorithm test passed")

def testBisectionMethod():
    TOL = 1e-3
    a = 1
    b = 2
    N = 1000
    f = lambda x : x * x * x + 4 * x * x - 10

    iterations = bisectionMethod(a,b,N,f,TOL)
    assert(iterations == 10)
    print("Bisection Method Passed")

def testFixedPointMethod():
    p0 = 1.5
    TOL = 1e-6
    f = lambda x : x - x * x * x - 4 * x * x + 10
    N = 1000 
    iterations = fixedPointMethod(p0,f,TOL,N)
    assert(iterations == -1)
    print("Test Fixed Point Method Passed") 
def testNewtonMethod():
    p0 = pi / 4
    N = 1000
    f = lambda x : cos(x) - x
    fd = lambda x: -1 * sin(x) - 1   
    TOL = 1e-8
    iterations = newtonsMethod(p0,f,fd,TOL,N)
    assert(iterations == 4)
    print("Newton Method passed")
def runTests():
    testIterationMethod()
    testBisectionMethod()
    testFixedPointMethod()
    testNewtonMethod()
    print("ALL tests passed")
    pass    