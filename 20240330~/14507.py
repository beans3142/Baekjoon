import sys
import math
import random
from collections import deque

# Constants
EPS = 1e-9

def eq(a, b):
    d = abs(a - b)
    return d < EPS or d < EPS * max(abs(a), abs(b))


class Vec2:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

    def add(self, rhs):
        return Vec2(self.x + rhs.x, self.y + rhs.y)

    def sub(self, rhs):
        return Vec2(self.x - rhs.x, self.y - rhs.y)

    def scale(self, s):
        return Vec2(s * self.x, s * self.y)

    def dot(self, rhs):
        return self.x * rhs.x + self.y * rhs.y

    def cross(self, rhs):
        return self.x * rhs.y - self.y * rhs.x

    def midpoint(self, rhs):
        return Vec2(0.5 * (self.x + rhs.x), 0.5 * (self.y + rhs.y))

    def mag2(self):
        return self.x * self.x + self.y * self.y

    def mag(self):
        return math.sqrt(self.mag2())

    def dist(self, rhs):
        return self.sub(rhs).mag()

    def ortho_cw(self):
        return Vec2(self.y, -self.x)

    def ortho_ccw(self):
        return Vec2(-self.y, self.x)

    def __str__(self):
        return f"<{self.x:.7f}, {self.y:.7f}>"


