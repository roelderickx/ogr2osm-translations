# ogr2osm-translations

Translations submodule for ogr2osm

## About

In this repository you can find examples of translation files to be used with [ogr2osm](https://github.com/roelderickx/ogr2osm). Please note none of these translations is tested with the latest version.

## Upgrading from a previous version

The translation files currently in use for pnorman's version can not immediately be used in the latest version of ogr2osm. The translation is converted to a class to make the ogr2osm code more maintainable.

This means you need to modify your translation file, but in most cases this is straightforward. The steps below will guide you through the conversion, langleyroad.py is taken as an example:

- At the top of the translation file you need to add `import ogr2osm`
- Next, you need to define a class. The name is not important as long as it is a subclass of `ogr2osm.TranslationBase`.
  For example `class LangleyRoadTranslation(ogr2osm.TranslationBase):`
- Indent the rest of your file to make it part of the class and add the self parameter to all functions. This means the defintion of the translateName function will become `def translateName(self, rawname):`
- Search all calls to these functions and replace them with a call to the class method. The line `translated = translateName(attrs['ROADNAME'].title())` will become `translated = self.translateName(attrs['ROADNAME'].title())`.
- The names of the ogr2osm translation methods have changed somewhat as well, to comply with the pylint standard.
  -  `filterLayer(layer)` has become `filter_layer(self, layer)`
  -  `filterFeature(feature, fieldNames, reproject)` has become `filter_feature(self, ogrfeature, layer_fields, reproject)`. The value passed by layer_fields is the same value as the value passed by fieldNames before.
  -  `filterTags(tags)` has become `filter_tags(self, tags)`
  -  `filterFeaturePost(feature, ogrfeature, ogrgeometry)` has become `process_feature_post(self, osmgeometry, ogrfeature, ogrgeometry)`. The value passed by osmgeometry is the same value as the value passed by feature before.
  -  `preOutputTransform(geometries, features)` has been rewritten to `process_output(self, osmnodes, osmways, osmrelations)`. In stead of passing all geometries as one list you get three separate lists of nodes, ways and relations. The features parameter has been omitted, if you need to know the tags you can find them in the node, way or relation element.

