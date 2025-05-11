Query: tampilkan Mahasiswa dan Dosen Pengajarnya
```
PREFIX ex: <http://example.org/ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?namaMhs ?namaMatkul ?namaDosen
WHERE {
  ?mhs a ex:Mahasiswa ;
       foaf:name ?namaMhs ;
       ex:mengambilMatkul ?matkul .
       
  ?matkul ex:namaMatkul ?namaMatkul .

  ?dosen a ex:Dosen ;
         foaf:name ?namaDosen ;
         ex:mengajarMatkul ?matkul .
}
```

Query: Di ruang mana mata kuliah "Pemrograman Dasar" berlangsung dan pada hari apa?
```
PREFIX ex: <http://example.org/ns#>

SELECT ?namaMatkul ?ruang ?hari ?jam
WHERE {
  ?jadwal a ex:Jadwal ;
          ex:untukMatkul ?matkul ;
          ex:dijadwalkanDi ?ruangObj ;
          ex:beradaPadaHari ?hari ;
          ex:berlangsungPadaJam ?jam .

  ?matkul ex:namaMatkul ?namaMatkul .
  ?ruangObj ex:namaRuang ?ruang .
}
```
Query Kompleks: Mahasiswa, prodi-nya, dan ruangan kuliah yang dia datangi
```
PREFIX ex: <http://example.org/ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?namaMahasiswa ?namaProdi ?namaMatkul ?ruang
WHERE {
  ?mhs a ex:Mahasiswa ;
       foaf:name ?namaMahasiswa ;
       ex:mengikutiProdi ?prodi ;
       ex:mengambilMatkul ?matkul .

  ?prodi ex:namaProdi ?namaProdi .
  ?matkul ex:namaMatkul ?namaMatkul .

  ?jadwal ex:untukMatkul ?matkul ;
          ex:dijadwalkanDi ?ruangObj .

  ?ruangObj ex:namaRuang ?ruang .
}
```
