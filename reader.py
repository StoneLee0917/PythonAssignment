# GEO1000 - Assignment 3
# Authors:Qiuxian Wei
# Studentnumbers:5801737

from geometry import Point, Rectangle, Circle
from strips import StripStructure


def read(file_nm, no_strips):
    """Reads a file with on the first uncommented line a bbox 
    (4 numbers separated by a space) and subsequently 0 or more lines with 
    points (2 numbers separated by a space) into a Strip Structure.
    
    If no valid box is found in the input file, it returns None.
    Otherwise a StripStructure with 0 or more points is returned.
    
    Returns - None or a StripStructure instance
    """
    fh = open(file_nm, "r")
    lines = fh.read().strip().split("\n")
    strip = None
    has_point = False
    for line in lines:
        if line[0] == '#':
            continue
        else:
            elems = line.split(" ")
            if len(elems) == 4:  # extent
                extent = [float(x) for x in elems]
                strip = StripStructure(extent, no_strips)
            else:  # point
                has_point = True
                strip.append_point(Point(float(elems[0]), float(elems[1])))
    if not has_point:
        return None
    return strip



def dump(structure, strip_file_nm="strips.wkt", point_file_nm="points.wkt"):
    """Dump the contents of a strip structure to 2 files that can be opened
    with QGIS.
    
    Returns - None
    """
    with open(strip_file_nm, "w") as fh:
        fh.write(structure.dump_strips())
    with open(point_file_nm, "w") as fh:
        fh.write(structure.dump_points())

