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


# SECOND EXPERIMENT!
CHUNK_SIZE = 10_000 （no change）
CORPUS: 13MB, 21 files

## sequential
Phase                  Time (s)    Share
----------------------------------------
I/O                      0.2029     2.5%
Tokenization             6.5646    81.5%
Local counting (Map)     0.1560     1.9%
Merge (Reduce)           1.1268    14.0%
----------------------------------------
Total                    8.0502   100.0%

Chunks processed : 1271
Total unique words: 42446

Top 20 words:
  the             141206
  and             100252
  of              75430
  to              51617
  a               36629
  in              35547
  i               34425
  that            30744
  he              27493
  it              23791
  his             22355
  was             20799
  for             20514
  not             19409
  with            18806
  you             17966
  is              17550
  be              16826
  as              15480
  but             15103

## multi-threads

Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.2104     2.2%
Tokenization                  7.9783    82.9%
Local counting (Map)          0.2316     2.4%
Merge (Reduce)                1.2067    12.5%
---------------------------------------------
Total                         9.6270   100.0%

Chunks processed : 1271
Total unique words: 42446

Top 20 words:
  the             141206
  and             100252
  of              75430
  to              51617
  a               36629
  in              35547
  i               34425
  that            30744
  he              27493
  it              23791
  his             22355
  was             20799
  for             20514
  not             19409
  with            18806
  you             17966
  is                17550
  be              16826
  as              15480
  but             15103

## multi-process
Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.1543     3.6%
Tokenization                  2.1233    50.1%
Local counting (Map)          0.9654    22.8%
Merge (Reduce)                0.9950    23.5%
---------------------------------------------
Total                         4.2380   100.0%

Chunks processed : 1271
Total unique words: 42446

Top 20 words:
  the             141206
  and             100252
  of              75430
  to              51617
  a               36629
  in              35547
  i               34425
  that            30744
  he              27493
  it              23791
  his             22355
  was             20799
  for             20514
  not             19409
  with            18806
  you             17966
  is              17550
  be              16826
  as              15480
  but             15103

## joblib

Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.6515    14.7%
Tokenization                  2.3218    52.4%
Local counting (Map)          0.4790    10.8%
Merge (Reduce)                0.9755    22.0%
---------------------------------------------
Total                         4.4279   100.0%

Chunks processed : 1271
Total unique words: 42446

Top 20 words:
  the             141206
  and             100252
  of              75430
  to              51617
  a               36629
  in              35547
  i               34425
  that            30744
  he              27493
  it              23791
  his             22355
  was             20799
  for             20514
  not             19409
  with            18806
  you             17966
  is              17550
  be              16826
  as              15480
  but             15103

# THIRD EXPERIMENT

Chunk Size = 100000
Corpus no change

预期：

版本	预期变化
串行	变化不大，纯计算，没有调度开销
多线程	略有改善，但 GIL 仍是瓶颈
多进程	改善最明显——chunk 大了，每次跨进程传输的数据变大但次数大幅减少；进程启动开销占比下降
joblib	与多进程类似，loky 后端也从中受益

## sequential 
Phase                  Time (s)    Share
----------------------------------------
I/O                      0.2165     3.2%
Tokenization             6.2446    92.1%
Local counting (Map)     0.1338     2.0%
Merge (Reduce)           0.1856     2.7%
----------------------------------------
Total                    6.7806   100.0%

Chunks processed : 138
Total unique words: 42032

Top 20 words:
  the             141233
  and             100267
  of              75439
  to              51622
  a               36609
  in              35551
  i               34411
  that            30754
  he              27475
  it              23793
  his             22357
  was             20802
  for             20517
  not             19412
  with            18812
  you             17970
  is              17551
  be              16825
  as              15479
  but             15106

chunk_size 变大后，循环次数从 1300 次降到 130 次，减少了以下开销：

1. 列表操作次数减少

make_chunks 创建的列表更短，local_counts.append() 调用次数少了 10 倍。

2. Counter 对象的创建和 GC 开销减少

每个 chunk 都会创建一个新的 Counter 对象。1300 个 vs 130 个，Python 的内存分配和垃圾回收压力直接减少了 10 倍。

3. reduce_counts 的合并次数减少


  ## multi-threads
  Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.2064     2.4%
Tokenization                  7.9335    92.9%
Local counting (Map)          0.1998     2.3%
Merge (Reduce)                0.1988     2.3%
---------------------------------------------
Total                         8.5385   100.0%

Chunks processed : 138
Total unique words: 42032

Top 20 words:
  the             141233
  and             100267
  of              75439
  to              51622
  a               36609
  in              35551
  i               34411
  that            30754
  he              27475
  it              23793
  his             22357
  was             20802
  for             20517
  not             19412
  with            18812
  you             17970
  is              17551
  be              16825
  as              15479
  but             15106

