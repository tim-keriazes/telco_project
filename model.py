#imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from statsmodels.formula.api import ols



def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test


def map_setosa_knn(X_train, y_train, knn, fig_x=12.0, fig_y=5.0):
    plt.rcParams["figure.figsize"] = [fig_x, fig_y]
    plt.rcParams["figure.autolayout"] = True

    n_neighbors = knn.get_params()['n_neighbors']
    weights = knn.get_params()['weights']

    iris = datasets.load_iris()
    X = np.array(X_train[['sepal_length', 'sepal_width']])
    y = y_train.map({'setosa':0, 'versicolor':1, 'virginica':2})
    h = .02

    cmap_light = ListedColormap(['orange', 'cyan', 'cornflowerblue'])
    cmap_bold = ['c', 'darkorange', 'darkblue']

    clf = neighbors.KNeighborsClassifier(n_neighbors, weights='uniform')
    clf.fit(X, y)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure()

    plt.contourf(xx, yy, Z, cmap=cmap_light)

    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=iris.target_names[y],
    palette=cmap_bold, alpha=1.0, edgecolor="black")

    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.title("3-Class classification (k = %i, '%s')"
    % (n_neighbors, weights))

    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])

    plt.show()

    def get_numeric_X_cols(X_train, object_cols):
        '''
        takes in a dataframe and list of object column names
        and returns a list of all other columns names, the non-objects. 
        '''
    numeric_cols = [col for col in X_train.columns.values if col not in object_cols]
    
    return numeric_cols


def prep4model(df, target):
    '''
    prep4model takes in a dataframe and target
    - produces a list of object column names
    - splits data into X/y train/validate/test
    - produces a list of numeric column names
    - scales the X_train/validate/test
    returns: split & scaled data.
    '''
    # get object columns names
    object_cols = get_object_cols(df)
    
    # split data 
    X_train, y_train, X_validate, y_validate, X_test, y_test = train_validate_test(df, target)
    
    # get numeric column names
    numeric_cols = get_numeric_X_cols(X_train, object_cols)

    # scale data 
    X_train_scaled, X_validate_scaled, X_test_scaled = min_max_scale(X_train, X_validate, X_test, numeric_cols)
    
    return X_train, X_train_scaled, y_train, X_validate, X_validate_scaled, y_validate, X_test, X_test_scaled, y_test

def upsample_target(df, target, val):
    from sklearn.utils import resample
    # Upsample the dfing data to balance a class imbalance
    minority_upsample = resample( df[df[target] == val],   #DF of samples to replicate
                                replace = True,         #Implements resampling with replacement, Default=True
                                n_samples = len(df[df[target]!=val]), #Number of samples to produce
                                random_state= 8         #Random State seed for reproducibility
                                )
    #Then glue the upsample to the original
    return pd.concat([minority_upsample, df[df[target]!=val]])    


for col in df.columns:
    if np.issubdtype(df[col].dtype, np.number):
        df[col].hist()
        plt.title(col)
        plt.show()
        sns.boxplot(data=df, x=col)
        plt.show()
        print('--------')

#IQR
# steps to defining IQR/Tukey method:
# get the Q1 and Q3 values
# determine our multiplier
# use these qualities to assert abnormalities

# start with an inner fence calculation
# multiplier = 1.5
# # calculate our q1 and q3
# q1 = df.Examination.quantile(0.25)
# q3 = df.Examination.quantile(0.75)
# iqr = q3 - q1

# q1, q3, iqr

# inner or outer: 1.5 fence multiplier convention for inner, 3.0 mult convention for outer
# lower: q1 - mult* iqr
# upper: q3 + iqr*mult

# inner_lower_fence = q1 - (multiplier * iqr)
# inner_upper_fence = q3 + (multiplier * iqr)

# df[(df['Examination'] < inner_lower_fence) |  (df['Examination'] > inner_upper_fence)]


# z-score:
# subtract the data point from the mean, divide by the standard deviation
# remember our z score calculation:
#  (x - x_mean) / x_std

# z_scores = (df['Infant.Mortality'] - df['Infant.Mortality'].mean()) / df['Infant.Mortality'].std()

def outlier_treatment(datacolumn):
 sorted(datacolumn)
 Q1,Q3 = np.percentile(datacolumn , [25,75])
 IQR = Q3 - Q1
 lower_range = Q1 - (1.5 * IQR)
 upper_range = Q3 + (1.5 * IQR)
 return lower_range,upper_range