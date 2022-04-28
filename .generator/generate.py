# Generate boiler plate code for Python 101 git workshop.
# Use users exported from Moodle as .csv.

import csv
import sys
from unidecode import unidecode

if len(sys.argv) != 2:
    print("Usage: python3 generate.py students.csv")
    exit(1)

def generate_test_code(function_call, username, full_name):
    test_code = (
        f"\ndef test_{username}():\n"
        f"\tyour_name = {function_call}\n"
        f"\tif your_name == 'missing':\n"
        f"\t\treturn\n"
        f"\tassert your_name == '{full_name}', 'Did you spell your name correctly?'\n"
    )
    return test_code

def generate_code(username):
    return (f'greet_{username}()', f"def greet_{username}():\n\treturn 'missing'\n\n")

with open(sys.argv[1]) as f, open('collaboration.py', 'w') as colab, open('test_collaboration.py', 'w') as test:
    warning = (
        '# This file is autogenerated. Only students should edit.\n'
        '# Add your full name from Moodle to your function.\n\n'
    )
    defitions = ''
    main_body = "if __name__ == '__main__':\n\tstudents = []\n"

    test_cases = (
        '# This file is autogenerated. Do not edit.\n'
        '# -*- coding: utf-8 -*-\n\n'
        'from collaboration import *\n'
    )

    reader = csv.reader(f, delimiter=',')
    # Skip header row
    next(reader, None)
    for student in reader:
        full_name = student[0] + ' ' + student[1]
        username = unidecode(full_name.lower().replace('-', '_').replace(' ', '_'))

        function_call, code = generate_code(username)
        defitions += code
        main_body += '\tstudents += [' + function_call + ']\n'

        test_cases += generate_test_code(function_call, username, full_name)

    main_body += (
        "\tnot_missing = lambda i: i != 'missing'\n\n"
        "\tprint('Here are some awesome people:\\n')\n"
        "\tprint('\\n'.join(filter(not_missing, students)))\n"
        "\tprint('\\nKudos to you!')\n"
    )

    colab.write(warning)
    colab.write(defitions)
    colab.write(main_body)

    test.write(test_cases)
