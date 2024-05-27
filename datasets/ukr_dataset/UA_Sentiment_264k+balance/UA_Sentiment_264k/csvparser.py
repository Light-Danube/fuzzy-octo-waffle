import random
from tqdm import tqdm


SRC_CSV = "UA_264008.csv"
TRGT_CSV = "UA_16k_balanced.csv"
TRGT_TEST_CSV = "UA_16k_balanced_2k_test.csv"
TRGT_PROBE_CSV = "UA_16k_balanced_2k_probe.csv"
SIZE_OF_DATASET = 16000
SIZE_OF_TEST = 2000
SIZE_OF_PROBE = 2000

SRC_DATA = {}
SRC_SIZE = 0
done_list = []


with open(SRC_CSV) as src:
    while 1:
        line = src.readline()
        if not line:
            break
        data = line.split(";")
        if not data:
            continue
        keyword = data[0]
        value = data[1].replace("\n", "")
        SRC_DATA[keyword] = value

if SRC_SIZE := len(SRC_DATA):
    print(f"{SRC_SIZE} items are loaded.")
else:
    print("Failed to load from source. Exit.")
    exit(1)

prev_trgt = 0
prev_test = 0
prev_probe = 0


print("Start to make main Dataset.")
readlines = tqdm(desc="Read lines: ")
progress = tqdm(desc="Written lines: ", total=SIZE_OF_DATASET)
counter = 0
with open(TRGT_CSV, "w", encoding="UTF-8") as trgt:
    print("word;pos_nеg", file=trgt)
    while counter < SIZE_OF_DATASET:
        readlines.update()
        index = random.randint(0, SRC_SIZE - 1)
        if index not in done_list:
            keyword = list(SRC_DATA.keys())[index]
            value = SRC_DATA[keyword]
            if value != prev_trgt:
                print(f"{keyword.replace(' ;', ';')};{value}", file=trgt)
                prev_trgt = value
                done_list.append(index)
                progress.update()
                counter += 1

readlines.close()
progress.close()

print("Start to make probe Dataset.")
readlines = tqdm(desc="Read lines: ")
progress = tqdm(desc="Written lines: ", total=SIZE_OF_PROBE)
counter = 0
with open(TRGT_PROBE_CSV, "w", encoding="UTF-8") as trgt:
    print("word;pos_nеg", file=trgt)
    while counter < SIZE_OF_PROBE:
        readlines.update()
        index = random.randint(0, SRC_SIZE - 1)
        if index not in done_list:
            keyword = list(SRC_DATA.keys())[index]
            value = SRC_DATA[keyword]
            if value != prev_trgt:
                print(f"{keyword.replace(' ;', ';')};{value}", file=trgt)
                prev_trgt = value
                done_list.append(index)
                progress.update()
                counter += 1
readlines.close()
progress.close()

print("Start to make test Dataset.")
readlines = tqdm(desc="Read lines: ")
progress = tqdm(desc="Written lines: ", total=SIZE_OF_TEST)
counter = 0
with open(TRGT_TEST_CSV, "w", encoding="UTF-8") as trgt:
    print("word;pos_nеg", file=trgt)
    while counter < SIZE_OF_TEST:
        readlines.update()
        index = random.randint(0, SRC_SIZE - 1)
        if index not in done_list:
            keyword = list(SRC_DATA.keys())[index]
            value = SRC_DATA[keyword]
            if value != prev_trgt:
                print(f"{keyword.replace(' ;', ';')};{value}", file=trgt)
                prev_trgt = value
                done_list.append(index)
                progress.update()
                counter += 1

readlines.close()
progress.close()

print("Job is done!")
