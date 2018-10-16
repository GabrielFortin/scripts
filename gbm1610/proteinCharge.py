# Author : Gabriel Fortin
import json

data = {
    "a" : {'mass': 89.10, 'pkacooh': 2.35, 'pkanh': 9.87, 'pkar': 'NAN'},
    "c" : {'mass': 121.1, 'pkacooh': 1.92, 'pkanh': 10.70, 'pkar': 'NAN'},
    "d" : {'mass': 133.1, 'pkacooh': 1.99, 'pkanh': 9.90, 'pkar': 3.90},
    "e" : {'mass': 147.1, 'pkacooh': 2.10, 'pkanh': 9.47, 'pkar': 4.07},
    "f" : {'mass': 165.2, 'pkacooh': 2.20, 'pkanh': 9.31, 'pkar': 'NAN'},
    "g" : {'mass': 75.00, 'pkacooh': 2.35, 'pkanh': 9.78, 'pkar': 'NAN'},
    "h" : {'mass': 155.1, 'pkacooh': 1.80, 'pkanh': 9.33, 'pkar': 6.04},
    "i" : {'mass': 131.2, 'pkacooh': 2.33, 'pkanh': 9.76, 'pkar': 'NAN'},
    "k" : {'mass': 146.2, 'pkacooh': 2.16, 'pkanh': 9.06, 'pkar': 10.54},
    "l" : {'mass': 131.2, 'pkacooh': 2.33, 'pkanh': 9.76, 'pkar': 'NAN'},
    "m" : {'mass': 149.2, 'pkacooh': 2.13, 'pkanh': 9.28, 'pkar': 'NAN'},
    "n" : {'mass': 132.1, 'pkacooh': 2.14, 'pkanh': 8.72, 'pkar': 'NAN'},
    "p" : {'mass': 115.1, 'pkacooh': 1.95, 'pkanh': 10.64, 'pkar': 'NAN'},
    "q" : {'mass': 146.1, 'pkacooh': 2.17, 'pkanh': 9.13, 'pkar': 'NAN'},
    "r" : {'mass': 174.2, 'pkacooh': 1.82, 'pkanh': 8.99, 'pkar': 12.48},
    "s" : {'mass': 105.1, 'pkacooh': 2.19, 'pkanh': 9.21, 'pkar': 'NAN'},
    "t" : {'mass': 119.1, 'pkacooh': 2.09, 'pkanh': 9.10, 'pkar': 'NAN'},
    "v" : {'mass': 117.1, 'pkacooh': 2.39, 'pkanh': 9.74, 'pkar': 'NAN'},
    "w" : {'mass': 204.2, 'pkacooh': 2.46, 'pkanh': 9.41, 'pkar': 'NAN'},
    "y" : {'mass': 181.2, 'pkacooh': 2.20, 'pkanh': 9.21, 'pkar': 'NAN'},
}

### INPUTS ###
ph = 7.4
chaina = "evanpehyik hplqnrwalw ffkndksktw qanlrliskf dtvedfwaly nhiqlssnlm pgcdyslfkd giepmwedek nkrggrwlit lnkqqrrsdl drfwletllc ligesfddys ddvcgavvnv rakgdkiaiw ttecenreav thigrvyker lglppkivig yqshadtatk sgsttknrfv v"
chains = [chaina]
##############

chaincount = 1
for chain in chains:
    print('*** Chain ' + str(chaincount) + ' ***')
    chaincount += 1
    # Count amino acids in chain
    counted = list()
    aminoacids = dict()
    for letter in chain:
        if letter not in counted:
            counted.append(letter)
        if letter not in aminoacids:
            aminoacids[letter] = 1
        else:
            aminoacids[letter] += 1

    print('Pour pH = '+ str(ph)+ ' : ')

    aminterminal = chain[0]
    numerator = float(10)**(ph - data[aminterminal]['pkanh'])
    percentnh3plus = float(1) - (numerator / (numerator + float(1)))
    percentnh3plus *= 100
    print('Pourcentage de NH3+ : ' +str(percentnh3plus) + ' %')
    
    partialchargeaminterminal = 1 * (percentnh3plus/100)


    carboxylterminal = chain[-1]
    numerator = float(10)**(ph - data[carboxylterminal]['pkacooh'])
    percentcoominus = numerator / (numerator + float(1)) 
    percentcoominus *= 100
    print('Pourcentage de COO- at : ' +str(percentcoominus) + ' %')

    partialchargecarboxylterminal = -1 * (percentcoominus/100)
    
    totalcharge = partialchargeaminterminal + partialchargecarboxylterminal

    ionisables = ['d', 'e', 'h', 'k', 'r']
    for ionisable in ionisables:
        if ionisable in aminoacids:
            pkar = data[ionisable]['pkar']
            partialcharger = 0
            if pkar < 4.10 and pkar != 'NAN':
                numerator = 10**(ph - pkar)
                percentcoominus = numerator / (numerator + float(1))
                percentcoominus *= 100
                print('Pourcentage COO- pour ' + ionisable.upper() + ' : ' + str(percentcoominus) + ' %' + ' pour ' + str(aminoacids[ionisable]) + ' ' + ionisable.upper()) 
                partialcharger = -1 * (percentcoominus/100)
            elif pkar > 4.10  and pkar != 'NAN':
                numerator = 10**(ph - pkar)
                percentnh3plus = 1- (numerator / (numerator + float(1)))
                percentnh3plus *= 100
                print('Pourcentage NH3+ pour ' + ionisable.upper() + ' : ' + str(percentnh3plus) + ' %' + ' pour ' + str(aminoacids[ionisable]) + ' ' + ionisable.upper()) 
                partialcharger = 1 * (percentnh3plus/100)
            
            totalcharge += aminoacids[ionisable] * partialcharger

    print('Charge de la proteine : '+str(totalcharge))
    print('\n')