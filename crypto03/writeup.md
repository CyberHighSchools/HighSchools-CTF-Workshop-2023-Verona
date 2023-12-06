# 3rd HighSchools CTF Workshop - Verona 2023

## [crypto] XOR enough

Dal titolo della challenge possiamo dedurre che la flag è stata cifrata utilizzando l'operatore XOR ed una chiave segreta a noi sconosciuta.
Il testo poi fornisce un ulteriore indizio in quanto ci ricorda il formato della flag, che inizia con `flag{`.

Usando questa informazione possiamo recuperare la chiave segreta nel seguente modo:

1. Effettuiamo lo XOR della stringa `flag{` con i primi cinque bytes del testo cifrato per recuperare una parte della chiave. Osserviamo che la chiave inizia con `xorKE`, putroppo non è completa.
2. Facendo qualche tentativo di decifratura è scopriamo che alla chiave manca un solo byte. Quest'ultimo è facilmente recuperabile tramite un bruteforce.

Tutte le operazioni possono essere svolte su [CyberChef](https://gchq.github.io/CyberChef).
