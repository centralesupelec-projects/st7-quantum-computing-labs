## Utils functions for Qiskit manipulations ##

from qiskit_aer import AerSimulator, StatevectorSimulator
import numpy as np

def processOneState(st): 
    """
    Length = power of 2
    """
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

def printOneState(d):
    """
    Get a dict as per processStates output
    """
    for k in d:
        im = d[k].imag
        re = d[k].real
        if abs(im) >= 0.001 or abs(re) >= 0.001:
            print("% .3f + % .3fj |%s>" % (re,im,k))

def printFinalRes(result):
    printOneState(processOneState(list(np.asarray(result))))


def runStateVector(qc):
    """
    Compute the output state vector
    Print its value in a nice format
    Return it
    """
    simulator = StatevectorSimulator()
    job = simulator.run(qc.decompose(reps=6), memory=True)
    job_result = job.result()
    result = job_result.results[0].to_dict()['data']['statevector']
    printFinalRes(result)
    return result

def runSample(qc,howmany):
    """
    Run the circuit with a simulator
    Need measure to get a result
    Print the result of measures and return a dict of it
    """
    simulator = AerSimulator()
    job = simulator.run(qc.decompose(reps=6), shots=howmany)
    res = dict(job.result().get_counts(qc))
    print(res)
    return res