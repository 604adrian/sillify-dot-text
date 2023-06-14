import sys
import re
import subprocess
from collections import defaultdict
from random import choice
from data import common_nouns, common_adjectives, silly_nouns, silly_adjectives

def replace_words(match):
    word = match.group(0).lower()
    if word in common_nouns:
        return choice(list(silly_nouns)).upper()
    elif word in common_adjectives:
        return toggle_case(choice(list(silly_adjectives)))
    else:
        return match.group(0)

def toggle_case(word):
    toggled_word = ""
    for i, c in enumerate(word):
        if i % 2 == 0:
            toggled_word += c.upper()
        else:
            toggled_word += c.lower()
    return toggled_word

def replace_text(file_name):
    with open(file_name, 'r') as file:
        text = file.read()

    pattern = r'\b\w+\b'
    replaced_text = re.sub(pattern, replace_words, text, flags=re.IGNORECASE)
    return replaced_text

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python text_replacement.py <file>")
        sys.exit(1)

    file_name = sys.argv[1]
    output = replace_text(file_name)

    # Pipe output to less window
    less_process = subprocess.Popen(['less'], stdin=subprocess.PIPE)
    less_process.communicate(input=output.encode())

