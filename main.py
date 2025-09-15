# Trapezoid calculator display 
from pyscript import display, document

def calculator(e): #creating calculating functions in python
    document.getElementById("output").innerHTML = "" #clearing the output field
    Height = document.getElementById("height").value #getting value from an inpute field
    Bass_One = document.getElementById("bass_one").value
    Bass_Two = document.getElementById("bass_two").value

    answer = (float(Height) * (float(Bass_One) + float(Bass_Two))) / 2 #formula for area of trapezoid

    display( f"The area of the trapezoid is {answer} meters", target = "output") #displaying the answer in the output field