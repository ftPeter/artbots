from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier
from svgpathtools import svg2paths, wsvg
paths, attributes = svg2paths('line_segment.svg')
print (paths)

