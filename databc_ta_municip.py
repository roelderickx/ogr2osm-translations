'''
A translation function for DataBC TA_MUNICIP city data. 
'''

import ogr2osm

class TaMunicipTranslation(ogr2osm.TranslationBase):    
    def filter_tags(self, attrs):
        if not attrs:
            return

        tags = {}
        if 'CODE' in attrs and attrs['CODE'] == 'MU':
            if 'MUN_NAME' in attrs:
                tags['boundary'] = 'administrative'
                tags['admin_level'] = '8'
                tags['source'] = 'DataBC TA_MUNICIP'
                tags['name'] = attrs['MUN_NAME'].title()
            else:
                tags['boundary'] = 'administrative'
                tags['admin_level'] = '8'
                tags['source'] = 'DataBC TA_MUNICIP'

        return tags
