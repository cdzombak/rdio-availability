# rdio-availability

Lists the albums in your [Rdio](http://rdio.com) collection which are no longer available for streaming, for [any of a variety of reasons](http://help.rdio.com/customer/portal/articles/58995).

## Cloning

    git clone https://github.com/cdzombak/rdio-availability.git
    cd rdio-availability
    git submodule update --init

## Usage

`python rdio-availability.py`

The script will prompt you to complete OAuth authorization with Rdio. This authorization is only used once when you run the script; if you run the script again you'll be re-prompted to authorize.

## Requirements

Python 2.6, 2.7. Might work on 2.5 or 3.x; I haven't tested.

## Sample Output

    Visit: https://www.rdio.com/oauth/authorize/?oauth_token=xxx
    Then enter the PIN: 1234

    Processing...

    20 (8%) of the 249 albums in your Rdio collection are no longer playable.

    Above & Beyond - Black Room Boy - http://rd.io/x/QVknEyJ378o/
    Above & Beyond - Group Therapy - http://rd.io/x/QVknEyJTFLI/
    Ferry Corsten - Beautiful - http://rd.io/x/QVknEyJe3AU/
    Ferry Corsten - Junk - http://rd.io/x/QVknEyJdtjs/
    Ferry Corsten - L.E.F. Bundle - http://rd.io/x/QVknEyJe0Ks/
    Ferry Corsten - Twice In A Blue Moon Remixed - http://rd.io/x/QVknEyJdt0U/
    Ferry Corsten - WKND - http://rd.io/x/QVknEyJKIJM/
    Four Tet - Pause - http://rd.io/x/QVknEyJdWK0/
    Four Tet - Ringer - http://rd.io/x/QVknEyJdjEk/
    Four Tet - Rounds - http://rd.io/x/QVknEyJdWWk/
    Four Tet - There Is Love In You - http://rd.io/x/QVknEyJdSPo/
    Lorde - The Love Club EP - http://rd.io/x/QVknEyJ3Gu8/
    Lorde - Tennis Court - http://rd.io/x/QVknEyJxrtc/
    Paul Simon - The Paul Simon Collection: On My Way, Don't Know Where I'm Going - http://rd.io/x/QVknEyJby3k/
    Philip Glass - Einstein on the Beach - http://rd.io/x/QVknEyJaO0M/
    Philip Glass - Music With Changing Parts - http://rd.io/x/QVknEyJexCg/
    Shields Brothers - Run Away With Me - http://rd.io/x/QVknEyJFkEc/
    deadmau5 - 4x4=12 - http://rd.io/x/QVknEyJWRy4/
    deadmau5 - > album title goes here < - http://rd.io/x/QVknEyJCs-c/
    deadmau5 - The Veldt EP - http://rd.io/x/QVknEyJHiUA/

# Author

Chris Dzombak <[chris.dzombak.name](http://chris.dzombak.name)>

* twitter [@cdzombak](https://twitter.com/cdzombak)
* ADN [@dzombak](https://alpha.app.net/dzombak)
