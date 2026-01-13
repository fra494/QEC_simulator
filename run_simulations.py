from util.full_circuits import *

import numpy as np
import matplotlib.pyplot as plt

def success_probability(counts, correct_state="0", shots=100):
    return counts.get(correct_state, 0) / shots



def pauli_graph():
    ps = np.arange(0, 1, 0.05)

    y_corr = []
    y_nocorr = []

    alpha = 1
    beta = 0

    for p in ps:
        counts_corr = uniform_pauli_channel_error(alpha, beta, p)
        counts_nocorr = uniform_pauli_channel_error_nc(alpha, beta, p)

        y_corr.append(success_probability(counts_corr))
        y_nocorr.append(success_probability(counts_nocorr))


    plt.plot(ps, y_corr, marker='o', label='Con correzione (Shor)')
    plt.plot(ps, y_nocorr, marker='o', label='Senza correzione')

    plt.xlabel('Probabilità di errore p')
    plt.ylabel('Probabilità di successo')
    plt.legend()
    plt.grid(True)

    plt.show()


def depolarizing_graph():
    ps = np.arange(0, 1.3, 0.05)

    y_corr = []
    y_nocorr = []

    alpha = 1
    beta = 0

    for p in ps:
        counts_corr = depolarizing_channel_error(alpha, beta, p)
        counts_nocorr = depolarizing_channel_error_nc(alpha, beta, p)

        y_corr.append(success_probability(counts_corr))
        y_nocorr.append(success_probability(counts_nocorr))


    plt.plot(ps, y_corr, marker='o', label='Con correzione (Shor)')
    plt.plot(ps, y_nocorr, marker='o', label='Senza correzione')

    plt.xlabel('Probabilità di errore p')
    plt.ylabel('Probabilità di successo')
    plt.legend()
    plt.grid(True)

    plt.show()


def amplitude_graph():

    ps = np.arange(0, 1, 0.05)

    y_corr = []
    y_nocorr = []

    alpha = 1
    beta = 0

    for p in ps:
        counts_corr = amplitude_damping_channel_error(alpha, beta, p)
        counts_nocorr = amplitude_damping_channel_error_nc(alpha, beta, p)

        y_corr.append(success_probability(counts_corr))
        y_nocorr.append(success_probability(counts_nocorr))


    plt.plot(ps, y_corr, marker='o', label='Con correzione (Shor)')
    plt.plot(ps, y_nocorr, marker='o', label='Senza correzione')

    plt.xlabel('Probabilità di errore p')
    plt.ylabel('Probabilità di successo')
    plt.legend()
    plt.grid(True)

    plt.show()



def phase_graph():

    ps = np.arange(0, 1, 0.05)

    y_corr = []
    y_nocorr = []

    alpha = 1
    beta = 0

    for p in ps:
        counts_corr = phase_damping_channel_error(alpha, beta, p)
        counts_nocorr = phase_damping_channel_error_nc(alpha, beta, p)

        y_corr.append(success_probability(counts_corr))
        y_nocorr.append(success_probability(counts_nocorr))


    plt.plot(ps, y_corr, marker='o', label='Con correzione (Shor)')
    plt.plot(ps, y_nocorr, marker='o', label='Senza correzione')

    plt.xlabel('Probabilità di errore p')
    plt.ylabel('Probabilità di successo')
    plt.legend()
    plt.grid(True)

    plt.show()


pauli_graph()