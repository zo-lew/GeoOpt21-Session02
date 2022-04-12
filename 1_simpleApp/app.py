from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

"""
    How to create inputs and outputs for hops.
    
    Hops Inputs should match the number of Hops inputs
    Hops Outputs should match the number of items that the functions returns 
"""

@hops.component(
    "/mycomponent",
    name = "MyComponent",
    inputs=[
        hs.HopsInteger("N1" ),
        hs.HopsInteger("Second Number", "N2", "Second Value", hs.HopsParamAccess.ITEM, default= 10)

    ],
    outputs=[
       hs.HopsInteger("Sum Result","S","Result of the sum")
    ]
)
def MyComponent(num1, num2):
    sum = num1 + num2
    return sum



if __name__== "__main__":
    app.run(debug=True)