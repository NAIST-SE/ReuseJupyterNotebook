# CREATE RANDOM DIRECTION PERPENDICULAR TO U1
u2 = np.random.normal(0,1,300)
u2 = u2 - u1.dot(u2)*u1
u2 = u2/np.sqrt(u2.dot(u2))
