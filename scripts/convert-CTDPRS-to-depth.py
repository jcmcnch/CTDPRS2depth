#!/usr/bin/env python

import seawater as sw
import csv
import sys

hashPRSLatDepthCTD = {}

#print header
print('\t'.join(["CTDPRS", "Latitude", "Depth (m)"]))

#read in CTD data and convert on the fly - PRS should be first as key and an array with latitude as the only value
for astrLine in csv.reader(open(sys.argv[1]), csv.excel_tab):

    EOS80depth = sw.dpth(float(astrLine[0]), float(astrLine[1]))

    print('\t'.join([astrLine[0], astrLine[1], str(EOS80depth)]))
