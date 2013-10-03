import sys
import webbrowser
from rdio import Rdio
from rdio_consumer_credentials import *

def main():
    rdio = Rdio((RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET))

    url = rdio.begin_authentication('oob')
    print('Visit: ' + url)
    webbrowser.open(url, new=1, autoraise=True)
    verifier = raw_input('Then enter the PIN: ').strip()
    rdio.complete_authentication(verifier)

    print('\nProcessing...')

    collectionAlbums = rdio.call('getAlbumsInCollection')['result']
    unstreamableAlbums = filter(lambda a: a['canStream'] == False, collectionAlbums)
    percentUnstreamable = int( round( (float(len(unstreamableAlbums)) / float(len(collectionAlbums))) * 100) )

    print('\n' + str(len(unstreamableAlbums)) + ' (' + str(percentUnstreamable) + '%) of the ' + str(len(collectionAlbums)) + ' albums in your Rdio collection are no longer playable.\n')

    sortedUnstreamableAlbums = sorted(unstreamableAlbums, key=lambda album: album['artist'])

    for album in sortedUnstreamableAlbums:
        print(album['artist'] + ' - ' + album['name'] + ' - ' + album['shortUrl'])

if __name__ == '__main__':
    main()
    sys.exit(0)
