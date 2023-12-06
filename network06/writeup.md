# 3rd HighSchools CTF Workshop - Verona 2023

## [network] A top secret message

Viene fornita una cattura in formato PCAP contenente l'invio di una mail. Recuperando l'allegato possiamo notare che questo è un file .zip protetto da password. La password è contenuta nel testo della mail, quindi estraendolo possiamo visualizzarne il contenuto.

### Soluzione

La descrizione parla di un messaggio di posta elettronica. Ricordando quanto visto nella lezione
teorica le mail utilizzano il protocollo SMTP. Possiamo quindi filtrare per tale protocollo inserendo
il filtro `smtp`.

Fatto questo notiamo che vi è lo scambio di una decina di pacchetti. Per visualizzare meglio la conversazione possiamo usare la funzione Follow TCP stream accessibile facendo tasto destro su
qualsiasi dei pacchetti.

Questo è il dialogo con il server SMTP:

```txt
220 mail.tinga.io ESMTP Postfix
EHLO [192.168.65.3]
250-mail.tinga.io
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-8BITMIME
250-DSN
250-SMTPUTF8
250 CHUNKING
MAIL FROM:<it@alerighi.it> BODY=8BITMIME SIZE=1360
250 2.1.0 Ok
RCPT TO:<agent.p@alerighi.it>
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
Content-Type: multipart/mixed; boundary="------------L4sBUshWrvX3h8gv0Za1PcOA"
Message-ID: <24f9611e-9b5e-48ff-919a-8fc2d3e67b90@alerighi.it>
Date: Sat, 25 Nov 2023 22:04:22 +0000
MIME-Version: 1.0
User-Agent: Mozilla Thunderbird
Content-Language: en-US
To: Agente P <agent.p@alerighi.it>
From: IT <it@alerighi.it>
Subject: NUOVE CREDENZIALI DI SICUREZZA

This is a multi-part message in MIME format.
--------------L4sBUshWrvX3h8gv0Za1PcOA
Content-Type: text/plain; charset=UTF-8; format=flowed
Content-Transfer-Encoding: 7bit

Buongiorno Agente P,

in allegato trova le nuove credenziali per connettersi al sistema.

Per motivi di sicurezza il file e' stato cifrato con la seguente
password: PERRY

Buona giornata,

il reparto IT


--------------L4sBUshWrvX3h8gv0Za1PcOA
Content-Type: application/zip; name="secret.zip"
Content-Disposition: attachment; filename="secret.zip"
Content-Transfer-Encoding: base64

UEsDBDMDAQBjAGeweVcAAAAAUgAAAD4AAAAPAAsAY3JlZGVuemlhbGkudHh0AZkHAAIAQUUB
AAAMmL53uxeUn+7i8ZQGSP0cYzxKPOX7ei949gFkLVpZMaKPNzHZI6ZE1H1z0jIXnptL/ts2
7VXX0SLBL8bpdogC2BvyKs9m6XzvrFCTmxeHXWNwUEsBAj8DMwMBAGMAZ7B5VwAAAABSAAAA
PgAAAA8ALwAAAAAAAAAggKSBAAAAAGNyZWRlbnppYWxpLnR4dAoAIAAAAAAAAQAYAAD9wy/r
H9oBAP3DL+sf2gEA/cMv6x/aAQGZBwACAEFFAQAAUEsFBgAAAAABAAEAbAAAAIoAAAAAAA==


--------------L4sBUshWrvX3h8gv0Za1PcOA--
.
250 2.0.0 Ok: queued as 4E47884CC0
```

Possiamo vedere, dopo un primo scambio di comandi fra client e server di posta
per avviare il trasferimento del messaggio, il messaggio stesso.

Il messaggio, come tutti i messaggi di posta che contengono allegati, è codificato
secondo MIME type multipart/mixed, dove ogni sezione è separata da un boundary (nel
nostro caso la stringa `--------------L4sBUshWrvX3h8gv0Za1PcOA`).

Possiamo notare che vi è un allegato, un file .zip. Decodificando il
base64 (ad es. con CyberChef) e salvando il file .zip risultante proviamo ad estrarlo.

Notiamo che ci viene chiesta una password: rileggendo la mail notiamo che la password
è `PERRY`, scritta all'interno del body della mail.

Una volta inserita nello zip troveremo un file credenziali.txt con dentro la flag.
