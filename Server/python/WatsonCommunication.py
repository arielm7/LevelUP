import sys 
import watson_developer_cloud
import time
import requests


## Data from PHP
DatafromPHP=str(sys.argv[1])

## Watson Assistant Code
###################################################################################

# Set up Assistant service.
service = watson_developer_cloud.AssistantV1(
  username = '24fb4d72-974d-452e-ac53-d0ddd14c5775', # replace with service username
  password = 'vMPmTgmcOOgR', # replace with service password
  version = '2018-02-16'
)
workspace_id = 'ead93613-f0f2-42fa-b8ac-bda25c0490ab' # replace with workspace ID


# Initialize with empty value to start the conversation.
user_input = ''
context = {}
current_action = ''
Output={}

# Main input/output loop
while current_action != 'end_conversation':
  
  # Send message to Assistant service.
  response = service.message(
    workspace_id = workspace_id,
    input = {
      'text': user_input
    },
    context = context
  )

  # If an intent was detected, Saves it in a list.
  if response['intents']:
    Output["intent"]=response['intents'][0]['intent'].encode("utf-8")
    


  # Saves the output from dialog, if any.
  if response['output']['text']:
    Output["output"]=response['output']['text'][0].encode("utf-8")
    
  # Update the stored context with the latest received from the dialog.
  context = response['context']

  # Check for action flags sent by the dialog and Saves it in a list.
  if 'action' in response['output']:
    current_action = response['output']['action']
    Output["action"]=current_action.encode("utf-8")
    print (Output)

  # User asked what time it is, so we output the local system time.
  if current_action == 'display_time':
    Output["time"]=time.strftime('%I:%M:%S %p')
    #print('The current time is ' + time.strftime('%I:%M:%S %p') + '.')

  # If we're not done, prompt for next round of input.
  if current_action != 'end_conversation':
    user_input = DatafromPHP
    


