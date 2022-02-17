# Airline prediction satisfaction prediction


---
**Source** : https://www.kaggle.com/teejmahal20/airline-passenger-satisfaction

**Problem Statement**

This dataset contains US airline passenger satisfaction survey. The airline passenger satisfaction survey is an in-depth feedback questionnaire that an airline sends to its passenger to collect feedback about the flying experience.

**Goals**


*   Predict passenger satisfication

**Dataset Information**

*   **Gender**: Gender of the passengers (Female, Male)

*  **Customer** Type: The customer type (Loyal customer, disloyal customer)

*    **Age**: The actual age of the passengers

*    **Type of Travel**: Purpose of the flight of the passengers (Personal Travel, Business Travel)

*   **Class**: Travel class in the plane of the passengers (Business, Eco, Eco Plus)

*   **Flight distance**: The flight distance of this journey

*    **Inflight wifi service**: Satisfaction level of the inflight wifi service (0:Not Applicable;1-5)

*    **Departure/Arrival time convenient**: Satisfaction level of Departure/Arrival time convenient

* **Ease of Online booking**: Satisfaction level of online booking

* **Gate location**: Satisfaction level of Gate location

* **Food and drink**: Satisfaction level of Food and drink

* **Online boarding**: Satisfaction level of online boarding

* **Seat comfort**: Satisfaction level of Seat comfort

* **Inflight entertainment**: Satisfaction level of inflight entertainment

* **On-board service**: Satisfaction level of On-board service

* **Leg room service**: Satisfaction level of Leg room service

* **Baggage handling**: Satisfaction level of baggage handling

* **Check-in service**: Satisfaction level of Check-in service

*  **Inflight service**: Satisfaction level of inflight service

*  **Cleanliness**: Satisfaction level of Cleanliness

*  **Departure Delay in Minutes**: Minutes delayed when departure

*  **Arrival Delay in Minutes**: Minutes delayed when Arrival

*  **Satisfaction**: Airline satisfaction level(Satisfied, neutral or dissatisfied)

# Conclusion

---

Using Airline Satisfaction dataset, we have succeeded in predicting will a passenger satisfied or neutral/dissatisified with the airline.

From the EDA, we get that,
* Both female and male equally concerned about the satisfaction, means gender doesn't give a full impact on the result. So we'll likely to drop it.
* Loyal customer gives a high result on the neutral or dissatisfied level. This should be highlighted to maintain the loyal customers.
* Business traveler satisfied more with the airline rather than the personal traveler
* Passenger in business class highly satisfied rather than passenger in economy class highly neutral or dissatisfied.
* Gate location doesn't giving much impact since it gives the same score.
* Age seems quiet balance means it's not necessarily affected much on the target variable
* Neutral or dissatisfied passenger higher than satisfed passenger by 13.4%

Algorithms that we try to find the model are Logistic Regression, Decision Tree Classifier, Random Forest Classifier, and XGBoost Classifier.

We compare the baseline model and model after tuning, these are the result,

**Base model result**

<img src='https://drive.google.com/uc?id=1WD7vhpsU0jmZ27UTmAarAHQ13lF9aOZg'>

**Model after tuning result**

<img src='https://drive.google.com/uc?id=1kx9dJgX-vxEUZN5qCx-V-SBGMR3UxTfO'>

In the base line model, Decision Tree and Random Forest is over-fit to training set, yet after we tune the model, they are at good-fit.

From the accuracy score and F1-Score **the best model out of all the models is XGBoost Model**, so we will use it in the model inference.
