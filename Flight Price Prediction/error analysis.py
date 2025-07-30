import pickle
import numpy as np
from sklearn.metrics import mean_absolute_error

with open('flight_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('X_test.pkl', 'rb') as f:
    X_test = pickle.load(f)
with open('y_test.pkl', 'rb') as f:
    y_test = pickle.load(f)

y_test = np.expm1(y_test)
y_pred = np.expm1(model.predict(X_test))

diff = (y_pred-y_test).to_frame('MeanError')
diff['Type of Error'] = diff['MeanError'].apply(lambda x: -1 if x < 0 else 1)

# This is telling me how much on average is my model overshooting (positive category) or undershooting (negative category)
print(np.round(diff.groupby('Type of Error')['MeanError'].mean()/np.abs(diff.groupby('Type of Error')['MeanError'].mean()).sum(),2))

# This is telling me how much is my model's median overshooting (positive category) or median undershooting (negative category)
print(np.round(diff.groupby('Type of Error')['MeanError'].median()/np.abs(diff.groupby('Type of Error')['MeanError'].median()).sum(),2))

# we will take the final ratio as 57.5:42.5 for the MAE to be distributed while calculating a range of prediction.
print(mean_absolute_error(y_test, y_pred)*0.575)
print(mean_absolute_error(y_test, y_pred)*0.425)



