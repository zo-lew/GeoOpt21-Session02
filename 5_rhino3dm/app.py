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
       hs.HopsBrep("mass","Geo","Extrusion of Curve", hs.HopsParamAccess.LIST)
    ]
)

def createExtruder(curve: rg.Geometry, height: float):

    geo = rg.Geometry(curve, height) 
    return geo.ToBrep(True, True)


if __name__== "__main__":
    app.run(debug=True)