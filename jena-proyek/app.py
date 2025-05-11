import requests

fuseki_url = "http://localhost:3030/mahasiswa-db/sparql"
query = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX ex: <http://example.org/ns#>

SELECT ?nama ?nim ?jurusan WHERE {
  ?mhs a ex:Mahasiswa ;
       foaf:name ?nama ;
       ex:nim ?nim ;
       ex:jurusan ?jurusan .
}
"""

params = {
    'query': query
}

headers = {
    'Accept': 'application/sparql-results+json'
}

response = requests.get(fuseki_url, params=params, headers=headers)

data = response.json()

for result in data["results"]["bindings"]:
    print("Nama:", result["nama"]["value"])
    print("NIM:", result["nim"]["value"])
    print("Jurusan:", result["jurusan"]["value"])
    print("---")
