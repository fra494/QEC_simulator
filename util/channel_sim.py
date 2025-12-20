from qiskit.quantum_info import Kraus
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile

import numpy as np
from random import randint
from qiskit.quantum_info import Kraus, Pauli


    
def pauli_channel_circuit_model(p):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    for i in range(9):
        if np.random.rand() < p:
            qc.x(q[i])
        if np.random.rand() < p:
            qc.y(q[i])
        if np.random.rand() < p:
            qc.z(q[i])

    qc.barrier()
        
    return qc


def quantum_pauli_channel(input_circuit):

    p = 0.01

    qc = pauli_channel_circuit_model(p)

    simulated_channel = input_circuit.compose(qc)

    return simulated_channel, qc
    

def quantum_delay_channel_all_qb(input_circuit):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    qc.delay(100)
    qc.barrier()

    simulated_channel = input_circuit.compose(qc)

    return simulated_channel, qc


def quantum_delay_channel_one_qb(input_circuit):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    qc.delay(100, q[randint(0,8)])
    qc.barrier()

    simulated_channel = input_circuit.compose(qc)

    return simulated_channel, qc


def ideal_empty_channel(input_circuit):

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)

    qc.barrier()

    simulated_channel = input_circuit.compose(qc)

    return simulated_channel, qc