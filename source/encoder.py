from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def shor_encoding(input_circuit):

    # registers
    ancillary_qubits = QuantumRegister(8, 'ancillary')
    input_circuit.add_register(ancillary_qubits)

    q = QuantumRegister(9, 'q')
    qc = QuantumCircuit(q)
    

    # gate
    qc.cx(q[0], q[3])
    qc.cx(q[0], q[6])
    qc.h(q[0])
    qc.h(q[6])
    qc.h(q[3])

    qc.cx(q[0], q[1])
    qc.cx(q[6], q[7])
    qc.cx(q[3], q[4])

    qc.cx(q[0], q[2])
    qc.cx(q[6], q[8])
    qc.cx(q[3], q[5])

    qc.barrier()

    encoded_circuit = input_circuit.compose(qc)

    return encoded_circuit



