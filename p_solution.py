import math

def rgb(r, g, b):
    def hexa(v):
       if v < 10: return v
       else:
           return "ABCDEF"[v-10]
    if r > 255: r = 255
    if r < 0: r = 0
    if g > 255: g = 255
    if g < 0: g = 0
    if b > 255: b = 255
    if b < 0: b = 0
    r2 = hexa(r % 16)
    r1 = hexa(int(math.floor(r / 16)))
    g2 = hexa(g % 16)
    g1 = hexa(int(math.floor(g / 16)))
    b2 = hexa(b % 16)
    b1 = hexa(int(math.floor(b / 16)))
    return str(r1) + str(r2) + str(g1) + str(g2) + str(b1) + str(b2)
from random import randint

from unittest import TestCase, main

class Test(TestCase):

    def test_file(self):
        self.assertEquals(rgb(0,0,0),"000000", "testing zero values")
        self.assertEquals(rgb(1,2,3),"010203", "testing near zero values")
        self.assertEquals(rgb(255,255,255), "FFFFFF", "testing max values")
        self.assertEquals(rgb(254,253,252), "FEFDFC", "testing near max values")
        self.assertEquals(rgb(-20,275,125), "00FF7D", "testing out of range values")
