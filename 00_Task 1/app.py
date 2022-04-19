#Zoé Lewis - Session 02, Asign 1, Task 1 
#AIA-Geo-Opt, MaCAD 2022, IAAC

from flask import Flask
import ghhops_server as hs

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createExtruder",
    name = "Create Extruder",
    inputs=[
        hs.HopsCurve("Curve", "C", "closed NURBS curve", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("geometry height", "H", "geometry height", hs.HopsParamAccess.ITEM),

    ],
    outputs=[
      hs.HopsBrep("Geometry","Geo","Extrusion of Curve", hs.HopsParamAccess.LIST),
    ]
)
def CreateExtruder(baseCrv,nH):
    extrusions = []

    for item in range(baseCrv):

        #extrude the curve
        base = rg.Extrusion.Create(baseCrv, nH, cap=True)
        
    return extrusions


if __name__== "__main__":
    app.run(debug=True)