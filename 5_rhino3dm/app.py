from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import box library 
import box as b

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createBox",
    name = "Create Box",
    inputs=[
        hs.HopsNumber("X Box dimension", "X", "length in X direction", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("Y Box dimension", "Y", "width in Y direction", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("Z Box dimension", "Z", "height in Z direction", hs.HopsParamAccess.ITEM, default= 1)

    ],
    outputs=[
       hs.HopsPoint("Box","Boxy","Boxxy ", hs.HopsParamAccess.LIST)
    ]
)
def createBox(bX,bY,bZ):
    createBx = []
    for i in range(count):

       #in each itereation generate some random points
        box_x = b.uniform(-bX, bX)
        box_y = b.uniform(-bY, bY)
        box_z = b.uniform(-bZ, bZ)

        #create a point with rhino3dm
        random_pt = rg.Point3d(random_x, random_y, 0)
        
       #add point to the list
        createBx.append(random_pt)

    return createBx


if __name__== "__main__":
    app.run(debug=True)