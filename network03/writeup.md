# 3rd HighSchools CTF Workshop - Verona 2023

## [network] Corrupted image

L'immagine ha i primi 4 byte (magic bytes) danneggiati. Ripristinandoli è possibile visualizzarne il contenuto e leggere la flag.

### Soluzione

Se proviamo ad aprire l'immagine con un visualizzatore vediamo che non si apre.
Questo perché il file è corrotto.

Ispezionando il file con un editor esadecimale notiamo subito che manca qualcosa:

```sh
$ hexdump -C hacker.png | head -n 2
00000000  89 20 20 20 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.   ........IHDR|
00000010  00 00 05 00 00 00 02 d0  08 06 00 00 00 cf 7d dd  |..............}.|
```

Essendo un immagine PNG (almeno secondo l'estensione) possiamo notare che manca la classica
stringa `PNG` all'inizio di un file.

Questa corrisponde ai cosiddetti _Magic Bytes_ del file, ossia quei byte che vengono utilizzati
per capire che il contenuto del file è effettivamente un'immagine in formato PNG.

Cercando su internet notiamo che i magic bytes corretti per un'immagine PNG sono i seguenti: `89 50 4e 47 0d 0a 1a 0a`.

Sostituendone il contenuto utilizzando un editor esadecimale, in maniera tale che il risultato
sia il seguente, notiamo che l'immagine si apre, e possiamo leggere la flag.

```sh
$ hexdump -C hacker_fix.png | head -n 2
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
00000010  00 00 05 00 00 00 02 d0  08 06 00 00 00 cf 7d dd  |..............}.|
```
