#!/bin/sh

rsparql --results NT --service https://query.wikidata.org/sparql --query wikidata-links.rq | sort >slices/gacs-wikidata-links.nt
