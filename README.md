# Quantum Error Correction Library – Shor Code

Libreria Python per la simulazione della **quantum error correction** basata sul **codice di Shor a 9 qubit**. Il progetto fornisce strumenti modulari per costruire, trasmettere e decodificare circuiti quantistici soggetti a rumore, con particolare attenzione alla separazione tra encoding, canale e decoding.

La libreria è orientata a uso didattico e di ricerca ed è progettata per essere facilmente estendibile.

---

## Struttura del progetto

La libreria è organizzata in quattro moduli principali.

### 1. Encoder

Il modulo `encoder` implementa l’**encoding di Shor a nove qubit**.

Funzionalità:
- Riceve in input un **circuito quantistico iniziale** o uno stato logico su singolo qubit.
- Costruisce il circuito di encoding secondo il codice di Shor.
- Restituisce il circuito codificato pronto per la trasmissione.

---

### 2. Channel Simulator

Il modulo `channel_simulator` permette di simulare diversi **canali quantistici**, applicabili al circuito codificato.

Canali disponibili:
- **Canale ideale** (assenza di rumore).
- **Canale con errori di Pauli ideali** (X, Y, Z stocastici).
- **Canale di depolarizzazione**.
- **Canale di amplitude damping**.
- **Canale di phase damping**.

Ogni canale può essere parametrizzato tramite probabilità di errore o coefficienti di rumore.

---

### 3. Decoder

Il modulo `decoder` gestisce la fase di decoding del circuito ricevuto.

Modalità supportate:
- **Decoding con correzione di Shor**, con misure di sindrome e operazioni correttive.
- **Decoding banale**, senza alcuna correzione, usato come riferimento.

---

### 4. Circuit Builder

Il modulo `circuit_builder` integra le funzionalità degli altri moduli e consente di costruire **circuiti completi end-to-end**.

Funzionalità:
- Inizializzazione del qubit logico a partire da **valori arbitrari dello stato iniziale**.
- Applicazione automatica dell’encoding di Shor.
- Inserimento di un canale rumoroso con **probabilità di errore specificate dall’utente**.
- Scelta della strategia di decoding (con o senza correzione).
- Produzione di un unico circuito quantistico completo, pronto per la simulazione.

Questo modulo rappresenta il punto di ingresso principale per esperimenti e benchmark.

---

## Workflow tipico

1. Definizione dello stato iniziale del qubit logico.
2. Costruzione automatica del circuito completo tramite `circuit_builder`.
3. Simulazione del circuito su backend quantistico o simulatore.
4. Analisi dei risultati con e senza correzione degli errori.

---

## Requisiti

- Python 3.x  
- Framework di simulazione quantistica compatibile (ad esempio Qiskit, se utilizzato dal progetto)

I requisiti dettagliati sono riportati in `requirements.txt`.

---

## Obiettivi del progetto

- Studiare il comportamento del codice di Shor in presenza di diversi modelli di rumore.
- Confrontare trasmissioni corrette e non corrette.
- Fornire una base modulare per l’estensione verso altri codici di quantum error correction.
- Facilitare esperimenti riproducibili e configurabili.

---

## Stato del progetto

Il progetto è in sviluppo ed è focalizzato sulla chiarezza concettuale e sulla correttezza teorica. Non è ottimizzato per l’esecuzione su hardware quantistico reale.

---

## Licenza

Specificare la licenza nel file `LICENSE`.
