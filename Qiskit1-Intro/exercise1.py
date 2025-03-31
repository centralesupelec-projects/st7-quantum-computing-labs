from qiskit import *
from utils import runStateVector

## Exercise 1 ##

# 1 - Build a circuit producing the 4-qubit state (1/sqrt2)*(|0000> - |1111>)
# 2 - Make it parametric: we want to be able to make an n-qubit state of that form
# 3 - Try it for various n and make sure it works
# 4 - Output a sample (therefore: the result of a series of measures):
# can you see the -1 coefficient in front of the |111..1> ? Can you say why?

def exercise1(n):
    q = QuantumRegister(n, name="q1")
    c = ClassicalRegister(3)
    qc = QuantumCircuit(q, c)
    
    qc.x(q[0])
    qc.h(q[0])
    for i in range(1, n):
        qc.cx(q[0], q[i])
    print(qc)
    runStateVector(qc)

    # qc.measure(q,c)
    # return runSample(qc,1000)

exercise1(5)