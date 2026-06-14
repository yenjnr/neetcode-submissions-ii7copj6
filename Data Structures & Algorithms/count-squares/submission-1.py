class CountSquares:

    def __init__(self):
        self.countMap = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.countMap[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for p in self.pts:
            x,y=p[0],p[1]
            qx,qy=point[0],point[1]
            if x!=qx and y!=qy and abs(x-qx) == abs(y-qy):
                res += self.countMap[(qx,y)] * self.countMap[(x,qy)]
        return res
