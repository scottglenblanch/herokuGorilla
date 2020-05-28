import json
from flask import Flask, request, render_template, Response
import os
from pprint import pprint as p


def runningOnDevelopmentServer(urlStr):
	if any(strToFind in urlStr for strToFind in ['127.0.0.1:5000', 'localhost:5000']):
		return True
	else:
		return False


def setupFlaskServer(flaskApp):

	flaskApp.config['TEMPLATES_AUTO_RELOAD'] = True

	urlOfSheet = os.environ.get('urlOfPublicGoogleSheet', 'https://www.google.com')


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

				from backend.reconcileArrays import reconcileArrays as reconcileArrays
				returnValue = reconcileArrays.reconcileArraysFunction(runningOnDevelopmentServer(request.url_root))
				return render_template(requestObj['htmlPathToLoad'], valueFromBackend=returnValue)

			else:
				return render_template(requestObj['htmlPathToLoad'], valueFromBackend=urlOfSheet)



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
		flaskApp.run(port=5000, debug=True, host='0.0.0.0')


flaskApp = Flask(__name__, template_folder='./', static_folder='./frontend')
setupFlaskServer(flaskApp)