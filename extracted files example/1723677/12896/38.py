# CREATE RANDOM DIRECTION PERPENDICULAR TO U1 AND U2
u3 = np.random.normal(0,1,300)
u3 = u3 - u1.dot(u3)*u1 - u2.dot(u3)*u2
u3 = u3/np.sqrt(u3.dot(u3))
