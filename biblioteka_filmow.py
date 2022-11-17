import random

class Film:
    def __init__ (self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = 0

    def __str__ (self):
        return f'{self.tytul} ({self.rok_wydania})'

    def __repr__ (self):
        return f'{self.tytul} ({self.rok_wydania}) {self.gatunek} {self.liczba_odtworzen}'

    def play (self):
        self.liczba_odtworzen += 1
            
class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__ (self):
        return f'{self.tytul} S{self.numer_odcinka:02d}E{self.numer_sezonu:02d}'

    def __repr__ (self):
        return f'{self.tytul} S{self.numer_odcinka:02d}E{self.numer_sezonu:02d} ({self.rok_wydania}) {self.gatunek} {self.liczba_odtworzen}'

def get_movies(lista_all):
    movies = []
    for i in lista_all:
        if type(i) == Film:
            movies.append(i)
            sorted_movies = sorted(movies, key=lambda movie: movie.tytul)
    return sorted_movies

def get_series(lista_all):
    series = []
    for i in lista_all:
        if type(i) == Serial:
            series.append(i)
            sorted_series = sorted(series, key=lambda series1: series1.tytul)
    return sorted_series

def search(title):
    for i in lista_all:
        if title == i.tytul:
            return i

def generate_views(lista_all):
    r= random.choice(lista_all)
    i = random.choice(range(1,101))
    r.liczba_odtworzen += i
    return repr(r)

# dlaczego na końcu daje "none"?
# jak wrzucę wszystko do return zamiast print to zwróci mi tylko raz
def play_generate():
    for n in range(10):
        print(generate_views(lista_all)) 

def top_titles(lista_all, content_type, n):
    top = []
    for i in lista_all:
        if type(i) == content_type:
            top.append(i)
            by_liczba_odtworzen = sorted(top, key=lambda liczba:liczba.liczba_odtworzen, reverse = True)
    return repr(by_liczba_odtworzen[:n])

movie1 = Film(tytul='Dogs', rok_wydania='1994', gatunek='komedia')
movie2 = Film(tytul='Cats', rok_wydania='1995', gatunek='dokumentalny')
movie3 = Film(tytul='Tiger', rok_wydania='1998', gatunek='biograficzny')
movie4 = Film(tytul='Home', rok_wydania='2005', gatunek='horror')

series1 = Serial(tytul='The Simpsons', rok_wydania='1994', gatunek='komedia', numer_odcinka= 1, numer_sezonu= 1)
series2 = Serial(tytul='Game of Thrones', rok_wydania='2000', gatunek='obyczajowy', numer_odcinka= 1, numer_sezonu= 1)
series3 = Serial(tytul='Friends', rok_wydania='1995', gatunek='komedia', numer_odcinka= 1, numer_sezonu= 1)
series4 = Serial(tytul='Star Trek', rok_wydania='2004', gatunek='horror', numer_odcinka= 1, numer_sezonu= 1)

movie2.play()
movie2.play()
movie2.play()
movie2.play()
print(movie2.liczba_odtworzen)

print(series2)
print(series3)

lista_all = []
lista_all.append(movie1)
lista_all.append(movie2)
lista_all.append(movie3)
lista_all.append(movie4)
lista_all.append(series1)
lista_all.append(series2)
lista_all.append(series3)
lista_all.append(series4)
print(lista_all)

print(get_movies(lista_all))
print(get_series(lista_all))

print(search('Dogs'))
print(search('Friends'))

print(play_generate())

print(top_titles(lista_all, Film, 3))
print(top_titles(lista_all, Serial, 3))

