from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

from sklearn import linear_model
boston = load_boston()

lr_model = linear_model.LinearRegression()
lr_fit = lr_model.fit(boston.data, boston.target)
coef = list(lr_fit.coef_)

feature = pd.DataFrame(list(boston.feature_names))
coef_t = pd.DataFrame(np.transpose(coef))
coefficients_df = pd.concat([feature, coef_t], axis = 1)
coefficients_df.columns = ['Feature', 'Coefficient']
print(coefficients_df)
#NOX has the most influence