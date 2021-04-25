# GreenhouseData

This project visualises the dataset of different gases quantity in the environment of different country over a time period. 

![graph](https://user-images.githubusercontent.com/22542053/115993983-c7577b80-a5f2-11eb-8439-e3b3e0248afa.png)


# To run the project 

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

Run `python service.py` to start the backend service.

# Information about project

`data-clean.py` is use to clean the initial data and add the data to `output.csv`. Please delete the current `output.csv` if you wish run the script again.

`service.py` loads the backend server which has 2 endpoints returning countryList and data for each country.



