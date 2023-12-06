# 3rd HighSchools CTF Workshop - Verona 2023

## [crypto] BaseNot64

Eccoti un bel messaggio cifrato... ehm volevo dire codificato.

`1i[\;7:U40>"3a06"Y"C10A^.;0"WPC,0sFH?r_<;_^d.2D]2h2/,]W>&e\-B/rh"BNR"`

### Soluzione

Come dice il titolo, il messaggio non è in Base64. È possibile provare ad applicare diverse decodifiche su [CyberChef](https://gchq.github.io/CyberChef).

Notiamo che nel testo di partenza vi sono molti più simboli rispetto a quelli della base 64, ciò indica che la base deve essere più alta. Provando con la base 85 otteniamo un testo ulteriormente codificato, questa volta con meno simboli.
Procediamo applicando la decodifica in base 58 e successivamente in base32 ottenendo cosí la flag.

È possibile risolvere la challenge anche utilizzando il pulsante "Bacchetta magica" di CyberChef che riconosce autonomamente le codifiche e ci restituisce la flag.
