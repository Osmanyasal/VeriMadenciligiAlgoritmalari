Naive bayes algoritmasını python3 ile kodladım

Kodlamış olduğum algoritma sadece kategorik veriler üzerinde çalışabilir.
eğer sayısal verileriniz varsa bunları kategorik hale geltirmelisiniz.

algoritmaya verilerinizi verirken data ve test olarak 2 ye ayırıp vermelisiniz

Data verisinde en son sutunda tahmin etmek istediğiniz kategori yer almalıdır.
tahmin verisinde ise tahmin edilmek istenilen kategori yer almamalıdır.

## örnek data ve tahmin verisi

-- DATA VERİSİ

age	income	student	credit_rating	computer
<=30	high	no	excellent	no
>40	low	yes	excellent	no
>40	medium	no	excellent	no
31..40	low	yes	excellent	yes
<=30	medium	yes	excellent	yes
31..40	medium	no	excellent	yes
<=30	high	no	fair		no
<=30	medium	no	fair		no
31..40	high	no	fair		yes
>40	medium	no	fair		yes
>40	low	yes	fair		yes
<=30	low	yes	fair		yes
>40	medium	yes	fair		yes
31..40	high	yes	fair		yes


-- TAHMİN VERİSİ

age	income	student	credit_rating
<=30	medium	yes	fair


j degeri...:  no
{'<=30': 3, 'medium': 2, 'yes': 1, 'fair': 2}
degerler :  3 5
degerler :  2 5
degerler :  1 5
degerler :  2 5
[0.006857142857142858]
j degeri...:  yes
{'<=30': 2, 'medium': 4, 'yes': 6, 'fair': 6}
degerler :  2 9
degerler :  4 9
degerler :  6 9
degerler :  6 9
[0.006857142857142858, 0.028218694885361547]
{'<=30': 0, 'medium': 0, 'yes': 0, 'fair': 0}
{'no': 5, 'yes': 9}

**********************
Sonuc degerleri ...: [0.006857142857142858, 0.028218694885361547]

Sonuç degeri sirayla no ve yes içindir.