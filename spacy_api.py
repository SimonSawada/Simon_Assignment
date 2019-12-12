import googlemaps
import spacy

from algoliasearch.search_client import SearchClient

client = SearchClient.create('RSBCBF0EG8','362a46f9db7603d913d9f4eea9a47fde')
index = client.init_index('Simon_test_wine')
gmaps = googlemaps.Client(key='AIzaSyBHAFJQ8hdhQCEscOUXKfqD_GDo4HJ-6Xo')


nlp = spacy.load("en_core_web_sm")

query = ''
res = index.browse_objects({'query': query, 'filters':'country:France'})


i=0
for hit in res:
    text=hit["description"]
    doc = nlp(text)
    if (doc):
        index.partial_update_object({'objectID': hit["objectID"], 'tags': [chunk.text for chunk in doc.noun_chunks if chunk.text in list]},
                                    {'createIfNotExists': 'true'})




list=['acidity',
'tannins',
'wood',
'fruit',
'structure',
'Citrus',
'minerality',
'honey',
'fruity',
'firm tannins',
'vanilla',
'soft tannins',
'sweetness',
'fresh acidity',
'ripe fruit',
'dry tannins',
'pepper',
'caramel',
'lemon',
'Peach',
'apricot',
'complexity',
'red fruits',
'plum',
'dark tannins',
'almonds',
'yellow fruits',
'apple',
'bright acidity',
'chocolate',
'intense acidity',
'licorice',
'Black fruits',
'pineapple',
'cherry',
'melon',
'raspberry',
'herbs',
'mango',
'pink grapefruit',
'berry fruits',
'smoke']







# query = ''
# res = index.browse_objects({'query': query})
#
# i=0
# for hit in res:
#     index.partial_update_object({'objectID':hit["objectID"],'img':"https://sc01.alicdn.com/kf/HTB1rPxCX6LuK1Rjy0Fhq6xpdFXaA/wine-bottle.jpg"},
#                                 {'createIfNotExists':'true'})
#     i = i + 1
#     print(i)

#

# Geocoding an address
# geocode_result = gmaps.geocode('De Ladoucette winerie')
# print(geocode_result)
#
# lat=geocode_result[0]["geometry"]["location"]["lat"]
# lng=geocode_result[0]["geometry"]["location"]["lng"]
# print(lat)
# print(lng)












#[0]["geometry"]["location"]["lat"]

