#!/usr/bin/env python
#===================================================================

import random
VERBOSE = False


#-------------------------------------------------------------------
# NumOnes
#
# Calculates the number of ones and the ration of ones.
#-------------------------------------------------------------------
class NumOnes:
    def __init__(self):
        self.ones = 0
        self.bits = 0
        print("NumOnes: Count all one bits.")

    def consume(self, i):
        for n in xrange(32):
            if (i & 0x01):
                self.ones += 1

            self.bits += 1
            i = i >> 1


    def present(self):
        print("NumOnes:")
        print("Number of bits: %d, number of ones: %d, ratio: %3f" %
              (self.bits, self.ones, (float(self.ones) / float(self.bits))))
        print("")


#-------------------------------------------------------------------
# BitRuns
#
# Find maximum run length of bits (either ones of zero).
#-------------------------------------------------------------------
class BitRuns:
    def __init__(self):
        self.firstbit = True
        self.max = 0
        self.count = 0
        self.bit = 0
        self.lengths = [0] * 64
        print("BitRuns: Find maximum run length and number of runs for a given run length.")


    def consume(self, i):
        for n in xrange(32):
            curr = (i & 0x80000000) >> 31
            if VERBOSE:
                print("i = 0x%08x, bit31 = 0x%01x" % (i, curr))

            if (curr) == self.bit:
                self.count += 1
            else:
                self.lengths[self.count] += 1
                if self.count >= self.max:
                    self.max = self.count
                self.count = 1

            self.bit =  curr
            i = i << 1 & 0xffffffff


    def present(self):
        print("BitRuns:")
        print("Maximum run length: %d bits" % self.max)
        for i in xrange(64):
            if (self.lengths[i] > 0) and i > 0:
                print("Number of runs with length %3d: %d" %
                (i, self.lengths[i]))
        print("")


#-------------------------------------------------------------------
# Lets test.
#-------------------------------------------------------------------

num_words = 100000

print("\n Online tester model")
print("-===================-")
print("Running online test models with %d 32-bit words." % num_words)

print("\nThe following test models are used:")
print("-----------------------------------")

my_Numones = NumOnes()
my_BitRuns = BitRuns()

for i in xrange(num_words):
    if VERBOSE:
        print("iteration %d" % i)
    rand = random.randint(0, (2**32) - 1)
    my_Numones.consume(rand)
    my_BitRuns.consume(rand)

print("\nResults from the models:")
print("------------------------")
my_Numones.present()
my_BitRuns.present()

#=======================================================================
# EOF online_tester.py
#=======================================================================
