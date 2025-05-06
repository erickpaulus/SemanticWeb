## What is he Semantic Web stack?
The Semantic Web stack is a common  framework proposed by the W3C to make machines able to process and understand the meaning (semantics) of information on the web. It builds on the existing web architecture and layerly set additional standards and technologies  so that computer  can  interprete data. In general, the Semantic Web stack can be represented as a 7-layered stack, as shown in the figure below.

![Semantic Web Stack](https://www.w3.org/RDF/Metalog/images/sw-tower.png)

*Image credit: [W3C Semantic Web - Easy Guide](https://www.w3.org/RDF/Metalog/docs/sw-easy)*


### Key Layers of Semantic Web stack (from bottom to top):
- URI & Unicode
  - Purpose: Provides a global identification system for resources (URI) and standard character encoding (Unicode).
  - Key point: Foundation for uniquely identifying data on the web.
- XML + XML Namespace
  - Purpose: Defines a syntax for structuring data.
  - Key point: Provides a flexible markup language for exchanging information.
- RDF (Resource Description Framework)
  - Purpose: Provides a data model for describing relationships between resources in subject-predicate-object triples.
  - Key point: Enables basic semantic interoperability.
- RDFS (RDF Schema)
  - Purpose: Extends RDF with vocabulary for describing properties and classes.
  - Key point: Supports basic ontological modeling (hierarchies, domains, ranges).
- OWL (Web Ontology Language)
  - Purpose: Offers richer semantics than RDFS — e.g., equivalent classes, disjoint classes, property restrictions.
  - Key point: Enables complex ontologies and formal reasoning.
- Logic Layer
  - Purpose: Allows inference rules and logical reasoning based on ontologies.
  - Key point: Derives new facts from existing data using reasoners.
- Proof & Trust Layers
  - Purpose:
    - Proof: Verifies inference processes.
    - Trust: Establishes data credibility and authenticity.
  - Key point: Enhances security, provenance, and reliability in semantic data exchange.


### Purpose and Benefits:
- Facilitates data integration, automation, and interoperability across applications.
- Enables intelligent agents to perform complex tasks by understanding linked data.

### References:
- Berners-Lee, T., Hendler, J., & Lassila, O. (2001). The Semantic Web. Scientific American, 284(5), 34–43. https://www.scientificamerican.com/article/the-semantic-web/
- W3C Semantic Web Activity. https://www.w3.org/2001/sw/
- Antoniou, G., & van Harmelen, F. (2004). A Semantic Web Primer. MIT Press.
- Hebeler, J., Fisher, M., Blace, R., Perez-Lopez, A.,, Dean, M.(2009). Semantic Web Programming. Indianapolis, IN: Wiley. ISBN: 978-0-470-41801-7
- http://www.governoaberto.sp.gov.br/wpcontent/uploads/2016/05/Book-Semantic-Web-Guideline.pdf
