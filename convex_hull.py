import math

def findBottomLeft(points:list):
	bottom_left = points[0]
	for point in points:
		if (point.y < bottom_left.y) or (point.y == bottom_left.y and point.x < bottom_left.x):
			bottom_left = point
	return bottom_left


def sortCCW(points:list):
	base_point = findBottomLeft(points)
	points.remove(base_point)
	points.sort(key=lambda point: math.atan2(point.y - base_point.y, point.x - base_point.x ))
	points.insert(0, base_point)

def isLeftTurn(p1,p2,p3):
	return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x) > 0


def grahamScan(points:list):
	sortCCW(points)
	convex_hull = [points[0], points[1], points[2]]
	for point in points[3:]:
		while (len(convex_hull) > 1) and (not isLeftTurn(convex_hull[-2], convex_hull[-1], point)):
			convex_hull.pop()
		convex_hull.append(point)
	# add first point to close a circle
	convex_hull.append(convex_hull[0])
	return convex_hull
