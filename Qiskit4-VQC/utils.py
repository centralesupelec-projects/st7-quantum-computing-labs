from qiskit import transpile
from qiskit_aer import AerSimulator

def get_cost(qc, howmany):
    simulator = AerSimulator()
    circ = transpile(qc, simulator)
    result = simulator.run(circ, shots=howmany).result()
    counts = result.get_counts(circ)
    cost_value = 1 - (counts["00000 00000"]/howmany)
    # print(f"{cost_value:.3f}")
    return cost_value

def runSample(qc,howmany):
    simulator = AerSimulator()
    job = simulator.run(qc, shots=howmany)
    res = job.result().get_counts(qc)
    return res