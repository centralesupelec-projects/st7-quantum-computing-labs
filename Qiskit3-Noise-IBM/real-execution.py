from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime import SamplerV2 as Sampler
import numpy as np
from circuit import circuit_1

service = QiskitRuntimeService(
    channel='ibm_quantum',
    instance='ibm-q/open/main',
    token='<token>'
    )

backend = service.least_busy(operational=True, simulator=False)

qc = circuit_1()
pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
qc2 = pm.run(qc)

sampler = Sampler(backend)
job = sampler.run([qc2])
result = job.result()

res = np.array(result[0].data.meas.get_bitstrings())
values, counts = np.unique(res, return_counts=True)
counts = {values[i] : counts[i] for i in range(len(values))}
print(counts)
plot_histogram(counts)