from flask import Flask, render_template, request , redirect, jsonify
import razorpay


name = "kunwar"
email = "rr@gmail.com"
contact = "+91982736292"


client = razorpay.Client(auth = ("rzp_test_AG3uPrA1DPRUTD" , "YzMCP49a7ni2c9IgiJcdrnqQ"))


app = Flask(__name__)

check = 0 

@app.route ('/ignite', methods = ['GET', 'POST'])
def ignite_arduino():
	global check; 
	#set data values for arduino 
	check = 1;
	return render_template('sigma_success.html')
	#return redirect('')


@app.route('/ff', methods = ['GET'])
def hello_world():
#check if data and send to arduino 
	global check; 

	if(request.method == 'GET'):
		data = {'check': check};
		check = 0 ;
		return jsonify(data);

	return 0;

@app.route('/', methods= ['POST', 'GET'])
def home ( ):
	if(request.method == 'GET'):
		print(request.args.get('value'))
	if(request.method == 'POST'):
		#print( request.form[ "maggie"], request.form["lays-classic-salted"] )

		# to make: done, price
		#assuming done
		#get price from form
		price = 1000
		done =1
		if(done):
			page = client.payment_link.create({
				"amount": price , "currency" : "INR", "accept_partial": False, "description" : "Vending" ,
				"customer": {
					"name": name,
					"email": email,
					"contact": contact
				},

				"callback_url": "https://hackathon41951.herokuapp.com/ignite"    ,
				"callback_method": "get"

				})
			return redirect(page['short_url'])

	
	return render_template('frontend.html')



if(__name__ == "__main__"):
	app.run(debug = True, port = 8000)