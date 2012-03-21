#! /usr/bin/python -i
from copy import copy

PRINTABLE_CHARACTERS = [9,10,13] + range(32,127)

class Freq(object):
    def __init__(self,charset=PRINTABLE_CHARACTERS):
        self.diagraph = {}
        self.freq = {}
        self.sorted_freqs = []
        self.heat_map = []

        self.charset = charset

    def feed(self,data):
        for ci in xrange(1,len(data)):
            # make sure our dict has the right elts
            self.diagraph.setdefault(data[ci-1],{})
            self.diagraph[data[ci-1]].setdefault(data[ci],0)
            # increment diagraph
            self.diagraph[data[ci-1]][data[ci]] += 1

            #make sure our freq dict has the right elts
            self.freq.setdefault(data[ci],0)
            # increment frequency
            self.freq[data[ci]] += 1
        
        self._sort()
        
    def _sort(self):
        sorted_by_freq = sorted(self.freq.iteritems(),cmp=lambda x,y:cmp(y[1],x[1]))
        self.sorted_freqs = []
        for c in sorted_by_freq:
            self.sorted_freqs.append((c[0],sorted(self.diagraph[c[0]].iteritems(),cmp=lambda x,y:cmp(y[1],x[1])))) 

    
    def __repr__(self):
        return str(self.sorted_freqs)

if __name__ == "__main__":
    print "Starting"
    print "Making Freq()"
    fr = Freq()
    print "Loading sample_text"
    f = open('sample_text','r')
    d = f.read()
    print "Feeding sample_text data to Freq()"
    fr.feed(d)
    print "Done"