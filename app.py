from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	food= ["pasta","pizza","baget"]
	food=food   
	return render_template("index.html",food=food)


if __name__ == '__main__':
   app.run(debug = True)
