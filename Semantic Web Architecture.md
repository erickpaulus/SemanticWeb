The semantic web architecture is built on a stack of components, as shown in the image below.
![Semantic Web Architecture](https://upload.wikimedia.org/wikipedia/en/3/37/Semantic-web-stack.png?20080518142307)

*This image is taken from [Wikipedia](https://en.wikipedia.org/wiki/File:Semantic-web-stack.png).*

1. URI and Unicode (Foundation Layer)
   - *URI (Uniform Resource Identifier)* is used to uniquely identify resources (documents, people, concepts, etc.) on the web.
   - *Unicode* is a universal character encoding standard to represent text in most languages.
2. XML, XML Namespace, XML Schema
   - XML (eXtensible Markup Language) is a flexible markup language for structuring and storing data.
   - XML Namespace is to prevent naming conflicts between elements from different vocabularies.
   - XML Schema is to define the structure, content, and data types in XML documents.

  While XML itself isn’t a semantic web technology, it's used for interoperability and data transport.

3. RDF (Resource Description Framework)
     - RDF provides a standard model for data interchange on the web using triples: Subject – Predicate – Object.
  
    Example:
    ```
    <John> <hasFriend> <Mary>
    John is the subject
    hasFriend is the predicate (property)
    Mary is the object
    ```
  
    RDF is the foundation for expressing relationships in semantic form.

4. RDFS (RDF Schema)
   - RDFS extends RDF by defining vocabularies — such as classes and properties.

    Examples:
    ```
    Define Person as a class
    Define that hasFriend relates Person to another Person
    ```
    RDFS enables basic semantic definitions (taxonomies, class hierarchies).

5. OWL (Web Ontology Language)
   - OWL provides a richer vocabulary and more complex semantics than RDFS.
   - Additional features:
       - Class hierarchies
       - Property constraints (e.g., cardinality)
       - Logical relationships (e.g., equivalence, disjointness)
    - OWL variants:
        - OWL Lite: Simplified, for simple hierarchies
        - OWL DL: Balances expressiveness and computational completeness
        - OWL Full: Maximum expressiveness (less computational guarantees)

    - OWL allows building formal ontologies — structured knowledge models.

6. SPARQL
    - SPARQL is a query language for RDF data (like SQL for relational databases).
    - Enables querying, filtering, and manipulating RDF triples.
    - SPARQL is used to retrieve and operate on data in semantic web systems.

7. Logic Layer (Inference & Reasoning)
     - Applies logic rules to infer new knowledge from existing data.

    Example:
    ```
    If A is a parent of B, and B is a parent of C, then A is a grandparent of C.
    ```
    This enables automated reasoning and deduction.

8. Proof Layer
    - Describes how inferences were made — traceable justifications.
    - Useful for:
        - Transparency
        - Debugging reasoning processes
        - Verifying correctness

    - Ensures that results from reasoning can be trusted and traced.

9. Trust Layer
    - Ensures trustworthiness of information and sources.
    - Involves:
        - Digital signatures
        - Source credibility
        - Provenance and reputation

    - Crucial for validating data in open and decentralized systems like the web.
