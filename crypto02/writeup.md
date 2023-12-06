# 3rd HighSchools CTF Workshop - Verona 2023

## [crypto] Mi piacciono i treni

Ho ricevuto una mail da un amico ma contiene un testo crittografato ed una strana somma.
Non so cosa fare. Aiutami a recuperare il messaggio!

```text
Ciphertext: amGlg03_of{s_p1}A3k3n!w39
Key + Offset: 11
```

### soluzione

Analizzando il titolo e la descrizione della sfida, capiamo che il messaggio è stato cifrato con un _Rail Fence Cipher_.
Possiamo decodificare il testo manualmente o usando [CyberChef](https://gchq.github.io/CyberChef), ottenendo la flag quando la chiave è uguale a 5 e l'offset è uguale a 6 (6 + 5 = 11).
