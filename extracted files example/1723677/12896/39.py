# CREATE AN ANIMATION
images = []
steps = 60
fig = plt.figure(figsize=(8,8))
for k in range(steps):
    
    # CALCULATE NEW ANGLE OF ROTATION
    angR = k*(2*np.pi/steps)
    angD = round(k*(360/steps),0)
    u4 = np.cos(angR)*u1 + np.sin(angR)*u2
    u = np.concatenate([u4,u3]).reshape((2,300))
    
    # PROJECT TRAIN AND TEST ONTO U3,U4 PLANE
    p = u.dot(train.iloc[:,2:].values.transpose())
    p2 = u.dot(test.iloc[:,1:].values.transpose())
    
    # PLOT TEST DATA
    img1 = plt.scatter(p2[0,:],p2[1,:],c='gray')
    
    # PLOT TRAIN DATA (KEEP CORRECT COLOR IN FRONT)
    idx0 = train[ train['target']==0 ].index
    idx1 = train[ train['target']==1 ].index
    if angD<180:
        img2 = plt.scatter(p[0,idx1],p[1,idx1],c='yellow')
        img3 = plt.scatter(p[0,idx0],p[1,idx0],c='blue')
    else:
        img2 = plt.scatter(p[0,idx0],p[1,idx0],c='blue')
        img3 = plt.scatter(p[0,idx1],p[1,idx1],c='yellow')
        
    # ANNOTATE AND ADD TO MOVIE
    img4 = plt.text(1.5,-3.5,'Angle = '+str(angD)+' degrees')
    images.append([img1, img2, img3, img4])
    
# SAVE MOVIE TO FILE
ani = ArtistAnimation(fig, images)
ani.save('data.gif', writer='imagemagick', fps=15)
