from flask import Flask, jsonify, request, render_template
from process1 import *
# from process2 import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
def heatwave_month():
	for key, value in request.form.items():
		if key == 'method': 
			method = value
		if key == 'month': 
			month = value


	if method == 'Adilabad':
		result = adilabad(month)
	elif method == 'karimnagar':
		result = karimnagar(month)
	elif method == 'khammam':
		result = khammam(month)
	elif method == 'Nizamabad':
		result = Nizamabad(month)
	else:
		result = warangal(month)		
			
	if method=='Adilabad':
		if result>=35:
			op="Be careful. There is chance of occuring heatwaves in adilabad in ",month," 2023"
		else:
			op="you will be safe, there will be no chance of occuring heawaves"
	else:
		if result>=40:
			op="Be careful. There is chance of occuring heatwaves in Kaimnagar in ",month," 2023"
		elif result>=35 and result<=40:
			op="there may be chance of occuring the heatwave"
		else:
			op="you will be safe, there will be no chance of occuring heawaves"			
	return render_template('result.html',result=result , op=op)

# def aqi_month():
# 	for key, value in request.form.items():
# 		if key == 'method2': 
# 			method2 = value
# 		if key == 'date': 
# 			date = value 

#     if method2 == 'Adilabad':
# 		result2 = adilabad(date)
# 	elif method2 == 'karimnagar':
# 		result2 = karimnagar(date)
# 	elif method2 == 'khammam':
# 		result = khammam(date)
# 	elif method2 == 'Nizamabad':
# 		result2 = Nizamabad(date)
# 	else:
# 		result2 = warangal(date)


if __name__=="__main__":
	app.run(debug=True)
