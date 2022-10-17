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
    fPoint = open(file_nm,'r')
    lines = fPoint.readlines()
    # print( Lines)
    pts = []
    extent=[]
    for line in lines:
        if line[0] == "#":
            continue
        else:

            # print(line,"  ")
            items=line.split()
            if len(items) == 4:
                extent = [float(items[0]), float(items[1]), float(items[2]), float(items[3])]
            else:
                pt = Point(float(items[0]), float(items[1]))
                # print(pt)
                pts.append(pt)
    strc = StripStructure(extent,no_strips)
    for i in pts:
        strc.append_point(i)
    fPoint.close()
    return strc



def dump(structure, strip_file_nm="strips.wkt", point_file_nm="points.wkt"):
    """Dump the contents of a strip structure to 2 files that can be opened
    with QGIS.
    #points: POINT(30 10)
    # Polygon: POLYGON((10 20,10 30,24 10,10 20))
    Returns - None
    """
    with open(strip_file_nm, "w") as fh:
        fh.write(structure.dumps_strips())
    with open(point_file_nm, "w") as fh:
        fh.write(structure.dumps_points())

