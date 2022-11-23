# Direct Connection
This code allows for the EV3 to directly communicate with the Onshape API. This demo updates the color of a part based on the EV3 Color Sensor

## Installation on EV3: 
In order to run this above code the following steps need to be run

  1. Create a new EV3 Project in Vscode
  2. Copy **main.py**, **onshapeCommunication.py**, and **api-key** into the VsCode Project
  3. Edit the api-key file and replace the first two lines with your Onshape access key and secret key respectively.
  4. Download and Run the code to the EV3 using F5
## How the Code Works:
The code operates by working around the micropythonwaiting for the user to press any button on the EV3 in order to detect a color. This color is then sent to Onshape's API from an outs
  
Click here to access the document for the [color changing assembly](https://rogers.onshape.com/documents/5180c826cc8ee318e7669421/w/dd443cb272828ce48b0bb115/e/57e0db8f710c855151c78a04). Using this code will update this assembly. 
