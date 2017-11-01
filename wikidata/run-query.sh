#!/bin/sh

rsparql --service http://tester-os-kktest.lib.helsinki.fi/sparql --query gacs-geo-mixnmatch.rq --out CSV >gacs-geo-mixnmatch.csv
./join-table.py <gacs-geo-mixnmatch.csv >gacs-geo-mixnmatch.tsv

