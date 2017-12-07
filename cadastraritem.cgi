#!/bin/bash
read POST

foi(){
cat <<EOFFF
content-type: text/html

        <html>
        <h1>caralho</h1>
        <a href="../pgnadm.html">Voltar</a>
        </html>
EOFFF
}

foinao(){
cat <<EOFFF
content-type: text/html

        <html>
     <h1>deu pau</h1>
        <a href="../pgnadm.html">Voltar</a>
        </html>
EOFFF
}

usuario=$(echo $POST | cut -d"&" -f1 | cut -d"=" -f2)
senha=$(echo $POST | cut -d"&" -f2 | cut -d"=" -f2)
if [[ ! $(grep "^$usuario:" passwd) ]] ; then
        echo "$usuario:$senha" >> passwd
        foi
else
        foinao
fi
