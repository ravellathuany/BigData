import sys

for line_w in sys.stdin:
    line_w = line_w.strip()
    words = line_w.split()
    for w in words:
        print(f'{w}\t1')