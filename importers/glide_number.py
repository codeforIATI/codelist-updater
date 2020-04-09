from helpers import source_to_xml


url = 'https://morph.io/codeforIATI/humanitarian-emergency-codelists/' + \
      'data.csv?key=wFTSIH61nwMjLBhphd4T' + \
      '&query=select+%2A+from+%22GLIDE_numbers%22'
lookup = [
    ('code', 'GLIDE_number'),
    ('codeforiati:event-code', 'Event_Code'),
    ('codeforiati:event_en', 'Event'),
    ('codeforiati:country-code', 'Country_Code'),
    ('codeforiati:country_en', 'Country'),
    ('codeforiati:date', 'Date'),
    ('codeforiati:glide-serial', 'Glide_Serial')
]

source_to_xml('GLIDENumber', url, lookup, repo='Unofficial-Codelists')
