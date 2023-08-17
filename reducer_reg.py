import sys
import re
from collections import defaultdict

def preprocess_word(word):
    return re.sub(r"[,.?!;:()\[\]{}-]", '', word).replace('"', '').replace("'", '')

def main():
    count_dict = defaultdict(int)

    for line_w in sys.stdin:
        line_w = line_w.strip().lower()
        word, count = line_w.split('\t', 1)
        word = preprocess_word(word)
        if re.match(r"^[A-Za-z]+$", word):
            try:
                quant = int(count)
                if word in count_dict:
                    count_dict[word] += quant
                else:
                    count_dict[word] = quant
            except ValueError:
                continue
    count_ord = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)

    print(f"Total unique words: {len(count_ord)}")
    print(f"Top 10 words: {list(count_ord)[:10]}")

    f_min = count_ord[-1][1]
    f_max = count_ord[0][1]
    s_interval = (f_max - f_min) / 10
    hist = [0] * 10

    for _, f in count_ord:
        ind_interval = int((f - f_min) // s_interval)
        ind_interval = min(ind_interval, 10 - 1)
        hist[ind_interval] += 1

    for x, c_freq in enumerate(hist):
        start_int = int(f_min + x * s_interval)
        end_int = int(f_min + (x + 1) * s_interval - 1)
        print(f"Interval {x+1} ({start_int}-{end_int}) - {c_freq} words")

if __name__ == "__main__":
    main()
