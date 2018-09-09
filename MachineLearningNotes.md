# Machine Learning

* Data Preprocessing
	- Importing the libraries
		* numpy
			- Mathematical toolkit
			- Arrays toolkit
		* matplotlib.pyplot
			- Visualization
		* pandas
			- Data IO
			- Data manipulation
	- Importing the data (pandas)
		* Read the data
		* Split data into
			- Matrix of features (X)
			- Array of Prediction (y)
	- Handle missing data
		* Remove record with missing data
		* Replace missing data with column mean (sklearn.preprocessing - Imputer)
		* Replace missing data with column median (sklearn.preprocessing - Imputer)
		* Replace missing data with most frequent value (sklearn.preprocessing - Imputer)
		* Replace missing data with most frequent value in similar type of data
		* Predict the missing value using KNN (categorical data)
		* Treat missing data as another category (categorical data)
	- Handle categorical data
		* Label Encoding (sklearn.preprocessing - LabelEncoder)
			- In case of comparable data
			- Ex: [Low, Medium, High]
		* One Hot Encoding (sklearn.preprocessing - OneHotEncoder)
			- In case of non comparable data
			- Ex: [Male, Female]
			- Creates Dummy Variable with boolean data for each category value of every categorical feature column
			- Remove 1 Dummy Variable to avoid Dummy Variable Trap
	- Split data into Training & Testing dataset (sklearn.cross_validation - train_test_split)
		* Good Test Size (0.2, 0.25, 0.3)
		* Build model on Train Data
		* Verify model on Test Data
		* Calculate accuracy using Predicted values and test values
	- Feature Scaling
		* Necessary to avoid biased predictions
		* Fit scaler over train data and transform both train data and test data
		* Standardization
			- Denotes how many standard deviations away the value is from the mean
		* Normalization
			- Scales the values between 0 and 1
* Regression
	- Linear Regression Assumptions
		* Linearity
		* Homoscedasticity
		* Multivariate normality
		* Independence of errors
		* Lack of multicollinearity 
	- Simple Linear Regression (sklearn.linear_model - LinearRegression)
		* y = b<sub>0</sub> + b<sub>1</sub>\*x<sub>1</sub>
		* Fits a straight line with b1 slope and b0 offset on y axis
		* Squared Sum Error becomes minimum
	- Multiple Linear Regression (sklearn.linear_model - LinearRegression)
		* y = b<sub>0</sub> + b<sub>1</sub>\*x<sub>1</sub> + ... + b<sub>n</sub>\*x<sub>n</sub>
		* Fits a straight line depending upon features (x<sub>1</sub>...x<sub>n</sub>)
		* Squared Sum Error becomes minimum
		* Methods to build model
			- All-in
				* Use all features
				* Lazy approach
				* Not Recommended
			- Backward Elimination (Recommended, Fastest)
				* Select Significance Level (SL) (Around 0.05)
				* Fit the model with all features and remove the feature with highest P-value if P-value > SL
				* Repeat this until no more feature can be removed
			- Forward Selection
				* Select Significance Level (SL) (Around 0.05)
				* Fit all possible model with single feature at a time and add the feature with least P-value
				* Keep adding another feature to the model, fir the model and iteratively add new feature with lowest P-value less than SL
				* Repeat this until no more features can be added
			- Bidirectional Elimination (Stepwise Regression) (Too much computation)
				* Select Significance Level (SL) (Around 0.05)
				* For every pass of `Forward Selection`, run entire `Backward Elimination`
				* Repeat this until no more features can be added or removed
			- Score Comparison
				* Build all possible models (2<sup>N</sup>-1) (N - No. of features)
				* Use the one with best results
				* Exponential, Not scalable with higher no. of features
	- Polynomial Regression
		* y = b<sub>0</sub> + b<sub>1</sub>\*x<sub>1</sub> + b<sub>2</sub>\*x<sub>1</sub><sup>2</sup> + ... + b<sub>n</sub>\*x<sub>1</sub><sup>n</sup>
		* Fits a non-linear curve depending on the degree of equation
		* Expand the feature set by different powers of existing feature
		* Implement `Multiple Linear Regression` on expanded feature sets
		* Higher the degree of polynomial, better are the predictions