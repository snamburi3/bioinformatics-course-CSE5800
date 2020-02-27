import sys
import math

def distance_between_points(x, y):
    """
    distance between two points with the coordinates (x1, y1) and (x2, y2).
    D=√(x2−x1)2+(y2−y1)2
    """
    all_distances = []
    zipped = zip(x,y)
    for z in zipped:
        z1, z2 = z
        all_distances.append((z1-z2)**2)
    return math.sqrt(sum(all_distances))


def squared_error_distortion(centers, data):
    sum_distortion = []
    for d in data:
        nearest_centers = {}
        for c in centers:
            distance_nc = distance_between_points(d, c)
            nearest_centers[distance_nc] = c
        nearest_center = nearest_centers[min(nearest_centers.keys())]
        distance = distance_between_points(d, nearest_center)**2
        sum_distortion.append(distance)
    return (sum(sum_distortion)/len(data))


# read centers and data
fh = open(sys.argv[1], 'r')
k = fh.readline().strip()

centers = []
data = []
flag = False
for line in fh.readlines():
    if line.startswith('-'):
        flag = True
        continue
    if flag:
        data.append(tuple(map(float, line.strip().split())))
    else:
        centers.append(tuple(map(float, line.strip().split())))
print (round((squared_error_distortion(centers, data)),3))


