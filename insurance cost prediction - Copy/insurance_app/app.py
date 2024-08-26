from flask import *
import pickle
import os

app=Flask(__name__)

model = pickle.load(open("lrmodel.pkl", "rb"))

@app.route('/', methods=["GET", "POST"])
def home():
	if request.method == "POST":
		age=int(request.form["age"])
		bmi=float(request.form["bmi"])
		children= int(request.form["children"])
		sex = int(request.form["sex"])
		if sex == 0:
			d1 = [0]
		else:
			d1 = [1]
		smoker = int(request.form["smoker"])
		if smoker == 0:
			d2 = [0]
		else:
			d2 = [1]
		d = [[age]+[bmi]+[children]+d1+d2]
		res = model.predict(d)
		msg = "\u20B9 " + str(round(res[0], 2))
		return render_template("home.html", msg=msg)
	else:
		return render_template("home.html")

if __name__=='__main__':
    app.run(debug=True)