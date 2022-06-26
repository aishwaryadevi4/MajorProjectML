# MajorProjectML
Requirements:
Install node-js(Reference:https://nodejs.org/en/download/)
Install angular(Reference:https://angular.io/guide/setup-local)
Install python-3
Donwload pipenv using the command pip3 install pipenv

Steps:
Clone all 3 repositories mentioned below:
https://github.com/rohithreddydepa/majorProjectApi
https://github.com/rohithreddydepa/majorProjectUi
https://github.com/aishwaryadevi4/MajorProjectML (current repository)

Go to the UI code from the terminal, run this command to install all the UI dependencies->  npm i
Go to the API code from the terminal, run this command to install the API dependencies-> pipenv install
Run the app.py file from the API code.
From the UI terminal, use this command: npm start
Open the localhost:4200 to view the UI.
Open the localhost:5000 to view both the UI and the API. (For the CORS error to be resolved, download the extension "Allow CORS: Access-Control-Allow-Origin" through
https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?hl=en )

To make changes in the UI, after making the changes, run the command-> ng build --base-href /static/   
This will generate a folder called "dist", replace the index.html of API code with the index.html from the dist folder. Clear the static folder of API and add the remaining files from the dist folder 
to the static folder of API.



