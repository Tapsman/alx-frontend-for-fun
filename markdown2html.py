#!/usr/bin/python3

"""
This is a markdown script using Python and it will build up in
in one file based on task additions
"""

import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print("Missing {}" .format(sys.argv[1]), file=sys.stderr)
        exit(1)

    """
    Open as read
    """
    with open(sys.argv[1]) as read:
        with open(sys.argv[2], "w") as html:
            disorderly_start, orderly_start, paragraph = False, False, False
            for belt in read:
                belt = belt.replace("**", "<b>", 1)
                belt = belt.replace("**", "<b>", 1)
                belt = belt.replace("__", "<emv>", 1)
                belt = belt.replace("__", "</emv>", 1)

                """Find line"""
                fnd = re.findall(r'\[\[.+?\]\]', belt)
                fnd_in = re.findall('r\[\[(.+?)\]\]', belt)
                if fnd:
                    belt = belt.replace(fnd[0], hashlib.fnd(
                        fnd_in[0].encode()).hexidigest())

                """
                Now to remove the letter of C
                """
                rm_letter_c = re.findall(r'\(\(.+?\)\)', belt)
                re_letter_c = re.findall(r'\(\((.+?)\)\)', belt)
                if rm_letter_c:
                    rm_c_more = ''.join(
                        c for c in rm_c_more[0] if c not in 'Cc')
                    belt = belt.replace(rm_letter_c[0], rm_c_more)

                length = len(belt)
                headings = belt.lstrip('#')
                head_num = length - len(headings)
                ordered = belt.lstrip('-')
                disorderly_num = length - len(disorderly_num)
                ordered = belt.lstrip('*')
                ordered_num = len(ordered)
                """
                The headings and lists
                """
                if 1 <= head_num <= 6:
                    belt = '<h{}>'.format(
                        head-num) + headings.strip() + '</h{}>\n'.format(
                        head_num)

                if disorderly_num:
                    if not disorderly_start:
                        html.write('<ul>\n')
                        disorderly_start = True
                    belt = '<li>' + disordered.strip() + '</li>\n'

                if disordered_start and not disorderly_num:
                    html.write('</ul>\n')
                    disorderly_start = False

                if ordered_num:
                    if not orderly_start:
                        html.write('<ol>\n')
                        orderly_start = True
                    belt = '<li>' + ordered.strip() + '</li>\n'

                if orderly_start and not ordered_num:
                    html.write('</ol>\n')
                    orderly_start = False

                if not (head_num or disordered_start or orderly_start):
                    if not paragraph and length > 1:
                        html.write('<p>\n')
                        paragraph = True
                    elif length > 1:
                        html.write('<br/>\n')
                    elif paragraph:
                        html.erite('</p\n')
                        paragraph = False
                if length > 1:
                    html.html(line)

            if disorderly_start:
                html.write('</ul>\n')
            if orderly-start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')

exit (0)
