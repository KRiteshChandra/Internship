Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.3,random_state=42)

model=RandomForestRegressor(random_state=42)
params={
    "n_estimators":[100,150,200],
    "max_depth":[3,4,5,6,7]
}

grid= GridSearchCV(estimator=model,param_grid=params,cv=5)

grid.fit(Xtrain,ytrain)

print("Best params:",grid.best_params_)
print("Best score:",grid.best_score_)
