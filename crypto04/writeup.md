# 3rd HighSchools CTF Workshop - Verona 2023

## [crypto] Elementary, Watson

I numeri del messaggio segreto corrispondono alla sequenza di tasti che è necessario premere in un vecchio telefono cellulare per comporre un SMS testuale.
È possibile decodificarlo a mano o tramite un tool online come [Multi-Tap Decoder](https://www.dcode.fr/multitap-abc-cipher).

A questo punto ci accorgiamo che l'ultima riga del messaggio è ancora in codice. Per capire l'agoritmo di cifratura utilizzato abbiamo ma disposizione due indizi:

- La frase del messaggio `ASK TO AT.SH`
- L'immagine allegata alla challenge

I due indizi ci dicono che l'ultima riga è stata codificata con il cifrario Atbash, facilmente invertibile tramite [CyberChef](https://gchq.github.io/CyberChef).
