# Z3 - math solver library for Python



# Problem 1

prop = 'Ana are mere.'.lower()

freq = ()
max_freq = 0

for letter in 'abcdefghijklmnopqrstuvwxyz':
    freq[letter] = prop.count(letter)

max_freq = max(freq.values())

m = []
for i in range(26):
    m += ['o' * freq[chr(ord('a' + i))] + '-' * (max_freq - freq[chr(ord('a') + i)])]

for j in range(max_freq):
    print('\n')
    for i in range(26):
        print(m[i][j], end = "")

with open('output.txt', 'w') as f:
    pass
print()
print(''.join(freq.keys()))



# Problem 2

print([(letter, ord(letter)) for index, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')])



# Problem 3

with open('output.txt', 'r') as f:
    text = f.read()

hex_alphabet = "0123456789ABCDEF"

hex_representation = [[]]

for i in range(0, 16):
    hex_representation[0].append('0' + hex_alphabet[i])

text_length = len(text)

current_index = 0
for i in range(0, len(text) // 16):
    hex_representation.append([hex(ord(text[i * 16 + curr])) for curr in range(16)])
    #current_index += 16

hex_representation.append([hex(ord(text[i * 16 + curr])) for curr in range(16 - len(text) % 16)])

print(hex_representation)

ox_removed = [[f"{elem[2:]:>02}" for elem in ln] for ln in hex_representation]

print(ox_removed)

for ln in ox_removed:
    print(' '.join(ln))



# Probleme grele - Problema 1

import json

with open('Studenti.txt') as f:
    data = json.load(f)

counter = 0
for student in data.values():
    seminar = sum(student['seminarii']) / len(student['seminarii']) * 0.2
    examene = (student['partial'] + student['curs']) * 0.03
    proiect = student['proiect'] * 0.02

    media = seminar + examene + proiect

    if media >= 4.5:
        counter += 1

print(len(data))
print(counter)