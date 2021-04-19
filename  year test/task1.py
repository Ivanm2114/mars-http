import sys

for line in sys.stdin:
    if line:

        while ('AX' in line) or ('BXX' in line) or ('CXXX' in line):
            line = line.replace('AX', 'B', 1)
            line = line.replace('BXX', 'C', 1)
            line = line.replace('CXXX', 'A', 1)
        print(line.strip())
