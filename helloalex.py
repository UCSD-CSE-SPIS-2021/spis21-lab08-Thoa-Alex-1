from flask import Flask

app = Flask(__name__)
@app.route("/")

    def hello():

         return "Hello World!"
def ftoc(ftemp):

   return (ftemp - 32.0) * (5.0 / 9.0)
@app.route('/ftoc/<ftemp_str>')
def convert_ftoc(ftemp_str):
    ftemp = 0.0
def milestokm (distance)
    return (miles * 1.6)
@app.route('/milestokm/<distance_str>')
def convert_milestokm(ftemp_str):
    distance = 0.0


    try:

        ftemp = float(ftemp_str)

        ctemp = ftoc(ftemp)

        return "In Farenheit: " + ftemp_str + " In Celsius " + str(ctemp) 

    except ValueError:

        return "Sorry.  Could not convert " + ftemp_str + " to a number"
if __name__ == "__main__":

    app.run(host='0.0.0.0')