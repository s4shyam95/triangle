from math import sqrt
def triangle_algorithm(S, p, eps):
	def euc_dis(p1, p2):
		summ = 0
		for i in range(len(p1)):
			summ+=(p1[i]-p2[i])*(p1[i]-p2[i])
		return sqrt(summ)
	def find_pivot(pp, p, S):
		for vj in S:
			if euc_dis(vj,pp) > euc_dis(vj,p):
				return (True,vj[:])
		return (False,None)
	min_norm = 1e10
	pp = v = None
	for vi in S:
		if euc_dis(p, vi) < min_norm:
			min_norm = euc_dis(p, vi)
			pp = vi[:]
			v = vi[:]
	while True:
		print p, pp, v
		if euc_dis(p, pp) < eps*euc_dis(p, v):
			# pp is an eps-approx solution
			return (True, pp)
		else:
			if find_pivot(pp, p, S)[0]:
				v = find_pivot(pp, p, S)[1]
				alpha = range(len(v))
				for i in range(len(alpha)):
					alpha[i] = (p[i]-pp[i])*(v[i]-pp[i])
					alpha[i] /= euc_dis(v,pp)*euc_dis(v,pp)
				pp_temp = range(len(pp))
				for i in range(len(pp_temp)):
					pp_temp[i] = (1.0 - alpha[i])*pp[i] + alpha[i]*v[i]
				pp = pp_temp[:]
				
				
			else:
				#pp is a p-witness
				return (False, pp)
			
		


#Testing
hull_pts = []
hull_pts.append([0,1])
hull_pts.append([1,1])
hull_pts.append([1,0])
hull_pts.append([0,0])
test_pt = [0.5,0.5]
eps = 1e-2
print triangle_algorithm(hull_pts, test_pt, eps)
