#stamp on sphere, using color info of a texture
'''
before we run the script we need to execute the following 2 lines, and then apply a texture to the polySphere
sphereradius=5
cmds.polySphere(r=sphereradius)
'''


import maya.cmds as cmds
from random import randint,random
import math

# this simple function is called each time the script below decides an object should be located
def locate_object(x,y,z):
			cmds.polyCone()		
			cmds.scale(0.01, 0.01, 0.01)
			cmds.move( x,y,z)

def getVtxPos( shapeNode ) :
 
	vtxWorldPosition = []    # will contain positions un space of all object vertex
 
	vtxIndexList = cmds.getAttr( shapeNode+".vrts", multiIndices=True )
 
	for i in vtxIndexList :
		curPointPosition = cmds.xform( str(shapeNode)+".pnts["+str(i)+"]", query=True, translation=True, worldSpace=True )    # [1.1269192869360154, 4.5408735275268555, 1.3387055339628269]
		vtxWorldPosition.append( curPointPosition )
 
	return vtxWorldPosition




sphereorigin=[0,0,0]


#save a list of all shapes world positions
sphereVertexList=getVtxPos('pSphereShape1')
vertexCount=0
#loop and print all positions of the vertices on the sphere
for i in sphereVertexList:
    global vetexCount
    vertexCount+=1
    #print "vertex_%d =%s"%(vertexCount,i)
    
    #create a spherepoint vector to hold the position of the vertex onto the sphere in 3d space
    spherePoint=[]
    for coordinate in i:
        spherePoint.append(coordinate)
        
    #print spherePoint
        
    
    #Find U V  on the sphere
    #by 
    #i) For any point P on the sphere, calculate d, that being the unit vector from P to the sphere's origin.
    
    #subtract 2 vectors
    spherePointToOrigin=[]
    #create the direction from point to origin vector by subtractig the vectors 
    for index in range(len(spherePoint)):
        spherePointToOrigin.append( sphereorigin[index]-spherePoint[index] ) 
    
    dirVec=[]
    #normalize vector from point on sphee to origin of sphere
    
    spherePointToOriginLentgh=math.sqrt( spherePointToOrigin[0]*spherePointToOrigin[0] + spherePointToOrigin[1]*spherePointToOrigin[1] + spherePointToOrigin[2]*spherePointToOrigin[2] )
    dirVec.append(spherePointToOrigin[0]/spherePointToOriginLentgh)
    dirVec.append(spherePointToOrigin[1]/spherePointToOriginLentgh)
    dirVec.append(spherePointToOrigin[2]/spherePointToOriginLentgh)
    
    
        
        
    #print "dirVec=%s"%dirVec
    
    #now find u v for the point on the sphere
    __u= 0.5+(math.atan2(dirVec[2],dirVec[0]) / (2*math.pi))
    
    __v=0.5+math.asin(dirVec[1])/math.pi
    #print "__u=%f, __v=%f"%(__u,__v)

    # the colour components at the uv referred to by the current values fu and fv are returned and
    # assigned to the variable named 'sample'
    sample = cmds.colorAtPoint( 'file1', output ='RGBA', u = -__u-0.05, v = -__v )
    #print "sample=%s"%sample
    		
    #0.19607841968536377, 0.5803921222686768, 0.003921568393707275
    if sample[0] == 0.9294117093086243 and sample[1] ==0.10588234663009644: # checks if the blue component is less than 0.7
        locate_object(spherePoint[0], spherePoint[1], spherePoint[2])		
        print "sample=%s"%sample
    
    	
    


# make things easier by removing the namespace associated with the imported file
if cmds.namespace(exists='map1'):
    print "removing namespace map1"
    cmds.namespace(mergeNamespaceWithRoot=True,removeNamespace=":map1")


'''
# the following nested loops iterate through values from 0 - 100			
for number in range(0,2000):
	x = randint(0,101)
	z = randint(0,101)
	# by dividing x and z by float value 100.0 the next lines create floating point values between 0.0 and 1.0
	fu = x/100.0
	fv = z/100.0
	# the colour components at the uv referred to by the current values fu and fv are returned and
	# assigned to the variable named 'sample'
	sample = cmds.colorAtPoint( 'file1', output ='RGBA', u = fu, v = fv )
	# if you want to see what the values actually are,
	# uncomment the next lines that I used when developing the script 
	# print 'at u,v' + str(u/100.0) + "," + str(v/100.0) + ' sample = '
	# print sample
	if sample[2] < 0.7 : # checks if the blue component is less than 0.7
		locate_object(x,z)		
		
 
		replace the last line with these three lines to make the placement of cones
		less regular by perturbing the value of the location a little
		
		px = random()-random()
		pz = random()-random()
		locate_object(x+px,z+pz)
		
		use a texture that you have chosen or made yourself
		
		use the texture to choose what type of object to locate
		
		what other attributes of an object might be controlled by the texture?
		
		how might it be applied in creating a scene?
		
		could you use different textures for different features?
		
		could you use a texture to guide the movement of a character?





'''
