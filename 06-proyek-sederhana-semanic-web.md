# Membuat aplikasi sederhana semantic web
To do:
- Menyimpan data seputar kampus dalam format RDF (Turtle).
- Upload ke Jena Fuseki sebagai dataset RDF.
- Menjalankan SPARQL query untuk menampilkan data mahasiswa.

Prasyarat:
- sudah install java JDK yang sesuai kebutuhan Apache Jena Fuseki
- sudah install Apache Jena Fuseki (https://jena.apache.org/download/index.cgi)
-  sudah install python

Code, RDF, SPARQL dapat dilihat pada folder [jena-proyek](https://github.com/erickpaulus/SemanticWeb/tree/main/jena-proyek)
## Struktur Proyek
```
jena-project/
├── data/
│   └── mahasiswa.ttl
│   └── data-kampus1.ttl
│   └── data-kampus2.ttl
├── sparql/
│   └── sparql1.ttl
│   └── sparql2.ttl
├── app.py   <-- (jika kamu pakai Python + requests)
```
## 1. Dataset RDF (Turtle) – mahasiswa.ttl
```
@prefix ex: <http://example.org/ns#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

ex:mahasiswa1 a ex:Mahasiswa ;
    foaf:name "Agus Mulyono" ;
    ex:nim "11210010" ;
    ex:prodi "Teknik Informatika" .

ex:mahasiswa2 a ex:Mahasiswa ;
    foaf:name "Guntur Karo" ;
    ex:nim "1321001" ;
    ex:prodi "Sistem Informasi" .

```

## 2. Jalankan Fuseki dan Upload Dataset
- Buka folder Apache Jena Fuseki
- _double click_ fuseki-server.bat 
```
./fuseki-server.bat
```
- Buka browser ke: http://localhost:3030
- Buat dataset baru, misal mhs-db
- pilih add data
- Upload file mahasiswa.ttl data data turtle lainnya, lihat [di sini](https://github.com/erickpaulus/SemanticWeb/tree/main/jena-proyek/data)

## 3. Contoh SPARQL Query
```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX ex: <http://example.org/ns#>

SELECT ?nama ?nim ?prodi WHERE {
  ?mhs a ex:Mahasiswa ;
       foaf:name ?nama ;
       ex:nim ?nim ;
       ex:prodi ?prodi .
}
```
Ujicoba SPARQL lainnya yang tersimpan pada [tautan](https://github.com/erickpaulus/SemanticWeb/tree/main/jena-proyek/sparql) ini.
## 4. Akses data dari Python 
- Install Library
```
pip install requests
```
- Arahkan ke folder jena-proyek
- jalankan code app.py
```
python app.py
```
