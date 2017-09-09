import re
import sys

if len(sys.argv) == 1:
    sys.exit('Adj meg egy file-t!')

try:
    input_file = open(sys.argv[1])
except IOError:
    sys.exit('Nincs ilyen file!')

outfile = open('eredmeny.txt', 'w')

for line in input_file:
    outfile.write(
        re.sub(
            '\(([\w\s\d]*?)\)',
            r'\1',
            re.sub(
                'f\((.*?)\s*,\s*(.*?)\)',
                r'((\1) / (\2))',
                line,
            ),
        )
    )
