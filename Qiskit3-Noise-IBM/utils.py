from qiskit import transpile

def runSample(qc,howmany, simulator):
    qc = transpile(qc, simulator)
    job = simulator.run(qc, shots=howmany)
    res = job.result().get_counts(qc)
    return res