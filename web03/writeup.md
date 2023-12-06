# 3rd HighSchools CTF Workshop - Verona 2023

## [web] find-me

Sulla pagina principale è presente un link che porta al menù completo del Gilberto Coffee Shop. Seguendo il link notiamo il seguente endpoint: "/menu?file=menu.txt".
Intuiamo quindi che con ogni probabilità è possibile leggere file dal web-server. Questo tipo di vulnerabilità è comunemente detta Path Traversal: siamo cioè in grado di leggere file arbitrari sul web server.
Il codice (nella challenge) che permette la lettura di file arbitrari è il seguente:

```python
file_path = request.args.get('file')
    if file_path:
        try:
            with open(file_path, 'r') as file:
                return render_template("menu.html", file_content=file.read())
        except FileNotFoundError:
            return "File not found", 404
```

dove la variabile `file_path` viene presa dalla query `?file=<file_path>`. Il file viene poi aperto tramite la funzione `open()` di python e infine viene renderizzata la pagina con il contenuto del file.

Sostituendo quindi "menu.txt" con "/flag.txt" siamo in grado di accedere al contenuto del file "flag.txt" presente nella root directory del web server.
