# Description: Add to an existing selection based on an attribute query
 
# Import system modules
import arcpy

# Include trunks in primary road, use REMOVE_FROM_SELECTION to remove
arcpy.SelectLayerByAttribute_management("clipped_roads_openstreetmap_primary", "ADD_TO_SELECTION", "fclass = 'trunk'", "NON_INVERT")
