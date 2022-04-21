from flask import Flask
import ghhops_server as hs

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createExtrusion",
    name = "Create Extruder",
    inputs=[
        hs.HopsCurve("Curve", "C", "closed NURBS curve", hs.HopsParamAccess.ITEM),
        hs.HopsInteger("geometry height", "H", "geometry height", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
      hs.HopsBrep("Geometry","Geo","Extrusion of Curve", hs.HopsParamAccess.LIST),
    ]
)
def CreateExtruder(baseCrv, nH):

    base = rg.Extrusion.Create(baseCrv, nH, cap=True)
        
    return base



@hops.component(
    "/createExtrusions",
    name = "Create Extruder",
    inputs=[
        hs.HopsCurve("Curve", "C", "closed NURBS curve", hs.HopsParamAccess.LIST),
        hs.HopsInteger("geometry height", "H", "geometry height", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
      hs.HopsBrep("Geometry","Geo","Extrusion of Curve", hs.HopsParamAccess.LIST),
    ]
)
def CreateExtruder(baseCrvs,nH):
    extrusions = []

    for i in range(len(baseCrvs)):

        #extrude the curve
        base = rg.Extrusion.Create(baseCrvs[i], nH, cap=True)
        extrusions.append(base)

    return extrusions


if __name__== "__main__":
    app.run(debug=True)