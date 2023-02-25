from xgboost import XGBClassifier

def train(X_train):
    y_train = X_train['status']
    X_train = X_train.drop(['status'],axis=1)

    xgbc = XGBClassifier(random_state=42)
    xgbc.fit(X_train,y_train)

    return xgbc