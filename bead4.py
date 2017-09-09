import csv
import re
import sys
import time
from datetime import datetime, date, time

if len(sys.argv) == 1:
    sys.exit('Adj meg egy file-t!')

input_file = sys.argv[1]


class FlightDataRepo(object):

    def __init__(self, filename):
        try:
            self.input_file = csv.reader(open(filename), delimiter='\t')
        except IOError:
            sys.exit('ErrorCode: 1')
        next(self.input_file)
        self.flight_data = [
            [field.strip() for field in line] for line in self.input_file
        ]

    def jaratszam(self, destination):
        return [flight[0] for flight in self.flight_data
                if flight[1] == destination]

    def lfk(self):
        def format_time(time_string):
            t = time_string.split(':')
            return time(hour=int(t[0]), minute=int(t[1]))

        return [
            (flight[0], int((datetime.combine(date.today(), format_time(flight[3])) - datetime.combine(date.today(), format_time(flight[2]))).total_seconds() / 60))
            for flight in self.flight_data
            if flight[0].startswith('LH') and flight[3]
        ]

menetrend = FlightDataRepo(input_file)
