'''
Author:     Kjell Ziegert
Date:       02.02.2021
LICENSE:    MIT
'''

def is_reflexive(a, r):
    for element in a:
        if (element, element) not in r:
            return False
    return True

def is_symmetrical(a, r):
    for element in a:
        for element_2 in a:
            if (element, element_2) in r:
                if (element_2, element) not in r:
                    return False
    return True

def is_asymmetrical(a, r):
    for element in a:
        for element_2 in a:
            if (element, element_2) in r:
                if (element_2, element) in r:
                    return False
    return True

def is_transitive(a, r):
    for element in a:
        for element_2 in a:
            for element_3 in a:
                if (element, element_2) in r and (element_2, element_3) in r:
                    if (element, element_3) not in r:
                        return False
    return True

def is_aequivalencerelation(a, r):
    return (is_reflexive(a, r) and is_symmetrical(a, r) and (is_transitive(a, r)))

def is_orderrelation(a, r):
    return (is_reflexive(a, r) and is_asymmetrical(a, r) and (is_transitive(a, r)))

'''
Parameter:

a ist die Menge auf der die Relation zu betrachten ist
r ist die ZWEISTELLIGE Relation in Angabe als Menge

Hierbei koennen diese egal wie angegeben werden, also mit () oder [], niemals jedoch mit {} wie in der Mathematischen Mengenschreibweise, da dies in Python ein Dictionary ist statt einer Liste !
'''