import sys
from rdio import Rdio
from rdio_consumer_credentials import *

def main():
    rdio = Rdio((RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET))

    url = rdio.begin_authentication('oob')
    print('Visit: ' + url)
    verifier = raw_input('Then enter the PIN: ').strip()
    rdio.complete_authentication(verifier)

    print('\nProcessing...')

    # find out what playlists you created
    collectionAlbums = rdio.call('getAlbumsInCollection')['result']
    unstreamableAlbums = filter(lambda a: a['canStream'] == False, collectionAlbums)
    percentUnstreamable = int( round( (float(len(unstreamableAlbums)) / float(len(collectionAlbums))) * 100) )

    print('\n' + str(len(unstreamableAlbums)) + ' (' + str(percentUnstreamable) + '%) of the ' + str(len(collectionAlbums)) + ' albums in your Rdio collection are no longer playable.\n')

    for a in unstreamableAlbums:
        print(a['artist'] + ' - ' + a['name'])

if __name__ == '__main__':
    main()
    sys.exit(0)
