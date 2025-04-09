from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from utils import runSample

## Grover Algorithm ##
# Quantum search algorithm that finds with high probability
# the unique input to a black box function that produces a
# particular output value - Amplitude amplification
# We implement a boolean AND function on N variables (f)

N = 4 # Number of variables of f

def oracle(qc,q,aux):
    """
    The orcale is written st |x> -> (-1)^F(x)|x>
    where F is the considered function
    """
    qc.h(aux[0])            # Hadamard gate
    qc.mcx(q[0:], aux[0])   # Unitary f function (boolean AND)
    qc.h(aux[0])            # Hadamard gate

def u0bot(qc,q):
    """
    This function is Uo orthogonal operator
    |11...1> -> -|11...1>
    |x> -> |x> if ≠ |11...1>
    """
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
    q = QuantumRegister(N)
    c = ClassicalRegister(N) 
    aux = QuantumRegister(1)  # store additional wire used for O
    qc = QuantumCircuit(q,aux,c)

    hadamard_tower(qc, q)
    qc.x(aux[0])  # Set aux bit to 1
    
    for _ in range(n_iter):
        qc.barrier()
        oracle(qc,q, aux)
        hadamard_tower(qc, q)
        u0bot(qc,q)
        hadamard_tower(qc, q)

    qc.measure(q,c)
    return qc

# Print Grover circuit
print("--- Grover circuit size 2 --- \n")
print(grover(2))

# Run the circuit, for different nb_iterations values
print("--- Circuit run for different nb_iterations --- \n")
for i in range(15):
    s = runSample(grover(i),1000)
    k="1"*N
    if k in s:
        sample_number = s[k]
    else:
        sample_number = 0
    print(f"Iteration {i} | Number of samples: {sample_number}")

# Note: This probabilty shows a regularity: increasing until n_iterations of 3, decreasing later. 
# This is because there is an optimal amount of iterations to increase the probability of good result.
# The optimal number of iterations pi/4*sqrt(2^N/nb_good_states) which here equals pi.