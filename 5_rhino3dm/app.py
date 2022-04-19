from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createBox",
    name = "Create Box",
    inputs=[
        hs.HopsNumber("Xdimension", "X", "X dimension length", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Ydimension", "Y", "Y dimension length", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Zdimension", "Z", "Z dimension length", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsBrep("mass","Bx","A very basic box", hs.HopsParamAccess.LIST)
    ]
)

def CreateBox(Xdimension,Ydimension,Zdimension):

    bx = rg.createBox(Xdimension, Ydimension, Zdimension)
    return bx



if __name__== "__main__":
    app.run(debug=True)