import json
from flask import Flask, request, render_template, Response
from pprint import pprint as p
import waitress


def setupFlaskServer(flaskApp):

	flaskApp.config['TEMPLATES_AUTO_RELOAD'] = True
	flaskAppStatus = ''

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

			if requestObj['spreadsheetType'] == 'public':
				return render_template('main/frontend/htmlTemplates/reconcileArrays/reconcilePublic.html')
			else:
				return render_template('main/frontend/htmlTemplates/reconcileArrays/reconcilePrivate.html')


	@flaskApp.route('/')
	def returnMainPage():
		return render_template('main/frontend/htmlTemplates/index.html', flaskAppStatus=flaskAppStatus)
		# return """	<p>Spreadsheet to reconcile:</p>
		# 			<button onclick="publicClickFunction()">Public</button>
		# 			<button onclick="privateClickFunction()">Private</button>
		# 			<p></p>
		# 			<img src="./frontend/assets/regal-cat.jpeg" alt="regal cat" />"""


	if __name__ == '__main__':
		
		# waitress.serve(flaskApp, host='0.0.0.0', port=8000)
		flaskAppStatus = '__name__ = __main__'
		flaskApp.run()



flaskApp = Flask(__name__, template_folder='../../', static_folder='../../main')
setupFlaskServer(flaskApp)