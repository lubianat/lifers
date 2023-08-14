import json

import yaml
from wdcuration import query_wikidata
from pathlib import Path


def generate_experience_pack(pack_id, pack_name, task, creator_name, creator_id, experience_class, sparql_query):
    
    # Fetching results
    results = query_wikidata(sparql_query)
    
    # Formatting the results into the experience pack structure
    entities = []
    
    for result in results:
        entity ={f"{pack_id}_{str(len(entities) + 1)}" :{
            'local_id': len(entities) + 1,
            'name': result['itemLabel'],
            'description': result['description'] if 'description' in result else '',
            'best_image': result['image'] if 'image' in result else '',
            'links': {
                'wikidata': result['item'],
                'wikipedia': result['article'] if 'article' in result else ''
            }
        }}
        entities.append(entity)
    
    # Building the pack
    pack = {
        'name': pack_name,
        'task': task,
        'creator_name': creator_name,
        'creator_id': creator_id,
        'creation_date': '2023-08-11T00:00:00.000Z',  # This can be updated to use the current date
        'id': pack_id,
        'valid_links': ['wikidata', 'wikipedia'],
        'experience_class': experience_class
    }
    
    experience_pack = {
        'entities': entities,
        'pack': pack
    }
    
    return experience_pack







def write_to_yaml(data, pack_id):
    HERE = Path(__file__).parent.resolve()

    filename=HERE.parent / "experience_packs" / f"{pack_id}.yaml"
    with open(filename, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

def main():
      # Example usage:
    sparql_query = """
      SELECT DISTINCT ?item ?itemLabel ?description ?image ?article WHERE {
        ?item wdt:P31/wdt:P279 wd:Q13205267 .  # Change the property and value to what you need. This is for "naked-eye planets"
        ?item wdt:P1215 ?magnitude . 
        FILTER (?magnitude < 5). 
        OPTIONAL { ?item wdt:P18 ?image . }
        OPTIONAL { ?item schema:description ?description . FILTER(LANG(?description) = "en") }
        OPTIONAL { ?article schema:about ?item . ?article schema:inLanguage "en" . ?article schema:isPartOf <https://en.wikipedia.org/>. }
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
      } 
      ORDER BY ?magnitude

  """
    pack_id='naked_eye_planets'
    experience_pack = generate_experience_pack(pack_id='naked_eye_planets', 
                                           pack_name='Solar System - Naked Eye Planets', 
                                           task='See the planets in the sky either with the naked eye. Better done at night!',
                                           creator_name='Tiago Lubiana', 
                                           creator_id='tiagolubiana', 
                                           experience_class='observation', 
                                           sparql_query=sparql_query)

    write_to_yaml(experience_pack, pack_id)

if __name__ == "__main__":
  main()