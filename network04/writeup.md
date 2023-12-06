# 3rd HighSchools CTF Workshop - Verona 2023

## [network] Nothing to see there

L'immagine contiene un file nascosto al suo interno, estraendolo con CyberChef notiamo che questo è un archivio `tar` che contiene la flag.

### Soluzione

Il file sembra una normale immagine JPEG. Proviamo ad aprire l'immagine con CyberChef e vedere
se al suo interno vi sono file nascosti.

Analizzandola con la funzione Forensics -> Scan for embedded files possiamo notare che viene
individuata la presenza di un file `tar` alla fine dell'immagine.

Possiamo quindi usare la funzione Forensics -> Extract files per estrarne il contenuto.

Vediamo che il contenuto è un file tar, un comune formato di archivio (simile ai file .zip) tipicamente
usato in sistemi Linux.

È possibile estrarne il contenuto utilizzando un qualsiasi software di gestione archivi. Su Linux/macOS
non è necessario installare tipicamente alcun software extra, mentre su Windows è possibile usare
il software open-source 7-zip (ma anche WinRar è in grado di estrarlo, se se ne possiede una licenza).

Aprendo l'archivio è possibile trovare una cartella `secret/`, al cui interno vi è un file `message.txt`,
in cui è contenuta la flag.
