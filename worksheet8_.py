import math
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = float(x); self.y = float(y)
    def __repr__(self):
        return f"Point({self.x:.4f}, {self.y:.4f})"
    def as_array(self):
        return np.array([self.x, self.y])

def distance(a: Point, b: Point):
    return np.linalg.norm(a.as_array() - b.as_array())

def midpoint(a: Point, b: Point):
    return Point((a.x + b.x)/2, (a.y + b.y)/2)

def line_equation(a: Point, b: Point):
    if b.x == a.x:
        return None, a.x  
    m = (b.y - a.y) / (b.x - a.x)
    c = a.y - m * a.x
    return m, c

def reflect_point_over_line(A: Point, B: Point, C: Point):
   
    p = C.as_array()
    a = A.as_array()
    b = B.as_array()
   
    d = b - a
    d_unit = d / np.dot(d, d)
  
    proj = a + d * np.dot(p - a, d) / np.dot(d, d)
    reflected = proj*2 - p
    return Point(reflected[0], reflected[1])


class Vec:
    def __init__(self, x, y):
        self.v = np.array([float(x), float(y)])
    def __add__(self, other):
        return Vec(*(self.v + other.v))
    def magnitude(self):
        return np.linalg.norm(self.v)
    def dot(self, other):
        return float(np.dot(self.v, other.v))
    def angle_with(self, other):
        dot = self.dot(other)
        mag = self.magnitude() * other.magnitude()
        if mag == 0:
            return 0.0
        cos = max(-1.0, min(1.0, dot/mag))
        return math.degrees(math.acos(cos))
    def projection_onto(self, other):
        
        denom = np.dot(other.v, other.v)
        if denom == 0:
            return Vec(0,0)
        scalar = np.dot(self.v, other.v) / denom
        proj = scalar * other.v
        return Vec(proj[0], proj[1])
    def __repr__(self):
        return f"Vec({self.v[0]:.4f}, {self.v[1]:.4f})"


def segment_length(S: Point, E: Point):
    return distance(S,E)

def closest_point_on_segment(S: Point, E: Point, P: Point):
    s = S.as_array(); e = E.as_array(); p = P.as_array()
    se = e - s
    if np.allclose(se, 0):
        return S
    t = np.dot(p - s, se) / np.dot(se, se)
    t_clamped = max(0, min(1, t))
    closest = s + t_clamped * se
    return Point(closest[0], closest[1])

def dist_point_to_segment(S: Point, E: Point, P: Point):
    cp = closest_point_on_segment(S,E,P)
    return distance(P, cp), cp


def intersect_lines(a1,b1,c1, a2,b2,c2):
   
    D = a1*b2 - a2*b1
    if abs(D) < 1e-12:
        return None  
    x = (c1*b2 - c2*b1) / D
    y = (a1*c2 - a2*c1) / D
    return Point(x,y)


if __name__ == "__main__":
    
    A = Point(1,2); B = Point(4,6)
    print("Distance A-B:", distance(A,B))
    print("Midpoint:", midpoint(A,B))
    m,c = line_equation(A,B)
    if m is None:
        print(f"Line is vertical: x = {c}")
    else:
        print(f"Line: y = {m:.4f}x + {c:.4f}")
    C = Point(2,0)
    print("Reflection of C over AB:", reflect_point_over_line(A,B,C))

    # Q2 vectors
    va = Vec(1,2); vb = Vec(3,4); vc = Vec(-1,1)
    R = va + vb + vc
    print("Resultant R:", R)
    print("Magnitudes:", va.magnitude(), vb.magnitude(), vc.magnitude())
    print("Dot products:", va.dot(vb), va.dot(vc), vb.dot(vc))
    print("Angles (deg):", va.angle_with(vb), va.angle_with(vc), vb.angle_with(vc))
    print("Projection of A onto B:", va.projection_onto(vb))

    # Q3 segment
    S = Point(0,0); E = Point(5,0); P = Point(3,4)
    print("Segment length:", segment_length(S,E))
    cp = closest_point_on_segment(S,E,P)
    print("Closest point on SE to P:", cp)
    d, cp2 = dist_point_to_segment(S,E,P)
    print("Distance from P to segment:", d)

    # Q4 lines intersection
    inter = intersect_lines(1, -1, 0, 0, 1, 2)  # x - y = 0 and y = 2
    if inter is None:
        print("Lines are parallel or coincident.")
    else:
        print("Intersection:", inter)
