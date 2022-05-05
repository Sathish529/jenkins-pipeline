from config import app
import routes

@app.route("/")
def hello():
    return "Hello !!! Flask app is running"

if __name__ =='__main__':
    app.run(debug=True,host="0.0.0.0")
 
 #new push