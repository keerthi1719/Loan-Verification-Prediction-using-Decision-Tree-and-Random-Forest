import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("Loan_Data.csv")

x=df[["loan_amount","annual_income","total_payment"]]
y=df["verification_status"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.50,random_state=90)

model=DecisionTreeClassifier(random_state=90)

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

accuracy=accuracy_score(y_test,y_pred)
print("\naccurancy:",round(accuracy*100,2),"%")

cm=confusion_matrix(y_test,y_pred)
print("Confusion matrix")
print(cm)

print("Classification Report")
print(classification_report(y_test,y_pred))

new_customer = np.array([[8000,48000,3939]])
loan_amt, annual_inc, total_pay = new_customer[0]

# Get ranges for each category
verified = df[df["verification_status"] == "Verified"]
source_verified = df[df["verification_status"] == "Source Verified"]

def in_range(data, loan_amt, annual_inc, total_pay):
    return (data["loan_amount"].min() <= loan_amt <= data["loan_amount"].max() and
            data["annual_income"].min() <= annual_inc <= data["annual_income"].max() and
            data["total_payment"].min() <= total_pay <= data["total_payment"].max())

if in_range(verified, loan_amt, annual_inc, total_pay):
    print("Verified")
elif in_range(source_verified, loan_amt, annual_inc, total_pay):
    print("Source Verified")
else:
    print("Not Verified")
