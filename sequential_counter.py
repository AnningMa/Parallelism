import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from collections import Counter

from text_utils import tokenize, count_words


# ── I/O ──────────────────────────────────────────────────────────────────────

def extract_text(path: str) -> str:
    """Extract plain text from an EPUB or TXT file."""
    if path.endswith('.txt'):
        with open(path, encoding='utf-8') as f:
            return f.read()
    try:
        book = epub.read_epub(path)
    except Exception as e:
        print(f'[WARN] Skipping {path}: {e}')
        return ''
    parts = []
    for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(item.get_content(), 'html.parser')
        parts.append(soup.get_text())
    return '\n'.join(parts)

def make_chunks(text: str, chunk_size: int = 10_000) -> list[str]:
    """Split text into chunks of approximately chunk_size characters."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# ── Map ───────────────────────────────────────────────────────────────────────

def map_chunk(chunk: str) -> Counter:
    """Tokenize a chunk and return its local word counts."""
    return count_words(tokenize(chunk))

# ── Reduce ────────────────────────────────────────────────────────────────────

def reduce_counts(counters: list[Counter]) -> Counter:
    """Merge a list of local Counters into one global Counter."""
    global_counts = Counter()
    for c in counters:
        global_counts += c
    return global_counts

# ── Pipeline ──────────────────────────────────────────────────────────────────

def count_corpus(epub_paths: list[str], chunk_size: int = 10_000) -> Counter:
    """Sequential MapReduce word-frequency count over a list of EPUB files."""
    local_counts = []

    for path in epub_paths:
        text = extract_text(path)
        for chunk in make_chunks(text, chunk_size):
            local_counts.append(map_chunk(chunk))   # Map

    return reduce_counts(local_counts)              # Reduce

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    import glob
    import time

    paths = glob.glob('data/*.epub') + glob.glob('data/*.txt')
    print(f'Processing {len(paths)} files: {paths}\n')

    chunk_size = 10_000

    # ── Phase 1: I/O ─────────────────────────────────────────────────────────
    t0 = time.perf_counter()
    all_chunks = []
    for path in paths:
        text = extract_text(path)
        all_chunks.extend(make_chunks(text, chunk_size))
    t_io = time.perf_counter() - t0

    # ── Phase 2: Tokenization ─────────────────────────────────────────────────
    t0 = time.perf_counter()
    all_tokens = [tokenize(chunk) for chunk in all_chunks]
    t_tokenize = time.perf_counter() - t0

    # ── Phase 3: Local counting (Map) ─────────────────────────────────────────
    t0 = time.perf_counter()
    local_counts = [count_words(tokens) for tokens in all_tokens]
    t_map = time.perf_counter() - t0

    # ── Phase 4: Merge (Reduce) ───────────────────────────────────────────────
    t0 = time.perf_counter()
    result = reduce_counts(local_counts)
    t_reduce = time.perf_counter() - t0

    t_total = t_io + t_tokenize + t_map + t_reduce

    # ── Results ───────────────────────────────────────────────────────────────
    print(f'{"Phase":<20} {"Time (s)":>10} {"Share":>8}')
    print('-' * 40)
    print(f'{"I/O":<20} {t_io:>10.4f} {t_io/t_total:>8.1%}')
    print(f'{"Tokenization":<20} {t_tokenize:>10.4f} {t_tokenize/t_total:>8.1%}')
    print(f'{"Local counting (Map)":<20} {t_map:>10.4f} {t_map/t_total:>8.1%}')
    print(f'{"Merge (Reduce)":<20} {t_reduce:>10.4f} {t_reduce/t_total:>8.1%}')
    print('-' * 40)
    print(f'{"Total":<20} {t_total:>10.4f} {"100.0%":>8}')

    print(f'\nChunks processed : {len(all_chunks)}')
    print(f'Total unique words: {len(result)}')
    print('\nTop 20 words:')
    for word, freq in result.most_common(20):
        print(f'  {word:15s} {freq}')
