from math import sqrt
def testIterationMethod():
    x0 = 1.5
    TOl = 0.000001
    x = iterationsAlgorithm(1.5,TOL)

    assert(abs(s - sqrt()) < TOL)
    print("Iteration Algorith test passed")

#def testBisectionMethod():

def runTests():
    testIterationMethod()
    pass    