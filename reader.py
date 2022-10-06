# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:

from geometry import Point, Rectangle, Circle
from strips import StripStructure


def read(file_nm, no_strips):#文件名，数据分列的列数
    """Reads a file with on the first uncommented line a bounding box
    (4 numbers separated by a space) and subsequently 0 or more lines with 
    points (2 numbers separated by a space) into a Strip Structure.
    
    If no valid box is found in the input file, it returns None.
    Otherwise a StripStructure with 0 or more points is returned.
    
    Returns - None or a StripStructure instance
    """
    fPoint==open(file_nm,'r')
    for i in fPoint:
        if eachLine[0]=="#":
            continue
        else:
            print(i,"  ")
            lines = fh.read().split("\n")
            for line in lines:
                items = line.split()
                temp = []
                temp.append(float(items[0].strip()[0]), float(items[0].strip()[1]), float(items[0].strip()[3]), float(items[0].strip()[4]))
                for pt in pts:
                    pt(float(item.strip()[0]), float(item.strip()[1]))
            sort(pts.x)
        fPoint.close()
    pass


def dump(structure, strip_file_nm="strips.wkt", point_file_nm="points.wkt"):
    """Dump the contents of a strip structure to 2 files that can be opened
    with QGIS.
    #points: POINT(30 10)
    # Polygon: POLYGON((10 20,10 30,24 10,10 20))
    Returns - None
    """
    with open(strip_file_nm, "w") as fh:
        fh.write(structure.dump_strips())
    with open(point_file_nm, "w") as fh:
        fh.write(structure.dump_points())

