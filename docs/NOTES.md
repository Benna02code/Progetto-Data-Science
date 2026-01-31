# Project Notes

## GUIDELINE NOTES (HOW TO USE IT)



Questo file contiene appunti e riflessioni sulle scelte fatte durante il progetto.  
Funziona come un **taccuino di progetto** per tenere traccia delle decisioni metodologiche,
del flusso mentale seguito e dei concetti importanti da ricordare (anche in vista dell’orale).

Non è un documento formale e non è destinato alla consegna finale.

Per creare la struttura date database su ogni computer è sufficiente scaricare la repo e runnare schema.sql per la struttura e 01_populate_db.ipynb per il popolamento già diviso in train val e test.
---


## GUIDELINE NOTES (HOW TO USE IT)
Per utilizzare git al meglio seguire gli step:
1. Nel terminale dentro la repo usare comando: git pull (per scaricare eventuali aggiornamenti)
2. git status (controllo)
3. Una volta effettuate modifiche consolidate fare commit con messaggio esautivo e push


Per creare la struttura date database su ogni computer è sufficiente scaricare la repo e runnare schema.sql per la struttura e 01_populate_db.ipynb per il popolamento già diviso in train val e test.

## Dataset structure

- Il dataset utilizzato è suddiviso in modo fittizio tra train val e test. Di fatto ci sono le stesse immagini copiate e incollate nelle tre stratificazioni.
Dobbiamo creare uno split nostro corretto e riproducibile

Mettiamo utte le immagini insieme e poi le suddividiamo in train (70%), val (15%) e test (15%).
The split was verified to preserve class proportions.

### Numero di immagini per split

| Split | Numero immagini |
|------|-----------------|
| Train | 1768 |
| Validation | 379 |
| Test | 380 |

### Distribuzione classi per split

| Split | Cardboard | Glass | Metal | Paper | Plastic | Trash |
|------|-----------|-------|-------|-------|---------|-------|
| Train | 282 | 350 | 287 | 416 | 337 | 96 |
| Validation | 61 | 75 | 61 | 89 | 72 | 21 |
| Test | 60 | 76 | 62 | 89 | 73 | 20 |

Lo split risulta bilanciato e coerente tra i diversi sottoinsiemi senza duplicazioni.

- Il problema è un **supervised learning multi-classe**:
  - ogni immagine ha una classe associata (es. cardboard, glass, plastic, ecc.).

- Le classi **non sono bilanciate tra loro**:
  - ad esempio la classe *trash* è sotto-rappresentata.
  - questo aspetto va considerato sia in fase di analisi che in fase di valutazione dei modelli
    (possibili effetti su accuracy e confusion matrix).

---

## Data flow (flusso dei dati)

Il flusso dei dati nel progetto è pensato per essere **chiaro, riproducibile e scalabile**.

### Struttura generale

- Le **immagini** sono memorizzate nel **filesystem** (cartelle locali).
- I **metadati** sono memorizzati in un **database PostgreSQL**.

Il database contiene informazioni come:
- dove si trova fisicamente l’immagine (filepath)
- a quale classe appartiene (label)
- a quale split appartiene (train / validation / test / external)
- l’origine del dato (dataset originale o immagini scattate da noi)

I modelli:
1. interrogano il database per ottenere i percorsi delle immagini corrette
2. caricano le immagini dal filesystem
3. applicano preprocessing e training

Questa separazione migliora:
- la gestione dei dati
- la riproducibilità degli esperimenti
- la chiarezza del progetto (soprattutto da spiegare all’orale)

---

## Preprocessing delle immagini (on the fly, senza salvarle)

Una volta selezionate le immagini corrette in base allo split, vengono applicate alcune trasformazioni.

Queste operazioni **NON cambiano l’etichetta** dell’immagine, ma influenzano
la qualità del training del modello.

### Resize
- Tutte le immagini vengono ridimensionate a una dimensione standard
  (es. 128×128 o 224×224).
- Serve perché i modelli (soprattutto le CNN) richiedono input di dimensione fissa.

### Normalizzazione dei pixel
- I pixel delle immagini vengono normalizzati.
- Tipicamente si passa da valori [0, 255] a [0, 1] oppure si applica una standardizzazione.
- Questo aiuta il modello a convergere più velocemente e in modo più stabile.

### Data augmentation (solo su training set)
La **data augmentation** consiste nell’applicare trasformazioni casuali alle immagini
per creare nuove versioni “simili” delle immagini originali.

Esempi:
- rotazioni leggere
- flip orizzontali
- piccoli zoom
- variazioni di luminosità

Scopo:
- aumentare la varietà dei dati di training
- ridurre overfitting
- migliorare la capacità di generalizzazione del modello

⚠️ Importante:
- la data augmentation viene applicata **solo sul training set**
- NON deve essere applicata su validation o test set,
  per non falsare la valutazione delle prestazioni.

---

## Database design (draft)

Il database PostgreSQL viene usato per memorizzare **solo i metadati**, non le immagini.
Tutti i percorsi salvati nel DB sono relativi alla root del repository.

### Metadati pianificati

- `image_id`: identificativo univoco dell’immagine
- `filepath`: percorso relativo del file immagine
- `label`: classe dell’oggetto (garbage category)
- `split`: appartenenza allo split (train / validation / test / external)
- `source`: origine del dato (raw dataset / immagini personali)

Le immagini **non vengono memorizzate nel database**:
- sono troppo pesanti
- il filesystem è più adatto allo storage dei file binari
- il database resta leggero e gestibile

---

## Oral exam – riassunto mentale

Se dovessimo riassumere il progetto a voce:

- Abbiamo utilizzato un dataset di immagini già supervisionato e suddiviso in train, validation e test.
- La suddivisione originale è stata mantenuta per garantire un confronto corretto tra i modelli.
- Il problema è una classificazione multi-classe di oggetti di rifiuto.
- I dati sono gestiti tramite un database PostgreSQL che contiene solo metadati.
- Le immagini sono caricate dal filesystem sulla base delle informazioni presenti nel database.
- Sono stati confrontati modelli di complessità crescente, fino a modelli deep learning.
