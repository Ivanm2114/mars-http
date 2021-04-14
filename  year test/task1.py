import sys

for line in sys.stdin:
    if line:
        while 'AAAAA' in line:
            line = line.replace('YYY', 'A',1)
            line = line.replace('AAA', 'Y',1)
        print(line)
