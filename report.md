# FIRST EPOCH EXPERIMENT!

CHUNK_SIZE = 10_000

## Sequential
Phase                  Time (s)    Share
----------------------------------------
I/O                      0.1462    21.0%
Tokenization             0.5162    74.3%
Local counting (Map)     0.0099     1.4%
Merge (Reduce)           0.0229     3.3%
----------------------------------------
Total                    0.6951   100.0%

Chunks processed : 86
Total unique words: 10633

Top 20 words:
  the             7707
  and             4970
  of              4231
  i               4231
  to              3929
  a               2785
  in              2069
  was             2017
  that            1996
  my              1943
  you             1665
  he              1638
  it              1587
  she             1430
  had             1302
  not             1242
  her             1240
  with            1219
  but             1209
  me              1098

## multi-threads
Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.1636    11.3%
Tokenization                  1.2496    86.0%
Local counting (Map)          0.0141     1.0%
Merge (Reduce)                0.0250     1.7%
---------------------------------------------
Total                         1.4524   100.0%

Chunks processed : 86
Total unique words: 10633

Top 20 words:
  the             7707
  and             4970
  of              4231
  i               4231
  to              3929
  a               2785
  in              2069
  was             2017
  that            1996
  my              1943
  you             1665
  he              1638
  it              1587
  she             1430
  had             1302
  not             1242
  her             1240
  with            1219
  but             1209

## multi-process

Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.1579    32.7%
Tokenization                  0.2293    47.5%
Local counting (Map)          0.0737    15.3%
Merge (Reduce)                0.0214     4.4%
---------------------------------------------
Total                         0.4822   100.0%

Chunks processed : 86
Total unique words: 10633

Top 20 words:
  the             7707
  and             4970
  of              4231
  i               4231
  to              3929
  a               2785
  in              2069
  was             2017
  that            1996
  my              1943
  you             1665
  he              1638
  it              1587
  she             1430
  had             1302
  not             1242
  her             1240
  with            1219
  but             1209
  me              1098

## joblib

Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.5753    60.7%
Tokenization                  0.2930    30.9%
Local counting (Map)          0.0574     6.1%
Merge (Reduce)                0.0225     2.4%
---------------------------------------------
Total                         0.9482   100.0%

Chunks processed : 86
Total unique words: 10633

Top 20 words:
  the             7707
  and             4970
  of              4231
  i               4231
  to              3929
  a               2785
  in              2069
  was             2017
  that            1996
  my              1943
  you             1665
  he              1638
  it              1587
  she             1430
  had             1302
  not             1242
  her             1240
  with            1219
  but             1209
  me              1098

