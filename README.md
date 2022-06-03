### Rulare
Mai intai porniti virtual environmentul:

* Pentru windows (daca deschideti in command prompt si sunteti in radacina repository-ului):

```
> venv\Scripts\activate.bat
```

* Pentru mac si linux:
```
$ source venv/Scripts/activate
```

Mai departe porniti serverul:

* Linux/Mac (mie imi merge si pe windows):
```
$ python manage.py runserver
```

* Windows:
```
> py manage.py runserver
```

Daca vreti alt port sau nu e disponibil 8000 care e default:
```
$ py manage.py runserver <port>
```

Ca sa vedeti site-ul intrati in browser pe link-urile \
localhost:8000/ \
localhost:8000/authservice \
localhost:8000/authservice/login \
localhost:8000/authservice/signup \
localhost:8000/hotels \
localhost:8000/admin

### Credentiale
username = user-ip \
password = 9c6nuqdJKSUG*Sw

Adminul e deja creat si pastrat in baza de date (db.sqlite3):\
username = admin \
password = student

### Alte idei
Se schimba usor baza de date, pentru postgres doar trebuie instalat un pachet  psyg2 parca si de schimbat niste configurari in settings.py, dar asta ramane ultima problema, putem sa lasam si asa.

Mai trebuie adaugate oricum modele si date pentru hoteluri.