## multi-process
Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.1631     5.8%
Tokenization                  2.0311    72.1%
Local counting (Map)          0.4791    17.0%
Merge (Reduce)                0.1450     5.1%
---------------------------------------------
Total                         2.8184   100.0%

Chunks processed : 138
Total unique words: 42032

Top 20 words:
  the             141233
  and             100267
  of              75439
  to              51622
  a               36609
  in              35551
  i               34411
  that            30754
  he              27475
  it              23793
  his             22357
  was             20802
  for             20517
  not             19412
  with            18812
  you             17970
  is              17551
  be              16825
  as              15479
  but             15106

## joblib
Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.7861    24.5%
Tokenization                  1.9867    61.9%
Local counting (Map)          0.2864     8.9%
Merge (Reduce)                0.1482     4.6%
---------------------------------------------
Total                         3.2074   100.0%

Chunks processed : 138
Total unique words: 42032

Top 20 words:
  the             141233
  and             100267
  of              75439
  to              51622
  a               36609
  in              35551
  i               34411
  that            30754
  he              27475
  it              23793
  his             22357
  was             20802
  for             20517
  not             19412
  with            18812
  you             17970
  is              17551
  be              16825
  as              15479
  but             15106

进程池启动一次大约耗时 50–200ms（取决于机器）。你的代码有 3 个并行阶段（I/O、Tokenization、Local counting 三个阶段各自独立创建和销毁进程池），所以 multiprocess 每次运行多付出约 3 × 启动开销。

关键差异在于 Parallel 的默认行为：
Parallel 默认使用 prefer=None，在任务数量少时（你只有 ~20 个文件）会自动判断是否值得开多进程，有时会降级到串行执行（n_jobs 被忽略）。而 ProcessPoolExecutor.map 始终并行。

# FORTH EXPERIMENT
Corpus size: 40MB
Chunks = 100000
大幅度扩大corpus size

## sequential 
Phase                  Time (s)    Share
----------------------------------------
I/O                      0.3549     1.5%
Tokenization            22.2214    92.3%
Local counting (Map)     0.5412     2.2%
Merge (Reduce)           0.9646     4.0%
----------------------------------------
Total                   24.0820   100.0%

Chunks processed : 435
Total unique words: 67310

Top 20 words:
  the             422032
  and             278159
  of              211929
  to              190271
  a               139560
  i               122928
  in              116886
  he              107742
  that            99239
  it              85800
  was             84716
  his             80852
  you             68557
  with            63542
  not             58333
  for             58163
  had             54568
  as              54567
  is              52337
  her             51610

## multi-threads
Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.3856     1.4%
Tokenization                 25.6822    90.7%
Local counting (Map)          0.7153     2.5%
Merge (Reduce)                1.5427     5.4%
---------------------------------------------
Total                        28.3257   100.0%

Chunks processed : 435
Total unique words: 67310

Top 20 words:
  the             422032
  and             278159
  of              211929
  to              190271
  a               139560
  i               122928
  in              116886
  he              107742
  that            99239
  it              85800
  was             84716
  his             80852
  you             68557
  with            63542
  not             58333
  for             58163
  had             54568
  as              54567
  is              52337
  her             51610

## multi-process
Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.2596     2.6%
Tokenization                  7.1506    70.5%
Local counting (Map)          1.9332    19.1%
Merge (Reduce)                0.7991     7.9%
---------------------------------------------
Total                        10.1425   100.0%

Chunks processed : 435
Total unique words: 67310

Top 20 words:
  the             422032
  and             278159
  of              211929
  to              190271
  a               139560
  i               122928
  in              116886
  he              107742
  that            99239
  it              85800
  was             84716
  his             80852
  you             68557
  with            63542
  not             58333
  for             58163
  had             54568
  as              54567
  is              52337
  her             51610

  ## jiblib
  Phase                       Time (s)    Share
---------------------------------------------
I/O                           0.7170     7.9%
Tokenization                  6.6066    72.6%
Local counting (Map)          1.0589    11.6%
Merge (Reduce)                0.7227     7.9%
---------------------------------------------
Total                         9.1052   100.0%

Chunks processed : 435
Total unique words: 67310

Top 20 words:
  the             422032
  and             278159
  of              211929
  to              190271
  a               139560
  i               122928
  in              116886
  he              107742
  that            99239
  it              85800
  was             84716
  his             80852
  you             68557
  with            63542
  not             58333
  for             58163
  had             54568
  as              54567
  is              52337
  her             51610

进程池复用。Tokenization 计时中包含了一次完整的进程池启动开销。

# FIFTH EXPERIMENT

