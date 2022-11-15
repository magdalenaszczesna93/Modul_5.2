class filmy:
    def __init__ (self, tytul, rok_wydania, gatunek, liczba_odtworzen):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtwoezen = liczba_odtworzen
    def __str__ (self):
        return f'{self.tytul} {self.rok_wydania} {self.gatunek} {self.liczba_odtwoezen}'

movie1 = filmy(tytul='Dogs', rok_wydania='1994', gatunek='komedia', liczba_odtworzen=20)
movie2 = filmy(tytul='Cats', rok_wydania='1995', gatunek='dokumentalny', liczba_odtworzen=10)
movie3 = filmy(tytul='Tiger', rok_wydania='1998', gatunek='biograficzny', liczba_odtworzen=25)
movie4 = filmy(tytul='Home', rok_wydania='2005', gatunek='horror', liczba_odtworzen=35)

class seriale(filmy):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
    def __str__ (self):
        return f'{self.tytul} {self.rok_wydania} {self.gatunek} {self.liczba_odtwoezen} S{self.numer_odcinka:02d}E{self.numer_sezonu:02d}'

series1 = seriale(tytul='The Simpsons', rok_wydania='1994', gatunek='komedia', liczba_odtworzen=20, numer_odcinka= 1, numer_sezonu= 1)
series2 = seriale(tytul='Game of Thrones', rok_wydania='2000', gatunek='obyczajowy', liczba_odtworzen=45, numer_odcinka= 1, numer_sezonu= 1)
series3 = seriale(tytul='Friends', rok_wydania='1995', gatunek='komedia', liczba_odtworzen=35, numer_odcinka= 1, numer_sezonu= 1)
series4 = seriale(tytul='Star Trek', rok_wydania='2004', gatunek='horror', liczba_odtworzen=10, numer_odcinka= 1, numer_sezonu= 1)

print(movie2)
print(series3)