
import sys

def format_output(output):
    res = ''
    line = ''
    counter = 0
    for letter in output:
        line += letter
        counter += 1
        if counter == 5:
            res += line + ' '
            line = ''
            counter = 0
    if line:
        res += line + '\n'
    return res

def encode(text, move):
    letters = [char.upper() for char in text if char.isalpha()]
    encoded = []
    for char in letters:
        ascii_value = ord(char)
        new_value = ascii_value + move
        if new_value > ord('Z'):
            final_value = (new_value - ord('Z')) % 26
            if final_value == 0:
                final_value = 26
            new_value = final_value + ord('A') - 1
        encoded.append(chr(new_value))
    return format_output(''.join(encoded))

args = sys.argv
if len(args) < 2:
    print("Please provide a shift value as a command line argument.")
    sys.exit(1)

shift = int(args[1])
for line in sys.stdin:
    res = encode(line.strip(), shift)
    sys.stdout.write(res)

