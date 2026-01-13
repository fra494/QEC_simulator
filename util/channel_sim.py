from qiskit.quantum_info import Kraus
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile

import numpy as np
from random import randint
from qiskit.quantum_info import Kraus, Pauli



def quantum_pauli_channel_one_qb(input_circuit, p):

    q = input_circuit.qubits

    i = np.random.randint(0,8)

    if np.random.rand() < p:
        input_circuit.x(q[i])
    if np.random.rand() < p:
        input_circuit.y(q[i])
    if np.random.rand() < p:
        input_circuit.z(q[i])

    input_circuit.barrier()


def quantum_pauli_channel(input_circuit, p):

    q = input_circuit.qubits

    for i in range(9):
        if np.random.rand() < p:
            input_circuit.x(q[i])
        if np.random.rand() < p:
            input_circuit.y(q[i])
        if np.random.rand() < p:
            input_circuit.z(q[i])

    input_circuit.barrier()
    

def quantum_delay_channel_all_qb(input_circuit):

    q = input_circuit.qubits

    input_circuit.delay(100)
    input_circuit.barrier()



def quantum_delay_channel_one_qb(input_circuit):

    q = input_circuit.qubits

    input_circuit.delay(100, q[randint(0,8)])
    input_circuit.barrier()



def ideal_empty_channel(input_circuit):

    q = input_circuit.qubits

    input_circuit.barrier()
