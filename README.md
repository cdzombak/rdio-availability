# rdio-availability

Lists the albums in your [Rdio](http://rdio.com) collection which are no longer available for streaming, for [any of a variety of reasons](http://help.rdio.com/customer/portal/articles/58995).

## Usage

`python rdio-availability.py`

The script will prompt you to visit a web oage to complete OAuth authorization with Rdio. This authorization is only used once when you run the script; if you run the script again you'll be re-prompted to authorize.

## Requirements

Python 2.6, 2.7. Might work on 2.5 or 3.x; I haven't tested.

## Sample Output

    Visit: https://www.rdio.com/oauth/authorize/?oauth_token=xxx
    Then enter the PIN: 1234

    Processing...

    13 (6%) of the 208 albums in your Rdio collection are no longer playable.

    Ferry Corsten - Beautiful
    Tegan and Sara - Closer
    Swedish House Mafia - Don't You Worry Child (Radio Edit) [feat. John Martin]
    Foo Fighters - Echoes, Silence, Patience & Grace
    Philip Glass - Einstein on the Beach
    Philip Glass - Music With Changing Parts
    Jon Hopkins - Opalescent
    Four Tet - Pause
    Four Tet - Ringer
    Four Tet - Rounds
    Shields Brothers - Run Away With Me
    Skyfall, Let the Sky Fall, So Let the Sky Fall - Skyfall, Let the Sky Fall, So Let the Sky Fall - Single (ADELE / James Bond - at as Skyfalls Tribute)
    Four Tet - There Is Love In You

# Author

Chris Dzombak <[chris.dzombak.name](http://chris.dzombak.name)>

* twitter [@cdzombak](https://twitter.com/cdzombak)
* ADN [@dzombak](https://alpha.app.net/dzombak)