class Vec3:
    def __init__(self, xx, yy, zz):
        self.x = xx
        self.y = yy
        self.z = zz

    def eq(self, rhs):
        return eq(self.x, rhs.x) and eq(self.y, rhs.y) and eq(self.z, rhs.z)

    def add(self, rhs):
        return Vec3(self.x + rhs.x, self.y + rhs.y, self.z + rhs.z)

    def sub(self, rhs):
        return Vec3(self.x - rhs.x, self.y - rhs.y, self.z - rhs.z)

    def scale(self, s):
        return Vec3(self.x * s, self.y * s, self.z * s)

    def dot(self, rhs):
        return self.x * rhs.x + self.y * rhs.y + self.z * rhs.z

    def cross(self, rhs):
        xn = self.y * rhs.z - self.z * rhs.y
        yn = self.z * rhs.x - self.x * rhs.z
        zn = self.x * rhs.y - self.y * rhs.x
        return Vec3(xn, yn, zn)

    def mag(self):
        return math.sqrt(self.mag2())

    def mag2(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def angle_btwn(self, rhs):
        mag1 = self.mag()
        mag2 = rhs.mag()
        if mag1 < EPS or mag2 < EPS:
            return 0.0
        dt = self.dot(rhs)
        return math.acos(dt / (mag1 * mag2))

    def __str__(self):
        return f"{self.x:.6f} {self.y:.6f} {self.z:.6f}"


class Circle2:
    def __init__(self, c, r):
        self.cen = c
        self.rad = r

    def on_border(self, p):
        return eq(self.cen.dist(p), self.rad)

    def contains(self, p):
        return self.cen.dist(p) <= self.rad + EPS

    @staticmethod
    def get_center(p1, p2, p3):
        m1 = p1.midpoint(p2)
        m2 = p3.midpoint(p2)

        n1 = Vec2(p2.y - p1.y, p1.x - p2.x)
        n2 = Vec2(p2.y - p3.y, p3.x - p2.x)

        if eq(n1.cross(n2), 0):
            return None

        L1 = Line2(m1, m1.add(n1))
        L2 = Line2(m2, m2.add(n2))
        return L1.intersect(L2)

    def __str__(self):
        return f"({self.cen}, {self.rad:.6f})"


class Line2:
    def __init__(self, a, b):
        self.e1 = a
        self.e2 = b

    def get_vec2(self):
        return self.e2.sub(self.e1)

    def intersect(self, rhs):
        v1 = self.get_vec2()
        v2 = rhs.get_vec2()
        v3 = rhs.e1.sub(self.e1)
        div = v1.cross(v2)
        sn = v3.cross(v2)
        s = sn / div

        return v1.scale(s).add(self.e1)


class CircleSearch:
    def __init__(self, pts):
        self.N = len(pts)
        self.pts = pts

    def calc_radius(self):
        return self.make_circle().rad

    def make_circle(self):
        c = None
        for i in range(self.N):
            p = self.pts[i]
            if c is None or not c.contains(p):
                c = self.make_circle_one_point(i + 1, p)
        return c

    def make_circle_one_point(self, M, p):
        c = Circle2(p, 0)
        for i in range(M):
            q = self.pts[i]
            if not c.contains(q):
                if c.rad == 0:
                    c = self.make_diameter(p, q)
                else:
                    c = self.make_circle_two_points(i + 1, p, q)
        return c

    def make_circle_two_points(self, M, p, q):
        circ = self.make_diameter(p, q)
        left = None
        right = None

        pq = q.sub(p)
        for i in range(M):
            r = self.pts[i]
            if circ.contains(r):
                continue

            cx = pq.cross(r.sub(p))
            c = self.make_circumcircle(p, q, r)

            if c is None:
                continue
            elif cx > 0 and (left is None or pq.cross(c.cen.sub(p)) > pq.cross(left.cen.sub(p))):
                left = c
            elif cx < 0 and (right is None or pq.cross(c.cen.sub(p)) < pq.cross(right.cen.sub(p))):
                right = c

        if left is None and right is None:
            return circ
        elif left is None:
            return right
        elif right is None:
            return left
        else:
            return left if left.rad <= right.rad else right

    def make_diameter(self, a, b):
        m = a.midpoint(b)
        return Circle2(m, a.dist(m))

    def make_circumcircle(self, a, b, c):
        p = Circle2.get_center(a, b, c)
        if p is None:
            return None
        return Circle2(p, p.dist(a))


class ConvexShell:
    def __init__(self, vs):
        self.N = len(vs)
        self.vs = vs
        self.edge = [[0] * self.N for _ in range(self.N)]

    def run(self):
        faces = deque()
        pending = deque()

        faces.append(Face(0, 1, 2))
        faces.append(Face(0, 2, 1))

        for p in range(3, self.N):
            v = self.vs[p]

            num_steps = len(faces)
            while num_steps > 0:
                num_steps -= 1
                f = faces.popleft()
                dv = v.sub(self.vs[f.spin[0]])

                dt = dv.dot(f.norm)
                if dt > EPS:
                    i, j, k = f.spin
                    self.edge[i][j] -= 1
                    self.edge[j][k] -= 1
                    self.edge[k][i] -= 1
                else:
                    faces.append(f)

            for f in faces:
                for c in range(3):
                    i = f.spin[(c + 1) % 3]
                    j = f.spin[c]

                    if self.edge[i][j] == 0:
                        pending.append(Face(i, j, p))

            faces.extend(pending)
            pending.clear()

        norms = [f.norm for f in faces]
        return norms


class Face:
    def __init__(self, i, j, k):
        self.spin = [i, j, k]
        self.norm = self.calculate_norm(i, j, k)

    def calculate_norm(self, i, j, k):
        return self.vs[j].sub(self.vs[i]).cross(self.vs[k].sub(self.vs[i]))

    def __str__(self):
        return f"{self.spin[0]} {self.spin[1]} {self.spin[2]}"


class StarsFont:
    def __init__(self, in_stream):
        self.N = int(in_stream.readline().strip())
        self.pts = [Vec3(*map(int, in_stream.readline().strip().split())) for _ in range(self.N)]
        self.first_approximation = self.calculate_approximation()

    def calculate_approximation(self):
        return CircleSearch(self.pts).calc_radius()

    def adjust(self):
        self.first_approximation = CircleSearch(self.pts).calc_radius()


if __name__ == "__main__":
    stars_font = StarsFont(sys.stdin)
    print(stars_font.first_approximation)
