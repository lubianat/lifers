# Lifers

## Concept


Lifers is an application for technology-powered joyful experience of life! 


It aims at extending the concept of "lifers" in birdwatching - i.e. seen a bird species for the first time - to other realms of human experience. 

It can be used for people wanting to collect experiences about anything: books, planes, trains, cars, constellations, soccer clubs, natural history museums, paradisiac beaches in northwestern Brazil, anything!

Lifers plays with a general protocol for observations of _anything_. The idea starts with observation, but can be extended to any experiences such as driving particular vehicles or eating particular types of food. 

Anything that the user wants to experience in an organized, information-rich and gamified fashion can be added as an _experience pack_ to Lifers. 


Let's consider a simple pack called "coolest constellations" comprising of entries for Orion, Scorpion and Ursa Major. Each experience pack also describes what counts as an experience. In this case, it could be "identification through naked eye or optical equipments of the general outline and major features of a constellation.". 

The pack will contain basic information about these entities, as well as links to learn more, similar to how iNaturalist handles species and how eBird handles their Merlin app. 


Like on eBird mobile, users will be able to submit lists of observations, or experiences both live during an _observation sprint_, which will record the observations in a particular date in a particular localization, or as a historical observation. For example, if I saw Orion, in São Paulo - Brazil in December 10th 2022, it will be recorded as so, with optional notes. If I am sure I saw the Ursa Major, but I do not know where and when, I can still add it as a past observation. 


Users will be able to browse previous lists, to see their life-list for each observation pack, see maps and timelines of observation and share their profiles with other users. 

## Implementation

### Experience packs

Experience packs will be comprised of yaml files containing the core observations to be made and some additional information to be parsed by the app. 

Here is the basic outline of an incomplete experience pack: 

```
---
entities:
- best_image: http://commons.wikimedia.org/wiki/Special:FilePath/Planet%20Venus%20im%20Deutschen%20Museum.jpg
  description: planet second-closest to the Sun in the Solar System
  global_id: naked_eye_planets_1
  links:
    wikidata: http://www.wikidata.org/entity/Q313
    wikipedia: https://en.wikipedia.org/wiki/Venus
  local_id: 1
  name: Venus
pack:
  - name: Solar System - Naked Eye Planets
  - task: See the planets in the sky either with the naked eye. Better done at night!
  - creator_name: Tiago Lubiana
  - creator_id: tiagolubiana
  - creation_date: 2023-08-11T00:00:00.000Z
  - id: naked_eye_planets
  - valid_links: wikidata, wikipedia
  - experience_class: observation
``` 


Experience packs will be customized depending on user cases.

The `entities` section will contain the information for each of the entities in the pack. 
Each entity is identified in the ymal via a global id, a combination of the pack.id and the entity.local_id. 
The following information bits are available for each entity: 

 * `local_id`: A non-padded integer, starting in 1 
 * `name`: The best name for the entity. At first, only English will be supported. 
 * `description`: A basic, plain-text, description for the entity.
 * `best_image`: The URL for the best image for the entity, to be rendered in the app.
 * `links`: A set of external links for reference. Each link is preceded by a prefix, outlined in pack.valid_links. The Lifer app needs to know how  to handle those links for visualization.


A second section, called `pack` will hold the metadata for this experience pack, including: 

* `name`: The preferred name for the pack, to be shown on the app
* `task`: The task the user needs to do to experience/observe an entity in the context of the pack 
* `creator_name`, `creator_id` and `creation_date`: basic metadata
* `id`: The global id for the pack (lowercase alphanumeric readable string split by underline)
* `valid links`: The valid links for this pack. The first iterations of the app will have only two possibilities: Wikidata and Wikipedia (for English Wikipedia)
* `experience_class`: There are 2 main types of experience_classes a priori: observation and interaction. The  logical "ownership" class is explicitly avoided at the moement- lets not get too materialistic 

A generator of experience packs using Wikidata will be available, where given a SPARQL query, the user can configure a premade pack
