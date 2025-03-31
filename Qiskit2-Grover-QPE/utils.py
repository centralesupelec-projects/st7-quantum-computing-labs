import numpy as np
from math import pi, gcd
from qiskit import *
from qiskit_aer import AerSimulator, StatevectorSimulator

def processOneState(st): # Longueur = puissance de 2
        s = list(st)
        if len(s) == 2:
            return {'0' : s[0], '1' : s[1]}
        else:
            a0 = processOneState(s[:len(s)//2])
            a1 = processOneState(s[len(s)//2:])
            r = {}
            for k in a0:
                r['0' + k] = a0[k]
            for k in a1:
                r['1' + k] = a1[k]
            return r

def printOneState(d): # get a dict as per processStates output
    for k in d:
        im = d[k].imag
        re = d[k].real
        if abs(im) >= 0.001 or abs(re) >= 0.001:
            print("% .3f + % .3fj |%s>" % (re,im,k))

def printFinalRes(result):
    printOneState(processOneState(list(np.asarray(result))))


def runStateVector(qc):
    simulator = StatevectorSimulator()
    job = simulator.run(qc.decompose(reps=6), memory=True)
    job_result = job.result()
    result = job_result.results[0].to_dict()['data']['statevector']
    printFinalRes(result)

def runStateVectorSeveralTimes(qc, howmany):
    qc.save_statevector(label = 'collect', pershot = True)
    simulator = StatevectorSimulator()
    job = simulator.run(qc.decompose(reps=6), memory=True, shots=howmany)
    result = job.result()
    memory = result.data(0)['memory']
    collect = result.data(0)['collect']
    r = {}
    for i in range(len(collect)):
        r[str(collect[i])] = (0, collect[i])
    for i in range(len(collect)):
        n, v = r[str(collect[i])]
        r[str(collect[i])] = (n+1, v)
    for k in r:
        i, v = r[k]
        print(f"With {i} occurences:")
        printFinalRes(v)

def runSample(qc,howmany):
    simulator = AerSimulator()
    job = simulator.run(qc.decompose(reps=6), shots=howmany)
    res = dict(job.result().get_counts(qc))
    return res