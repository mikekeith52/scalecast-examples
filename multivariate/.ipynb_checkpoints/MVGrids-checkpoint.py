
elasticnet = {
	'alpha':[i/10 for i in range(1,21)],
	'l1_ratio':[0,0.25,0.5,0.75,1],
	'normalizer':['scale','minmax',None],
	'lags':[1,3,10,13]
}

gbt = {
	'max_depth':[2,3],
	'max_features':['sqrt',None],
	'lags':[1,3,10,13]
}

knn = {
	'n_neighbors':range(2,21),
	'weights':['uniform','distance'],
	'lags':[1,3,10,13]
}

lightgbm = {
	'max_depth':[2,3],
	'lags':[1,3,10,13]
}

mlp = {
	'activation':['relu','tanh'],
	'hidden_layer_sizes':[(25,),(25,25,)],
	'solver':['lbfgs','adam'],
	'normalizer':['minmax','scale'],
	'random_state':[20],
	'lags':[1,3,10,13]
}

mlr = {
	'normalizer':['scale','minmax',None],
	'lags':[1,3,10,13]
}

rf = {
	'max_depth':[2,5],
	'n_estimators':[100,500,1000],
	'lags':[1,3,10,13]
}

svr={
	'kernel':['linear'],
	'C':[.5,1,2,3],
	'epsilon':[0.01,0.1,0.5],
	'lags':[1,3,10,13]
}

xgboost = {
	'max_depth':[2,3],
	'lags':[1,3,10,13]
}
