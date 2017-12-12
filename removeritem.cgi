#!/bin/bash

read POST

item=$(echo $POST | cut -d"=" -f2)
if [[ $(grep -E "(.*:)$item(:.*){4}" estoque ) ]] ; then
        sed -ri "/(.*:)$item(:.*){4}/d" estoque
        #cat estoque2 >> estoque
else
	erro="Deu Merda"
fi

cat <<EOFFF
content-type: text/html

<html>
<h1>caralho</h1>
<h2>$erro</h2>
<a href="../pgnadm.html">Voltar</a>
</html>
EOFFF
