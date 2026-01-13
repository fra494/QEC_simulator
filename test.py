# from util.full_circuits import *
# from qiskit import QuantumCircuit, QuantumRegister


# q = QuantumRegister(9, 'q')
# qc = QuantumCircuit(q)


# shor_encoding(qc)

# qc.draw(output='mpl', filename="./circuits_img/encoder.png")

# from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# q = QuantumRegister(5, 'q')
# c = ClassicalRegister(2, 'c')
# qc = QuantumCircuit(q, c)

# qc.h(q[2])
# qc.h(q[1])
# qc.h(q[0])

# qc.cx(q[0], q[3])
# qc.cx(q[1], q[3])
# qc.cx(q[0], q[4])

# qc.h(q[1])
# qc.h(q[0])

# qc.cx(q[2], q[4])
# qc.h(q[2])

# qc.measure(q[3], c[0])
# qc.measure(q[4], c[1])




# qc.draw(output='mpl', filename="./circuits_img/phase_flip_dect.png")

from util.full_circuits import depolarizing_channel_error


depolarizing_channel_error(0, 1, 0.1, True)