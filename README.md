# Predicting-Disesse-Outcomes
It can detect various disease by Puting Some symptomatic information.
First we need some data to trained our trained moduel so, we have collect the database from kaggle (we attached those csv files with my repository)
Then for building the trained moduel we use (https://jupyter.oneapi.devcloud.intel.com) 
To build the trained moduel we use Intel Optimized Sckitlearn library then we procesed the data and build trained test split for Support Vector Mechine classifier
For predicting the outcome of new data we save the SVM as trained SVM, and we save that file as .sav file.(we attached those sav files with my repository)
Now for building the frontend we used streamlit library in spider(Anaconda Navigator) as a platform.
We make the interface approchable for the user using this streamlit option menu.
We use this command (streamlit run "path") in conda cmd to see the page in browser.
We put the data in browser to test our application.
