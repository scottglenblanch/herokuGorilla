import json
from flask import Flask, request, render_template, Response
import os
from pprint import pprint as p



def setupFlaskServer(flaskApp):

	flaskApp.config['TEMPLATES_AUTO_RELOAD'] = True

	urlOfSheet = os.environ.get('urlOfPublicGoogleSheet', 'https://www.google.com')
	p(urlOfSheet)

	# objToFrontend = {
	# 	"urlOfSheet": os.environ.get('urlOfPublicGoogleSheet', 'URL not loaded')
	# }

	@flaskApp.route('/datarequests', methods=['GET', 'POST'])
	def datarequests():

		if request.method == 'GET':
			dataToSendToFrontend = {
				'cat eyes': 'yellow',
				'collar': 'red'
			}

			return Response(json.dumps(dataToSendToFrontend), mimetype='application/json')


		if request.method == 'POST':
			requestObj = request.json

			if 'processToRun' in requestObj:
				p(requestObj['processToRun'])
				
				from .reconcileArrays import reconcileArrays
				
				return render_template(requestObj['htmlPathToLoad'], valueFromBackend=urlOfSheet)
			else:
				return render_template(requestObj['htmlPathToLoad'], valueFromBackend=urlOfSheet)


			# if requestObj['spreadsheetType'] == 'public':
			# 	return render_template('frontend/htmlTemplates/reconcileArrays/reconcilePublic.html')
			# else:
			# 	return render_template('frontend/htmlTemplates/reconcileArrays/reconcilePrivate.html')


	@flaskApp.route('/')
	def returnMainPage():
		return render_template('frontend/htmlTemplates/index.html')
		# return """	<p>Spreadsheet to reconcile:</p>
		# 			<button onclick="publicClickFunction()">Public</button>
		# 			<button onclick="privateClickFunction()">Private</button>
		# 			<p></p>
		# 			<img src="./frontend/assets/regal-cat.jpeg" alt="regal cat" />"""


	if __name__ == '__main__':
		
		flaskAppLoadProcess = ''
		flaskApp.run()



flaskApp = Flask(__name__, template_folder='../', static_folder='../frontend')
setupFlaskServer(flaskApp)