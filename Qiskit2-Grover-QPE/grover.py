from qiskit import *
from utils import *

N = 4 # Number of variables of f

def oracle(qc,q,aux):
    qc.h(aux[0]) # Hadamard gate
    qc.mcx(q[0:], aux[0]) # Unitary f function (boolean AND)
    qc.h(aux[0]) # Hadamard gate

def u0bot(qc,q):
    for i in range(N):
        qc.x(q[i])
    qc.h(q[0])
    qc.mcx(q[1:], q[0])
    qc.h(q[0])
    for i in range(N):
        qc.x(q[i])

def hadamard_tower(qc, q):
    for i in range(N):
        qc.h(q[i])

def grover(n_iter):
    q = QuantumRegister(N)    # The variables in superposition
    c = ClassicalRegister(N)  # Registers to store their measure
    aux = QuantumRegister(1)  # to store the additional wire used for O. Note that there is no need to measure it !
    qc = QuantumCircuit(q,aux,c)

    # TODO initialize the circuit
    hadamard_tower(qc, q)
    qc.x(aux[0]) # Set aux bit to 1
    
    for _ in range(n_iter):
        qc.barrier()       # To physically separate each iteration (does nothing but renders the circuit more legible)
        oracle(qc,q, aux)
        hadamard_tower(qc, q)
        u0bot(qc,q)
        hadamard_tower(qc, q)

    # Testing purpose
    # print(qc)
    # runStateVector(qc)

    qc.measure(q,c)        # Measure
    return qc


print(grover(2))   # Show the circuit for 2 iterations

# Run the circuit
for i in range(15):
    s = runSample(grover(i),1000)
    k=""
    for _ in range(N):
        k += "1"
    if k in s:
        print(i, s[k])
    else:
        print(i, 0)