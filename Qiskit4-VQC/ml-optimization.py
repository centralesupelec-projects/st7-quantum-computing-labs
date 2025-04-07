from qiskit.circuit import ParameterVector
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
from qiskit import transpile
from scipy.optimize import minimize

simulator = AerSimulator()

qc5 = QuantumCircuit(5)
pv1 = np.random.random(5)
pv2 = ParameterVector("theta", 5)
for i in range(5):
    qc5.rx(pv1[i], i)
    qc5.rx(pv2[i], i)
qc5.measure_all()
qc5.draw()

## Cost function

def f(parameter):
    qc6 = qc5.assign_parameters({pv2: [i for i in parameter]})
    qc6.measure_all()
    circ = transpile(qc6, simulator)
    result = simulator.run(circ, shots=1000).result()
    counts = result.get_counts(circ)
    cost_value = 1 - (counts["00000 00000"]/4000)
    print(cost_value)
    return cost_value

## Optimization

x0 = np.random.random(5)
res = minimize(f, x0, method='COBYLA')
print("random angles of first rotation :", pv1)
print("optimized angle :",res.x)

print(res)
qc6 = qc5.assign_parameters({"theta["+str(i)+"]":res.x[i] for i in range(5)})
#qc6 = qc5.assign_parameters(parameter)
result = simulator.run(qc6, shots=4000).result()
counts = result.get_counts(qc6)
print(counts)