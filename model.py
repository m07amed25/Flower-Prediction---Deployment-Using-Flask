import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load CSV file
df = pd.read_csv('iris.csv')

print(df.head(5))
print('==========')


X = df.drop(columns='Class')
y = df['Class']

print(X)
print('==========')
print(y)
print('==========')


# Splitting Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Instantiate the mode
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

# Make Pickle file of The Model
pickle.dump(classifier, open('model.pkl', 'wb'))
