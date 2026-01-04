Fire Prediction Using Machine Learning

Project Overview

This project predicts the risk of fire based on environmental features using a Machine Learning model. The model analyzes input data such as temperature, humidity, wind speed, and other relevant factors to determine the likelihood of fire occurrence. The prediction is displayed as a percentage, along with a color-coded risk level to help users take preventive measures.

Features

* Predicts fire risk in percentage form.
* Displays a color-coded progress bar based on risk:

  * Green: Low risk
  * Yellow: Medium risk
  * Red: High risk
* Dynamic and modern user interface with alert messages.
* Option to predict multiple times using the “Predict Again” button.
* Easy integration with Flask or Django backend.

Tech Stack

* Backend: Python, Flask (or Django)
* Machine Learning Model: Logistic Regression / Random Forest / Your chosen ML algorithm
* Frontend: HTML, CSS, JavaScript
* Data: Environmental features like temperature, humidity, wind speed, etc.

How It Works

1. User enters environmental data into the input form.
2. The backend passes the data to the trained ML model.
3. The model predicts the risk of fire as a percentage.
4. The result page shows:

   * The prediction percentage
   * A progress bar with dynamic color based on risk
   * A status message recommending preventive actions

How to Run

1. Clone the repository:


git clone https://github.com/yourusername/fire-prediction.git


2. Navigate to the project folder:


cd fire-prediction


3. Install required Python packages:


pip install -r requirements.txt


4. Run the Flask app:


python app.py


5. Open your browser and go to `http://127.0.0.1:5000` to access the Fire Prediction app.

Future Improvements

* Include real-time data from IoT sensors.
* Add historical fire data analysis to improve accuracy.
* Enhance UI with animated flames for high-risk scenarios.
* Deploy as a web application accessible anywhere.

Author

Amaan – passionate about AI, Machine Learning, and data-driven solutions.


