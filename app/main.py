from flask import Flask 

app = Flask(__name__) 

#GPIO.setmode(GPIO.BCM)
#done = False

# original, edited for ngrok public hosting @app.route("/")
@app.route("/", methods=['GET'])
def home_view(): 
        return "<h1>Welcome to GPIO data for my Pi</h1>"

@app.route("/readPin/<pin>")
def readPin(pin):
   try:
      GPIO.setup(int(pin), GPIO.IN)
      if GPIO.input(int(pin)) == True:
         response = "Pin number " + pin + " is high!"
      elif GPIO.input(int(pin)) == False:
         response = "Pin number " + pin + " is low!"
   except:
      response = "There was an error reading pin " + pin + "."

   templateData = {
      'title' : 'Status of Pin' + pin,
      'response' : response
      }



   return render_template('pin.html', **templateData)

