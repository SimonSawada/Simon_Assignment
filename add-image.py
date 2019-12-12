from algoliasearch.search_client import SearchClient

client = SearchClient.create('RSBCBF0EG8','362a46f9db7603d913d9f4eea9a47fde')
index = client.init_index('Simon_test_wine')




query = ''
res = index.browse_objects({'query': query})

i=0
for hit in res:
    index.partial_update_object({'objectID':hit["objectID"],'img':"https://sc01.alicdn.com/kf/HTB1rPxCX6LuK1Rjy0Fhq6xpdFXaA/wine-bottle.jpg"},
                                {'createIfNotExists':'true'})
    i = i + 1
    print(i)


