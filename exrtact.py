from owlready2 import get_ontology, sync_reasoner_pellet
import csv

doid_ontology_path = ".../doid.owl"
doid_ontology = get_ontology("file://" + doid_ontology_path).load()


with open('doid_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
   
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['IRI', 'Synonyms', 'definition', 'label'])

 
    for cls in doid_ontology.classes():
        iri = cls.iri
        synonyms = [synonym for synonym in cls.hasExactSynonym] if hasattr(cls, 'hasExactSynonym') else []
        synonym_strings = [str(synonym) for synonym in synonyms]
        
        definition = str(cls.IAO_0000115[0]) if hasattr(cls, 'IAO_0000115') and cls.IAO_0000115 else ""
        label = ', '.join(cls.label) if cls.label else ""

        csv_writer.writerow([iri, '? '.join(synonyms), definition, label])
        
        # Print the extracted values for each class
        print("Class IRI:", cls.iri)
        print(" definition:", definition)
        print("Synonym:", synonym_strings)
        print("Label:", label)
        print("===")  # Separator between classes



#####################################  SYMP  #########################################

symp_ontology_path = "/kaggle/input/predibioonto/symp.owl"
symp_ontology = get_ontology("file://" + symp_ontology_path).load()

with open('symp_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
   
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['IRI', 'Synonyms', 'definition', 'label'])

 
    for cls in symp_ontology.classes():
        iri = cls.iri
        synonyms = [synonym for synonym in cls.hasExactSynonym] if hasattr(cls, 'hasExactSynonym') else []
        synonym_strings = [str(synonym) for synonym in synonyms]
        
        definition = str(cls.IAO_0000115[0]) if hasattr(cls, 'IAO_0000115') and cls.IAO_0000115 else ""
        label = ', '.join(cls.label) if cls.label else ""

        csv_writer.writerow([iri, '? '.join(synonyms), definition, label])






#####################################  DRON  #########################################
dron_ontology_path = "/kaggle/input/predibioonto/dron.owl"
dron_ontology = get_ontology("file://" + dron_ontology_path).load()

with open('dron_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
   
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['IRI', 'Synonyms', 'definition', 'label'])

    dron_classes = [cls for cls in dron_ontology.classes() if str(cls.iri).startswith('http://purl.obolibrary.org/obo/CHEBI_')]
    for cls in dron_classes:
        iri = cls.iri
        synonyms = [synonym for synonym in cls.hasExactSynonym] if hasattr(cls, 'hasExactSynonym') else []
        synonym_strings = [str(synonym) for synonym in synonyms]
        
        definition = str(cls.IAO_0000115[0]) if hasattr(cls, 'IAO_0000115') and cls.IAO_0000115 else ""
        label = ', '.join(cls.label) if cls.label else ""

        csv_writer.writerow([iri,'? '.join(synonyms), definition, label])
