
import re
def parse_molecule (formula):
    #print formula
    formula = formula.replace('(', '[').replace('{', '[').replace(')', ']').replace('}', ']')
    #print formula
    s = formula

    while s.find('[') > -1:
        stos, stos2 = [], []
        c,c1 = '', ''

        for i, x in enumerate(s):
          if x == '[':
            stos.append(i);
          if x == ']':
            c1 = re.findall('^[0-9]+', s[i+1:])
            c = c1[0] if len(c1) > 0 else 0
            stos2.append((stos.pop()+1, i, int(c)))

        p = stos2[0]

        s = s[:p[0]-1] + s[p[0]:p[1]] * (p[2] if p[2] > 0 else 1) + s[p[1] + 1 + (len(str(p[2])) if p[2] > 0 else 0):]

    l = re.findall('[A-Z][a-z0-9]*', s)
    #print l

    res = {}
    for x in l:
        v = re.findall('[^0-9]+', x) * (int(re.findall('[0-9]+', x)[0]) if len(re.findall('[0-9]+', x)) > 0 else 1);
        if res.has_key(v[0]):
            res[v[0]] += len(v)
        else:
            res[v[0]] = len(v)
    return res
from unittest import TestCase, main
def equals_atomically (obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True

class Test(TestCase):
    def test_one(self):
        testuple = (("H2O",
                {'H': 2, 'O' : 1},
                    "Should parse water"),
            ("B2H6",
                {'B': 2, 'H' : 6},
                    "Should parse diborane: B2H6"),
            ("C6H12O6",
                {'C': 6, 'H': 12, 'O' : 6},
                    "Should parse glucose: C6H12O6"),
            ("Mo(CO)6",
                {'Mo': 1, 'C': 6, 'O' : 6},
                    "Should parse molybdenum hexacarbonyl: Mo(CO)6"),
            ("Mg(OH)2",
                {'Mg': 1, 'O' : 2, 'H': 2},
                    "Should parse magnesium hydroxide: Mg(OH)2"),
            ("Fe(C5H5)2",
                {'Fe': 1, 'C': 10, 'H': 10},
                    "Should parse ferrocene: Fe(C5H5)2"),
            ("(C5H5)Fe(CO)2CH3",
                {'C': 8, 'H': 8, 'Fe': 1, 'O': 2},
                    "Should parse cyclopentadienyliron dicarbonyl dimer: (C5H5)Fe(CO)2CH3"),
            ("Pd[P(C6H5)3]4",
                {'Pd': 1, 'P': 4, 'C': 72, 'H': 60},
                    "Should parse tetrakis(triphenylphosphine)palladium(0): Pd[P(C6H5)3]4"),
            ("K4[ON(SO3)2]2",
                {'K': 4,  'O': 14,  'N': 2,  'S': 4},
                    "Should parse Fremy's salt: K4[ON(SO3)2]2"),
            ("As2{Be4C5[BCo3(CO2)3]2}4Cu5",
                {'As': 2,  'Be': 16,  'C': 44,  'B': 8,  'Co': 24,  'O': 48,  'Cu': 5},
                    "Should parse really weird molecule: As2{Be4C5[BCo3(CO2)3]2}4Cu5"),
            ("{[Co(NH3)4(OH)2]3Co}(SO4)3",
                {'Co': 4, 'N': 12, 'H': 42, 'O': 18, 'S': 3},
                    "Should parse hexol sulphate: {[Co(NH3)4(OH)2]3Co}(SO4)3")
           )

        for q21847, w23841, e32104 in testuple:
            self.assertTrue(equals_atomically(parse_molecule(q21847), w23841), e32104)