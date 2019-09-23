MrMap
=========

Extract place names from a URL or text, and add context to those names

## Install & Setup

Grab the package using `pip` (this will take a few minutes)

    pip install MrMap

MrMap uses [NLTK](http://www.nltk.org/) for entity recognition, so you'll also need
to download the models we're using. Fortunately there's a command that'll take 
care of this for you. 

    MrMap-nltk

## Basic Usage

Import the module, give some text or a URL, and presto.

    import MrMap
    url = 'http://www.bbc.com/news/world-europe-26919928'
    places = MrMap.get_place_context(url=url)

## Credits

MrMap is a fork of [geograpy2](https://github.com/ushahidi/geograpy) and inherits
most of it, but solves several problems and provides continues support in the development

MrMap uses the following excellent libraries:

* [NLTK](http://www.nltk.org/) for entity recognition
* [newspaper3k](https://github.com/codelucas/newspaper) for text extraction from HTML
* [jellyfish](https://github.com/sunlightlabs/jellyfish) for fuzzy text match
* [pycountry](https://pypi.python.org/pypi/pycountry) for country/region lookups

MrMap uses the following data sources:

* [GeoLite2](http://dev.maxmind.com/geoip/geoip2/geolite2/) for city lookups
* [ISO3166ErrorDictionary](https://github.com/bodacea/countryname/blob/master/countryname/databases/ISO3166ErrorDictionary.csv) for common country mispellings _via [Sara-Jayne Terp](https://github.com/bodacea)_

Hat tip to [Dhamodharan](https://github.com/dhamodharanrk) for the name.

Released under the MIT license.