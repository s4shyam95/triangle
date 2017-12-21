#Testing
hull_pts = []
hull_pts.append([0,1])
hull_pts.append([1,1])
hull_pts.append([1,0])
hull_pts.append([0,0])
test_pt = [0.5,0.5]
eps = 1e-2
print triangle_algorithm(hull_pts, test_pt, eps)