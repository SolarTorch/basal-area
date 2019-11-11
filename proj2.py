from __future__ import division

from visual import *
from visual.graph import *

import math,random


width = 300
height = 300
obv_point = [[vector(0,0,0)]*5 for i in range(5)]

for i in range(5):
    for j in range(5):
        obv_point[i][j] = vector(width*(1/10+i/5),height*(1/10+j/5),0)

print obv_point


scene = display(title='Estimating Timber',
                 width=width, height=height,
                 center=obv_point[2][2], background=color.white)


number = 20000    #number of trees
theta = 12       #angle of prism
threshold = math.tan(theta*pi/360)
print threshold

r_min = 0.10    #min radius of trees
r_max = 0.75    #max radius of trees
h_fix = 10      #fix the height of trees be 10 meters

trees = []      #set of trees

tree_empty = cylinder(pos = vector(0,0,0),
                      axis = vector(0,0,0),
                      radius = 0)


def set_up_field(number):
    count = 0
    for i in range(number+1):
        if (i == 0):
            trees.append(tree_empty)
        else:
            pos = vector(random.uniform(0,height),random.uniform(0,width),0)
            r = random.uniform(r_min,r_max)
            if (mag(pos-trees[i-1].pos) < r+trees[i-1].radius):
                trees.append(tree_empty)
                count += 1
            else:
                trees.append(cylinder(pos = pos,
                              axis = vector(0,0,h_fix),
                              radius = r,
                              color = color.orange))
    return count

ava_trees = number - set_up_field(number)
print ava_trees




def countable(distance,radius):
    output = 0
    if (radius/distance > threshold):
        output += 1
    elif (radius/distance == threshold):
          output += 1/2
    else:
          output += 0
    return output

def count_tree(vec):
    count_1 = 0
    for i in range(1,ava_trees):
          d = mag(vec-trees[i].pos)
          r = trees[i].radius
          count_1 += countable(d,r)
    return count_1

for i in range(5):
    for j in range(5):
        print count_tree(obv_point[i][j])
