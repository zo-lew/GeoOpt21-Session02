#importing flask and hops to create a workflow
from flask import Flask
import ghhops_server as hs

#importing rhino3dm to create rhino geometry in python
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
       hs.HopsBrep("Geometry","Geo","Extrusion of Curve", hs.HopsParamAccess.LIST)
    ]
)

def createExtruder(curve: rg.Geometry, height: float):

    geo = rg.Geometry(curve, height) 
    return geo.ToBrep(True, True)


if __name__== "__main__":
    app.run(debug=True)