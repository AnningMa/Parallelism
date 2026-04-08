# Lab 4 — Parallel Word Frequency Counter

A word frequency statistics experiment comparing sequential and parallel implementations using the MapReduce paradigm. The goal is to empirically study whether parallelisation actually speeds up a CPU-bound NLP workload, given Python's GIL and inter-process communication overhead.

## Project Structure

```
lab_4/
├── data/                    # Corpus (EPUB + TXT files)
├── text_utils.py            # Shared tokenization and counting functions
├── sequential_counter.py    # Sequential baseline (MapReduce)
├── multithreads_counter.py  # Parallel version using threading
├── multiprocess_counter.py  # Parallel version using multiprocessing
├── joblib_counter.py        # Parallel version using joblib
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
```

NLTK's `punkt_tab` tokenizer data is downloaded automatically on first run.

## Corpus

Place EPUB or TXT files in the `data/` directory. The experiment uses novels from [Project Gutenberg](https://www.gutenberg.org/):

## Tokenization Strategy

All four implementations share the **same tokenization pipeline** defined in `text_utils.py`:

1. NLTK `word_tokenize` — handles punctuation and contractions correctly
2. Lowercase
3. Keep alphabetic tokens only (strip punctuation, numbers)

Consistency across versions is enforced by importing `tokenize` and `count_words` from `text_utils` everywhere.

## Running the Experiments

Each script is self-contained and prints a per-phase timing breakdown.

```bash
python sequential_counter.py
python multithreads_counter.py
python multiprocess_counter.py
python joblib_counter.py
```

## MapReduce Phases and Parallelisation

| Phase | sequential | threads | multiprocess | joblib |
|-------|-----------|---------|--------------|--------|
| I/O | serial | ThreadPoolExecutor | ProcessPoolExecutor | Parallel (loky) |
| Tokenization | serial | ThreadPoolExecutor | ProcessPoolExecutor | Parallel (loky) |
| Local counting (Map) | serial | ThreadPoolExecutor | ProcessPoolExecutor | Parallel (loky) |
| Merge (Reduce) | serial | serial | serial | serial |

## Correctness Verification

All versions must produce identical `Total unique words` counts and top-20 word lists. Any discrepancy indicates a bug in tokenization consistency.

## Key Parameters

Adjust `CHUNK_SIZE` to study the effect of task granularity on overhead and load balancing.

## Expected Findings

- **I/O phase**: threads may help slightly (I/O releases the GIL); processes add serialisation overhead with little gain.
- **Tokenization phase**: CPU-bound; threads are bottlenecked by the GIL; processes can achieve true parallelism but pay inter-process data transfer costs.
- **Merge phase**: always serial; dominates at very large chunk counts.
- **Overall**: parallelisation benefit depends on corpus size, chunk granularity, and number of cores. Overhead can exceed savings on small corpora.
