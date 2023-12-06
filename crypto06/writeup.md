# 3rd HighSchools CTF Workshop - Verona 2023

## [crypto] Secret sound

Abbiamo a disposizione un file audio, ascoltandolo è possible riconoscere il suono caratteristico della pressione dei tasti sulla tastiera di un telefono. Nello specifico si tratta di _Dual-tone multi-frequency_ (DTMF), ossia un sistema di codifica usato in telefonia per codificare codici numerici sotto forma di segnali sonori in banda audio.

È possibile usare un tool online come [DTMF Encoder/Decoder](https://unframework.github.io/dtmf-detect/) per decodificare il segnale audio.
Dopo la decodifica otteniamo la seguente sequenza di tasti: `2331434783711923431767372331117714113`.

Ascoltando attentamente il suono notiamo che la pressione dei tasti è alternata a momenti di silezio, i valori decodificati possono essere quindi separati nel modo seguente: `23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13`.

I valori ottenuti hanno una caratteristica in comune, sono tutti numeri primi. Possiamo quindi associare ad ognuno la lettera dell'alfabeto che ha la stessa posizione del valore nell'elenco ordinato dei numeri primi.
