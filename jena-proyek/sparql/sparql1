1. SPARQL Sederhana – Tampilkan semua mahasiswa
```
PREFIX ex: <http://example.org/ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?nama ?nim ?prodi
WHERE {
  ?mhs a ex:Mahasiswa ;
       foaf:name ?nama ;
       ex:nim ?nim ;
       ex:prodi ?prodi .
}
```
2. SPARQL Menengah – Tampilkan mahasiswa dan mata kuliah yang diambil
```
PREFIX ex: <http://example.org/ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?nama ?namaMatkul
WHERE {
  ?mhs a ex:Mahasiswa ;
       foaf:name ?nama ;
       ex:mengambilMatkul ?matkul .
  ?matkul ex:namaMatkul ?namaMatkul .
}
```
3. SPARQL Menengah – Siapa saja dosen dan mata kuliah yang diajarkan
```
PREFIX ex: <http://example.org/ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?namaDosen ?namaMatkul
WHERE {
  ?dosen a ex:Dosen ;
         foaf:name ?namaDosen ;
         ex:mengajarMatkul ?matkul .
  ?matkul ex:namaMatkul ?namaMatkul .
}
```
4. SPARQL Kompleks – Mahasiswa, mata kuliah yang diambil, dan dosen pengajar
```
PREFIX ex: <http://example.org/ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?namaMahasiswa ?namaMatkul ?namaDosen
WHERE {
  ?mhs a ex:Mahasiswa ;
       foaf:name ?namaMahasiswa ;
       ex:mengambilMatkul ?matkul .
  ?matkul ex:namaMatkul ?namaMatkul .
  ?dosen a ex:Dosen ;
         ex:mengajarMatkul ?matkul ;
         foaf:name ?namaDosen .
}
```
5. SPARQL Kompleks – Total SKS yang diambil oleh setiap mahasiswa
```
PREFIX ex: <http://example.org/ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?namaMahasiswa (SUM(?sks) AS ?totalSKS)
WHERE {
  ?mhs a ex:Mahasiswa ;
       foaf:name ?namaMahasiswa ;
       ex:mengambilMatkul ?matkul .
  ?matkul ex:sks ?sks .
}
GROUP BY ?namaMahasiswa
```
