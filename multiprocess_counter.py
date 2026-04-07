import glob
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

from sequential_counter import extract_text, make_chunks, reduce_counts
from text_utils import tokenize, count_words


CHUNK_SIZE = 10_000
N_WORKERS  = 4


# ── Process workers (must be module-level to be picklable) ───────────────────

def load_file(path: str) -> list[str]:
    """I/O worker: read one file and return its chunks."""
    return make_chunks(extract_text(path), CHUNK_SIZE)


def map_chunk(chunk: str) -> Counter:
    """Map worker: tokenize + count one chunk (two steps kept together
    to minimise inter-process data transfer)."""
    return count_words(tokenize(chunk))


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    paths = glob.glob('data/*.epub') + glob.glob('data/*.txt')
    print(f'Processing {len(paths)} files: {paths}\n')

    # ── Phase 1: I/O (parallel across files) ─────────────────────────────────
    t0 = time.perf_counter()
    all_chunks = []
    with ProcessPoolExecutor(max_workers=N_WORKERS) as pool:
        for chunks in pool.map(load_file, paths):
            all_chunks.extend(chunks)
    t_io = time.perf_counter() - t0

    # ── Phase 2: Tokenization (parallel across chunks) ────────────────────────
    t0 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=N_WORKERS) as pool:
        all_tokens = list(pool.map(tokenize, all_chunks))
    t_tokenize = time.perf_counter() - t0

    # ── Phase 3: Local counting / Map (parallel across chunks) ────────────────
    t0 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=N_WORKERS) as pool:
        local_counts = list(pool.map(count_words, all_tokens))
    t_map = time.perf_counter() - t0

    # ── Phase 4: Merge / Reduce (sequential — single global result) ───────────
    t0 = time.perf_counter()
    result = reduce_counts(local_counts)
    t_reduce = time.perf_counter() - t0

    t_total = t_io + t_tokenize + t_map + t_reduce

    # ── Timing report ─────────────────────────────────────────────────────────
    print(f'{"Phase":<25} {"Time (s)":>10} {"Share":>8}')
    print('-' * 45)
    print(f'{"I/O":<25} {t_io:>10.4f} {t_io/t_total:>8.1%}')
    print(f'{"Tokenization":<25} {t_tokenize:>10.4f} {t_tokenize/t_total:>8.1%}')
    print(f'{"Local counting (Map)":<25} {t_map:>10.4f} {t_map/t_total:>8.1%}')
    print(f'{"Merge (Reduce)":<25} {t_reduce:>10.4f} {t_reduce/t_total:>8.1%}')
    print('-' * 45)
    print(f'{"Total":<25} {t_total:>10.4f} {"100.0%":>8}')

    print(f'\nChunks processed : {len(all_chunks)}')
    print(f'Total unique words: {len(result)}')
    print('\nTop 20 words:')
    for word, freq in result.most_common(20):
        print(f'  {word:15s} {freq}')
