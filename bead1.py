# -*- coding: utf8 -*-
#!/usr/bin/python
import re
import sys

if len(sys.argv) == 1:
    sys.exit('Adj meg egy file-t!')

try:
    input_file = open(sys.argv[1])
except IOError:
    sys.exit('Nincs ilyen file!')
output_file = open("eredmeny.txt", "w")

products = {}

product_name = None

for line in input_file:
    if not re.search("[0-9]", line):
        product_name = line[:-1]
        products[product_name] = []
    else:
        match = re.search("(.*) (\d*)", line)
        products[product_name].append((int(match.group(2)), match.group(1)))

for product in products:
    max_bid = max(products[product])
    output_file.write("%s -- %s -- %s\n" % (product, max_bid[1], max_bid[0]))
