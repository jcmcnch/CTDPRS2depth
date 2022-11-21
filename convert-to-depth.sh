#!/bin/bash -i
conda activate pyseawater-env
scripts/convert-CTDPRS-to-depth.py CTDPRS_lat.tsv > CTDPRS_lat_depth.tsv 
