# -*- coding: utf-8 -*-

'''
A translation function for TIGER 2012 counties
'''

import ogr2osm

class TigerCountiesTranslation(ogr2osm.TranslationBase):
    def filter_tags(self, attrs):
        if not attrs:
            return
        tags = {}
        tags['boundary'] = 'administrative'
        tags['admin_level'] = '6'
        # Names
        if 'NAME' in attrs:
            tags['name'] = attrs['NAME']
        if 'NAMELSAD' in attrs:
            tags['official_name'] = attrs['NAMELSAD']

        # FIPS codes
        if 'STATEFP' in attrs:
            tags['nist:state_fips'] = attrs['STATEFP']
            if 'COUNTYFP' in attrs:
                tags['nist:fips_code'] = attrs['STATEFP'] + attrs['COUNTYFP']

        return tags
