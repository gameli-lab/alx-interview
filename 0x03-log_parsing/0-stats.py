#!/usr/bin/python3
'''
    0-stats.py
    Script that parses Apache log files
    and prints various statistics.

    Usage: ./0-stats.py < apache_logs.txt'''
import re
import signal
import sys

'''Regex pattern to match the log format'''
pattern = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
        r' - '
        r'\[(?P<date>.*?)\]'
        r' "GET /projects/260 HTTP/1\.1"'
        r' (?P<status>\d{3})'
        r' (?P<size>\d+)'
        )

'''Initialize metrics'''

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


'''Register the signal handler for CTRL + C'''
signal.signal(signal.SIGINT, signal_handler)

''' Process each line from stdin'''
try:
    for line in sys.stdin:
        match = pattern.match(line.strip())
        if match:
            size = int(match.group('size'))
            status = int(match.group('status'))

            total_size += size
            if status in status_codes:
                status_codes[status] += 1

            line_count += 1
            if line_count == 10:
                print_stats()
                line_count = 0
except Exception as e:
    print(f"Error: {e}")

''' Print final statistics after the loop ends'''
print_stats()
