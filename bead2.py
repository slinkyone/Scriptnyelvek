# -*- coding: utf8 -*-
#!/usr/bin/python
import re
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit('Adj meg egy file-t!')

    try:
        input_file = open(sys.argv[1])
    except IOError:
        sys.exit('Nincs ilyen file!')

    out_file1 = open("eloadas.txt", "w")
    out_file2 = open("berlet.txt", "w")

    for line in input_file:
        if re.search('hétfő|kedd|szerda|csütörtök|péntek|szombat|vasárnap', line):
            act_day = re.split('\t\d', line)[0].strip()
            if 'Lumpáciusz Vagabundusz' in line:
                out_file1.write(re.split(': Lumpáciusz Vagabundusz', line)[0].replace('\t', '') + '\n')
            if 'Álomévad bérlet' in line:
                print(re.split('Álomévad bérlet', line)[0])
                out_file2.write(re.split('Álomévad bérlet', line)[0].replace('\t', '').replace('\t', '') + '\n')
        else:
            if 'Lumpáciusz Vagabundusz' in line:
                out_file1.write(act_day + re.split(': Lumpáciusz Vagabundusz', line)[0].replace('\t', '') + '\n')
            if 'Álomévad bérlet' in line:
                a = act_day + ', ' + re.split('Álomévad bérlet', line)[0].replace('\t', '')
                out_file2.write(act_day + ', ' + re.split('Álomévad bérlet', line)[0].replace('\t', '') + '\n')

if __name__ == '__main__':
    main()
