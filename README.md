# ProgramlamaDilleri Bot's Panel & API
<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Bu proje [Programlama Dilleri Bot](https://t.me/programlama_bot) u icin gelistirilmistir. 
Henuz aktif durumda degildir. Denemek veya incelemek icin kurulum adimlarini izleyebilirsiniz.

### Kurulum adimlari  
```shell
git clone https://github.com/ahmetveburak/ProgramlamaDilleri_API.git
cd ProgramlamaDilleri_API
poetry install # venv olusuyor ise etkinlestirmeyi unutma :)

python manage.py migrate
python manage.py initdb
python manage.py runserver
```
Default admin giris bilgileri
```shell
email: admin@admin.com
pass: 1
```

---
 
_Botun test edilmesi ve kullanilabilmesi icin
hazir kaynak verisi de eklenmistir fakat ayri bir sekilde calistirmak icin yeterli degildir.
Projenin paylasim amaci kopya bir kaynak botu olusturulmasi yerine 
kendimce uyguladigim menu/navigasyon yapisini best practice olmasa da oneri/fikir olarak
paylasmaktir :)_