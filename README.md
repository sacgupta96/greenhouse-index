# GreenhouseData

This project visualises the [dataset](https://www.kaggle.com/unitednations/international-greenhouse-gas-emissions) of different gases quantity in the environment of different country over a time period. 

This project is build using Angular framework backed by `flask` engine , leverages `chart.js` open library for graph visualization.

# UI mockup

![graph](https://user-images.githubusercontent.com/22542053/115993983-c7577b80-a5f2-11eb-8439-e3b3e0248afa.png)


# To run the project 

Supported Operating System - Windows , Linux , OSX

### Prerequisite
1. [NPM](https://phoenixnap.com/kb/install-node-js-npm-on-windows)
2. [Angular CLI](https://www.npmjs.com/package/@angular/cli)
3. [Python3](https://www.python.org/downloads/)
4. Install modules for python flask_cors , flask , flask_restful , pandas , json. Do pip install `module_name`.

### To Run
1. Run `python service.py` in backend folder to start the backend service. Service now runs on port 5000.
2. Run `ng serve` in project folder for starting dev server. Service now runs on port 4200.
3. On local browser , navigate to `http://localhost:4200/`.

# Information about project

`data-clean.py` is use to clean the initial data and add the data to `output.csv`.

`service.py` loads the backend server which has 2 endpoints returning countryList and data for each country.



