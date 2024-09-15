import sys
import config
import re
from collections import Counter

# Read file
#file_name = 'Incremento del 0% implica una pérdida de más del 6%'
file_name = sys.argv[1]
file_path = config.base_folder + file_name +'.md'

with open(file_path, 'r', encoding='utf8') as f:
    contents = f.read()

# Lower case
contents_cleared = contents.lower()

# Remove punctuation
punctuation_to_be_removed = '[$@&!¡¿?,.;=()-+%-\[\]/#\:"~\\\\]'
contents_cleared = re.sub(punctuation_to_be_removed, '', contents_cleared)

# get words
all_words = contents_cleared.split()

# compute and sort frequencies
counts = Counter(all_words).most_common()

# create output objects
keys = [t[0] for t in counts]
values = [t[1] for t in counts]

# Cut long key names
keys_chars_lenght = 20
keys = [k[0:keys_chars_lenght-3]+'...' if len(k)>keys_chars_lenght else k for k in keys]

# Adjuts lenght of keys
keys = [k.rjust(keys_chars_lenght) for k in keys]

# print horizontal bar chart
for k, v in zip(keys, values):
    bar_lenght = v
    bar = '|'*bar_lenght
    print(f'{k} {bar}')
