# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:

from reader import read
from geometry import Rectangle, Circle, Point
from os.path import basename


def parse(geom_str):
    """Parse a string into a shape object (Point, Circle, or Rectangle)
    # 输入的啥，返回输入点的类型
    Formats that can be given:
    p <px> <py>
    c <cx> <cy> <r>
    r <llx> <lly> <urx> <ury>
    
    Returns - Point, Circle, or Rectangle
    """
    geom_list=geom_str.split()
    # print(len(geom_list))
    if geom_list[0]=='p' and len(geom_list)==3:
        pt=Point(float(geom_list[1]),float(geom_list[2]))
        # print("是个点",pt.x,' ',pt.y)
        return pt
    elif geom_list[0]=='c' and len(geom_list)==4:
        cir_center=Point(float(geom_list[1]),float(geom_list[2]))
        cir_rad=float(geom_list[3])
        cir=Circle(cir_center,cir_rad)
        # print("Circle!",cir.center.x,' ',cir.center.y,' ',cir.radius)
        return cir
    elif geom_list[0]=='r' and len(geom_list)==5:
        rec_ll=Point(float(geom_list[1]),float(geom_list[2]))
        rec_ur=Point(float(geom_list[3]),float(geom_list[4]))
        rec=Rectangle(rec_ll,rec_ur)
        return rec
    else:
        print("input format wrong!")
        return 0



def print_statistics(result):
    """Prints statistics for the resulting list of Points of a query
    
    * Number of points overlapping (i.e. number of points in the list)
    * The leftmost point and its identity given by the id function
    * The rightmost point and its identity given by the id function
    
    Returns - None
    """
    print(len(result))
    x_cor=[]
    # 将x坐标放入list里排序，再用if和最左最右x坐标回找点及其id
    for i in result:
        x_cor.append(i.x)
    # print(sorted(x_cor))
    for i in result:
        if i.x==sorted(x_cor)[0]:
            print("left  ",i.x,' ',i.y, ' ',id(i))
        elif i.x==sorted(x_cor)[len(result)-1]:
            print("right  ",i.x,' ',i.y,' ',id(i))

def print_help():
    """Prints a help message to the user, what can be done with the program.
    """
    helptxt = """
Commands available:
-------------------
General:
    help
    quit

Reading points in a structure, defining how many strips should be used:
    open <filenm> into <number_of_strips>

Querying:
    with a point:     p <px> <py>
    with a circle:    c <cx> <cy> <radius>
    with a rectangle: r <llx> <lly> <urx> <ury>"""
    print(helptxt)

# =============================================================================
# Below are some commands that you may use to test your codes:
# open points2.txt into 5
# p 5.0 5.0
# c 10.0 10.0 1.0
# r 2.0 2.0 8.0 4.0
# =============================================================================
def main():
    """The main function of this program.
    """
    structure = None
    print("Welcome to {0}.".format(basename(__file__)))
    print("=" * 76)
    print_help()
    while True:
        in_str = input("your command>>>\n").lower()
        if in_str.startswith("quit"):#判断用户输入的字符串0是否以quit开始
            print("Bye, bye.")
            return
        elif in_str.startswith("help"):
            print_help()
        elif in_str.startswith("open"):
            filenm, nstrips = in_str.replace("open ", "").split(" into ")
            structure = read(filenm, int(nstrips))

            structure.print_strip_statistics()
        elif in_str.startswith("p") or in_str.startswith("c") or in_str.startswith("r"):
            if structure is None:
                print("No points read yet, open a file first!")
            else:
                print_statistics(structure.query(parse(in_str)))


if __name__ == "__main__":
    main()
    parse("c 2.0 3.0 5.5")