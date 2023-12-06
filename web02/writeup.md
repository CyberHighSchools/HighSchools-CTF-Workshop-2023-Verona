# 3rd HighSchools CTF Workshop - Verona 2023

## [web] change-me

Leggendo il codice (app.py) si nota che la flag viene inclusa nel template flag.html e che questo viene renderizzato solo se la richiesta è una POST.

```python
    if(request.method == 'GET'):
        return render_template('index.html')
    elif(request.method == 'POST'):
        return render_template('flag.html', flag=FLAG)
```

Si può quindi utilizzare curl per effettuare una richiesta POST:

`curl -XPOST <url>`
