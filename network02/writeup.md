# 3rd HighSchools CTF Workshop - Verona 2023

## [network] My briefcase

Analizzando la richiesta HTTP è possibile scaricare un file zip. All'interno del file zip sono contenuti diversi file, all'interno di uno di questi vi è la flag.

### Soluzione

Come per la flag precedente possiamo notare che vi sono delle richieste HTTP.

In questo caso useremo la funzione Export Objects di Wireshark (File -> Export Objects -> HTTP)
per andare a visualizzare quali file sono presenti nelle richieste HTTP.

Notiamo che è presente un file `briefcase.zip` che contiene le informazioni TOP SECRET che stavamo
cercando.

Esportando questo file ne possiamo estrarre il contenuto con un qualsiasi file manager.

All'interno notiamo un centinaio di file, nella maggioranza di questi vi è scritto che la flag si
trova in un altro file.

A questo punto possiamo o aprire tutti i file (operazione lunga!) oppure usare un qualsiasi sistema
per cercare all'interno del contenuto dei file.

Vi sono vari modi, ad esempio usando le funzioni di ricerca del sistema operativo, oppure usando
le funzioni di ricerca di un editor di testo come VSCode.

Se siamo su un PC Linux/macOS possiamo usare ad esempio il comando `grep`:

```bash
grep -R 'flag{' briefcase/
```

Su Windows invece possiamo usare il comando `findstr` da DOS oppure `Select-String` da PowerShell (vedi le opzioni del comando per l'esatta sintassi in quanto sono differenti).
