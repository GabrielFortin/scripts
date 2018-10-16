import json

massvalues = {
    "a" : 89.1,
    "c" : 121.1,
    "d" : 133.1,
    "e" : 147.1,
    "f" : 165.2,
    "g" : 75,
    "h" : 155.1,
    "i" : 131.2,
    "k" : 146.2,
    "l" : 131.2,
    "m" : 149.2,
    "n" : 132.1,
    "p" : 115.1,
    "q" : 146.1,
    "r" : 174.2,
    "s" : 105.1,
    "t" : 119.1,
    "v" : 117.1,
    "w" : 204.2,
    "y" : 181.2
}

aliphatiques = 'gavlimp'
aromatiques = 'fw'
ionisables = 'krdeh'
nonionisables = 'stynqc'

chaina = "evanpehyik hplqnrwalw ffkndksktw qanlrliskf dtvedfwaly nhiqlssnlm pgcdyslfkd giepmwedek nkrggrwlit lnkqqrrsdl drfwletllc ligesfddys ddvcgavvnv rakgdkiaiw ttecenreav thigrvyker lglppkivig yqshadtatk sgsttknrfv v"
# chainb = "pggtriiydr kflmecrnsp"
chain = chaina
print(chain)
# If error with input, change raw_input to input
usechain = raw_input('\nUse chain above ? (y/n) ')
if usechain != 'y':
    chain = raw_input('Paste chain to use : ')
chain = chain.replace(' ', '')
print('There are ' + str(len(chain)) + ' amino acids in the chain.')
counted = list()
aminoacids = dict()
for letter in chain:
    if letter not in counted:
        counted.append(letter)
    if letter not in aminoacids:
        aminoacids[letter] = 1
    else:
        aminoacids[letter] += 1

print('There are ' + str(len(counted)) + ' different amino acids in the chain.')
print(json.dumps(aminoacids, indent=4))
# print('By family : ')
# print('aliphatiques : ' )
# out = ''
# for key, value in aminoacids.items():
#     if key in aliphatiques:
#         out += (key + ' : ' + str(value) + ', ')
print('Not formatted below')
print(aminoacids)

mass = 0

for amino, number in aminoacids.items():
    mass += (massvalues[amino] * number)

mass -= (len(chain) - 1) * 18

print('The total mass is ' + str(mass) + ' g/mol.')
