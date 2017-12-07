#!/bin/bash
read POST
usuario=$(echo $POST | cut -d"=" -f2)
if [[ $(grep "^$usuario:" passwd ) ]] ; then
        cp passwd backup/passwd$(date +%Y%m%d%H%M%S)    
        cat passwd | sed "/$usuario\:/d" > passwd2
        cat passwd2 > passwd
cat <<EOFFF
content-type: text/html

<html>
<h1>caralho</h1>
<a href="../pgnadm.html">Voltar</a>
</html>
EOFFF
else
cat <<EOFFF
content-type: text/html

<html>
<h1>caralho deu treta</h1>
</html>
EOFFF

fi
