#we import all the libraries that our functions need here too
import random as r
import rhino3dm as rg

def CreateBox(Xdimension,Ydimension,Zdimension):

    extrusions = []
    
    for i in range(nS):
        vector =  rg.Vector3d(0,0,sH*i)
        base = rg.Extrusion.Create(baseGeom, sH, True)
        baseCopy = base.Duplicate()
        baseCopy.Translate(vector)
        extrusions.append(baseCopy)

    return extrusions