# 3rd HighSchools CTF Workshop - Verona 2023

## [network] Stolen diskette

Viene fornita l'immagine di un disco che contiene dei file eliminati. Recuperando i file eliminati è possibile trovare un file PDF che contiene la flag.

### Soluzione

Viene forinta assieme alla challenge un immagine floppy disk FAT32.

Provando a montare l'immagine del disco, o aprendola con un software di gestione archivi come 7-zip, si nota che contiene solo un file `LEGGIMI` che indica che l'Agente P ci ha preceduto ed ha eliminato tutte le informazioni sensibili.

Ricordiamo che quando cancelliamo un file da un disco non stiamo effettivamente eliminando il contenuto,
ma stiamo solo eliminando i suoi metadati, andando a marcare le aree di memoria che prima erano occupate
dal contenuto del file come libere.

Tuttavia il contenuto non è veramente eliminato fintantoché quelle locazioni di memoria non sono sovrascritte dalla creazione di un nuovo file.

Per recuperare i file eliminati da un supporto esistono vari metodi e software, ad esempio un software
open-source molto comune è Photorec.

Tuttavia possiamo, trattandosi di un file di piccole dimensioni, utilizzare anche uno strumento come
CyberChef, che tuttavia non sarebbe adatto ad analizzare immagini più grandi (ad es. un intero drive da 1Tb).

Possiamo come per la scorsa challenge usare la funzione Forensic -> Extract Files. A questo punto
notiamo che fra i file vi è un PDF. Scaricandolo ed aprendolo con un software di visualizzazione notiamo
che al suo interno vi è un messaggio che contiene la flag.
