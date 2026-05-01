#Saved clean data
df1.to_csv("clean_df.csv")

joblib.dump(best_modle,"rf_model.joblib")

joblib.dump(Xtrain.columns.tolist(),"model_columns.joblib")
