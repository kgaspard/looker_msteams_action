Credit goes to [@kirz182](https://github.com/kriz182)

1) Get your MS Teams incoming webhook URL: https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/connectors/connectors-using#setting-up-a-custom-incoming-webhook

2) Create a Cloud Function with main.py and requirements.txt. If using Google Cloud Functions for instance, don't forget to set Runtime to Python 3.7 and Function to execute as sendtoteams

3) Copy the code from action_param.lkml into the LookML field from which you want the user to be able to send to MS Teams, and fill in the relevant [...] fields
