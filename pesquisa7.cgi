#!/bin/bash
echo "content-type: text/html"
echo

read LOCAL

CAMPO=$(echo $LOCAL | cut -d"=" -f2 ) 

PESQUISA="$CAMPO"

grep .:"$PESQUISA": estoque > andar.txt

echo "<pre>$(cat andar.txt)</pre>"


