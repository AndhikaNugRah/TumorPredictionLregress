import numpy as np
#parameter x represents the size of a tumor in centimeters.
x_param = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
#Note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.

#parameter y represents whether or not the tumor is cancerous (0 for "No", 1 for "Yes").
y_param = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

from sklearn import linear_model
logr_model=linear_model.LogisticRegression()
Model_Pred=logr_model.fit(x_param,y_param)

#predict if tumor is cancerous where the size is 3.46mm:
predicted_result = logr_model.predict(np.array([3.46]).reshape(-1,1))
print(predicted_result)

log_odds = logr_model.coef_
odds=np.exp(log_odds)
oddsz=int(odds[0])
print("Size the tumor increases by 1mm being cancerous tumor increases by",oddsz,'times')

#to make the model mor interpreatable, 
# #create a probability function for details about cancerous percentage 
def logit2prob(logr,x):
  log_odds = logr.coef_ * x + logr.intercept_
  odds = np.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)

print(logit2prob(logr_model, x_param))

def predicted_result():
    while True:
        try:
            X = float(input("Input Tumor Size (in mm): "))
            break
        except ValueError:
            print("Invalid input. Please enter a float value.")
    class_label={1:'Positive', 0:"Negative"}

    x_param = logr_model.predict(np.array([X]).reshape(1,1))
    Model_Pred = class_label[int(x_param)]
                             
    print(f"if the tumor sized {X} we predict the result is : {Model_Pred} ")
    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() == "yes":
        predicted_result()  # recursive call to go back to the beginning
    else:
        print("Goodbye, thanks for using our service!  - Dhika")

predicted_result()