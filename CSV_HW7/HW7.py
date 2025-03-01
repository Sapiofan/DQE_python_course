import re
from collections import Counter
import csv


def word_counter(text):
    words = re.findall(r'\b\w+\b', text)
    counter = Counter(words).most_common()

    return [[word, count] for word, count in counter]


def letter_counter(text):
    letters_in_text = []
    lower_letter_in_text = []
    for symbol in text.lower():
        if symbol.isalpha():
            letters_in_text.append(symbol)
            lower_letter_in_text.append(symbol.lower())

    counter = Counter(letters_in_text)
    counter_lower = Counter(lower_letter_in_text).most_common()
    letter_list = []
    for key, value in counter_lower:
        letter_list.append([key, value, counter.get(key.upper(), 0),
                            int(round(float(value / len(letters_in_text)), 2) * 100)])

    return letter_list


def write_to_csv(header_list, data_list, path):
    with open(path, 'w', newline='') as file:
        writer = csv.DictWriter(file, delimiter=',',
                                fieldnames=header_list)
        writer.writeheader()
        for record in data_list:
            if header_list[0] == 'word':
                row = {header_list[0]: record[0], header_list[1]: record[1]}
                writer.writerow(row)
            elif header_list[0] == 'letter':
                row = {header_list[0]: record[0], header_list[1]: record[1],
                       header_list[2]: record[2], header_list[3]: record[3]}
                writer.writerow(row)
