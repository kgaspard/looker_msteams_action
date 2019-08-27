import pymsteams

def sendtoteams(request):
	# Get the JSON from Request
	data = request.get_json()

	#Get Message Value (Depends on the form_param you define), user dashboard link

	title = data['form_params']['Title']
	message = data['form_params']['Message']
	msteamswebhook = data['data']['msteamswebhook']
	user_dash = data['data']['link']
	link_text = data['data']['linktext']

	# You must create the connectorcard object with the Microsoft Webhook URL
	myTeamsMessage = pymsteams.connectorcard(msteamswebhook)

	# Add title to the message.
	myTeamsMessage.title(title)

    # Add text to the message.
	myTeamsMessage.text(message)

	# Add Link Button
	myTeamsMessage.addLinkButton(link_text, user_dash)

	# send the message.
	myTeamsMessage.send()

    #if False not in response:
	return '{"looker": {"success": true}}'