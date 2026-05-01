best_modle=grid.best_estimator_

ypred=grid.predict(Xtest)
ypred

print("Training Eff:",grid.score(Xtrain,ytrain))
print("Testing Eff:",grid.score(Xtest,ytest))
