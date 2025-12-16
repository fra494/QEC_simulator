from qiskit.quantum_info import Kraus
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile

import numpy as np
from qiskit.quantum_info import Kraus, Pauli


    
def pauli_channel_circuit_model(pX, pY, pZ):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    for i in range(9):
        if np.random.rand() < pX:
            qc.x(q[i])
        if np.random.rand() < pY:
            qc.y(q[i])
        if np.random.rand() < pZ:
            qc.z(q[i])

    qc.barrier()
        
    return qc


def quantum_channel(input_circuit):

    pX = 0.05
    pY = 0
    pZ = 0

    simulated_channel = input_circuit.compose(pauli_channel_circuit_model(pX, pY, pZ))

    return simulated_channel