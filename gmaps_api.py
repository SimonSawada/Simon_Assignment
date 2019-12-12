import googlemaps

from algoliasearch.search_client import SearchClient

client = SearchClient.create('RSBCBF0EG8','362a46f9db7603d913d9f4eea9a47fde')
index = client.init_index('Simon_test_wine')
gmaps = googlemaps.Client(key='AIzaSyBHAFJQ8hdhQCEscOUXKfqD_GDo4HJ-6Xo')



query = ''
res = index.browse_objects({'query': query, 'filters':'country:France'})

for hit in res:
    print(hit["winery"] + " winery")
    geocode_result = gmaps.geocode(hit["winery"] + " winery")
    if (geocode_result):
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
        index.partial_update_object({'objectID': hit["objectID"], '_geoloc': {'lat': lat, 'lng': lng}},
                                    {'createIfNotExists': 'true'})
        print(hit["winery"])


query = ''
res = index.browse_objects({'query': query})

i=0
for hit in res:
    index.partial_update_object({'objectID':hit["objectID"],'img':"https://sc01.alicdn.com/kf/HTB1rPxCX6LuK1Rjy0Fhq6xpdFXaA/wine-bottle.jpg"},
                                {'createIfNotExists':'true'})
    i = i + 1
    print(i)


