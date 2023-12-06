# 3rd HighSchools CTF Workshop - Verona 2023

## [network] Forgot password

La flag si trova nel body di una richiesta POST HTTP

### Soluzione

Analizzando il file .pcap con Wireshark si possono notare diversi pacchetti. In questa challenge siamo
interessati a filtrare il traffico per il protocollo HTTP, quindi possiamo inserire nella barra dei filtri: `http`

A questo punto analizziamo le varie richieste. Notiamo nel dissector (in basso a sinistra) che possiamo
analizzare il contenuto della richiesta.

Fra le richieste HTTP notiamo una POST, che solitamente è il tipo di richiesta che dispone di un body.
Notiamo che Wireshark va anche a decodificare il body (in questo caso codificato come form-url-encoded)
e mostrarci i due campi: `username` e `password`.

Nel campo `password` vi è la flag richiesta.
