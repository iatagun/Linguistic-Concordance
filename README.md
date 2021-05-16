# Linguistic-Concordance
Dilbilimcilerin ihtiyaçları doğrultusunda geliştirilen concordance aracı

# Kullanımı

    conc2csv(): concordance to csv
    Concordance aranan sözcüğün önündeki ve arkasındaki dört sözcüğe bakıp
    excel dosyasına aktaran fonksiyon

```
>>>from concordance import conc2csv
>>>conc2csv('test.txt', 'bir', 4)
```
