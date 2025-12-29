# Quantum Error Correction Library – Shor Code

Libreria Python per la simulazione della **quantum error correction** basata sul **codice di Shor a 9 qubit**. Il progetto fornisce strumenti modulari per l’encoding, la simulazione di canali rumorosi e il decoding con o senza correzione degli errori.

La libreria è pensata per scopi di ricerca, didattici e di sperimentazione, ed è progettata per essere estendibile ad altri codici o modelli di rumore.

---

## Struttura del progetto

La libreria è suddivisa in tre moduli principali:

### 1. Encoder

Il modulo `encoder` implementa l’**encoding di Shor a nove qubit**.

Funzionalità principali:
- Accetta in input un **circuito quantistico iniziale** (stato logico su un singolo qubit).
- Costruisce automaticamente il circuito di encoding secondo il codice di Shor.
- Restituisce il circuito codificato pronto per essere inviato a un canale rumoroso.

L’encoder isola completamente la logica di codifica, consentendo di lavorare in modo trasparente con circuiti arbitrari.

---

### 2. Channel Simulator

Il modulo `channel_simulator` consente di simulare diversi **modelli di canale quantistico**, applicabili al circuito codificato.

Canali supportati:
- **Canale ideale**: nessun errore applicato.
- **Canale con errori di Pauli ideali**: applicazione stocastica di errori X, Y e Z.
- **Canale di depolarizzazione**: simulazione della perdita di informazione tramite rumore isotropo.
- **Canale di amplitude damping**: modellazione del decadimento energetico.
- **Canale di phase damping**: simulazione della decoerenza di fase.

Il simulatore è progettato per permettere l’aggiunta semplice di nuovi canali o modelli di rumore.

---

### 3. Decoder

Il modulo `decoder` gestisce la fase finale del processo.

Modalità di decoding disponibili:
- **Decoding con correzione di Shor**: applica la procedura completa di rilevazione e correzione degli errori.
- **Decoding banale**: esegue il decoding senza alcuna correzione, utile come baseline di confronto.

Il decoder permette di valutare l’efficacia del codice confrontando i risultati con e senza correzione.

---

## Workflow tipico

1. Definizione di un circuito quantistico iniziale.
2. Encoding tramite il modulo `encoder`.
3. Applicazione di un canale rumoroso tramite `channel_simulator`.
4. Decoding finale con o senza correzione tramite `decoder`.
5. Analisi dei risultati.

---

## Requisiti

- Python 3.x  
- Framework di simulazione quantistica compatibile (es. Qiskit, se utilizzato dal progetto)

I requisiti specifici sono elencati nel file `requirements.txt`.

---

## Obiettivi del progetto

- Fornire una base modulare per lo studio della quantum error correction.
- Permettere il confronto tra diversi modelli di rumore.
- Valutare l’efficacia del codice di Shor in scenari realistici.
- Facilitare estensioni verso altri codici di correzione quantistica.

---

## Stato del progetto

Il progetto è in sviluppo e focalizzato sulla correttezza concettuale e sulla chiarezza strutturale. Non è ottimizzato per l’esecuzione su hardware quantistico reale.

---

## Licenza

Specificare la licenza nel file `LICENSE`.

