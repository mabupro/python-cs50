# $ pip install requests
# Successfully installed charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.2.1

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())

# $ python itunes.py weezer
# {'resultCount': 1, 'results': [{'wrapperType': 'track', 'kind': 'song', 'artistId': 115234, 'collectionId': 1440878798, 'trackId': 1440879325, 'artistName': 'Weezer', 'collectionName': 'Weezer', 'trackName': 'Buddy Holly', 'collectionCensoredName': 'Weezer', 'trackCensoredName': 'Buddy Holly', 'artistViewUrl': 'https://music.apple.com/us/artist/weezer/115234?uo=4', 'collectionViewUrl': 'https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4', 'trackViewUrl': 'https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4', 'previewUrl': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/f0/ba/a8/f0baa81a-7449-c490-f43a-b5c6e3609e3f/mzaf_3988310882581261442.plus.aac.p.m4a', 'artworkUrl30': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/30x30bb.jpg', 'artworkUrl60': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/60x60bb.jpg', 'artworkUrl100': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/100x100bb.jpg', 'collectionPrice': 10.99, 'trackPrice': 1.29, 'releaseDate': '1994-02-28T12:00:00Z', 'collectionExplicitness': 'notExplicit', 'trackExplicitness': 'notExplicit', 'discCount': 1, 'discNumber': 1, 'trackCount': 10, 'trackNumber': 4, 'trackTimeMillis': 159587, 'country': 'USA', 'currency': 'USD', 'primaryGenreName': 'Pop', 'isStreamable': True}]}

# print(json.dumps(response.json(), indent=2))

# $ python itunes.py weezer
# {
#   "resultCount": 1,
#   "results": [
#     {
#       "wrapperType": "track",    
#       "kind": "song",
#       "artistId": 115234,        
#       "collectionId": 1440878798,
#       "trackId": 1440879325,     
#       "artistName": "Weezer",    
#       "collectionName": "Weezer",
#       "trackName": "Buddy Holly",
#       "collectionCensoredName": "Weezer",
#       "trackCensoredName": "Buddy Holly",
#       "artistViewUrl": "https://music.apple.com/us/artist/weezer/115234?uo=4",
#       "collectionViewUrl": "https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4",
#       "trackViewUrl": "https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4",
#       "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview112/v4/f0/ba/a8/f0baa81a-7449-c490-f43a-b5c6e3609e3f/mzaf_3988310882581261442.plus.aac.p.m4a",
#       "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/30x30bb.jpg",
#       "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/60x60bb.jpg",
#       "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/fc/74/67/fc74674a-1eb0-d50d-33fe-215caee529d1/16UMGIM52971.rgb.jpg/100x100bb.jpg",
#       "collectionPrice": 10.99,
#       "trackPrice": 1.29,
#       "releaseDate": "1994-02-28T12:00:00Z",
#       "collectionExplicitness": "notExplicit",
#       "trackExplicitness": "notExplicit",
#       "discCount": 1,
#       "discNumber": 1,
#       "trackCount": 10,
#       "trackNumber": 4,
#       "trackTimeMillis": 159587,
#       "country": "USA",
#       "currency": "USD",
#       "primaryGenreName": "Pop",
#       "isStreamable": true
#     }
#   ]
# }

o = response.json()
for result in o["results"]:
    print(result["trackName"])

# $ python itunes.py weezer
# Buddy Holly