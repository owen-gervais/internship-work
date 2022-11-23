# micropython_OnshapeAPI

This work is an in-progress translation of Onshape API in micropython. Currently generates the correct headers and authorization keys but Onshape's API currently does not support the micropython urequests library.  

## Installation: 
Download both the **onshape.py** and **creds.json** and fill in your indiviudal Onshape developer access and secret keys.
If you do not have developer keys, you can get them here from the [Developer Portal](https://dev-portal.onshape.com/).

## Running the Client:
Once completed, download these files to the EV3 either by creating a new project in vscode or through **scp**. SSH into your robot and run the following command from the commandline,

```bash
brickrun -r -- pybricks-micropython onshape.py
```

## Common Errors:
If you run into the error that the config.json can not be found, make sure that your **config.json** file is located in the same directory as the **onshape.py** file.


