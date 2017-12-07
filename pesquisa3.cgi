#!/bin/bash
echo "content-type: text/html"
echo

read LOCAL

CAMPO=$(echo $LOCAL | cut -d"=" -f2 ) 

PESQUISA="$CAMPO"

grep .:.:"$PESQUISA": estoque > sala.txt

echo "<pre>$(cat sala.txt)</pre>"


