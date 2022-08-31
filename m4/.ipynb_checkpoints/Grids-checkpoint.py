elasticnet = {
    'alpha':[i/10 for i in range(1,21)],
    'l1_ratio':[0,0.25,0.5,0.75,1],
}

gbt = {
    'max_depth':[2,3],
    'max_features':['sqrt',None],
    'n_iter_no_change':[5],
}

knn = {
    'n_neighbors':range(2,51,2),
}

lightgbm = {}

lasso = {
    'alpha':[i/100 for i in range(1,101)],
}

mlp = {
    'activation':['relu','tanh'],
    'hidden_layer_sizes':[(50,),(50,50,50,)],
    'solver':['lbfgs','adam'],
}

mlr = {
    'normalizer':['minmax'],
}

prophet = {
    'n_changepoints':range(5),
}

rf = {
    'max_depth':[2,5],
    'n_estimators':[100,500],
    'max_features':['auto','sqrt'],
    'max_samples':[.75,.9,1],
}

ridge = {
    'alpha':[i/100 for i in range(1,101)],
}

silverkite = {
    'changepoints':range(5),
}

sgd={
    'penalty':['l2','l1','elasticnet'],
    'l1_ratio':[0.15,0.5,0.85],
}

svr={
    'kernel':['linear'],
    'C':[.5,1,2,3],
    'epsilon':[0.01,0.1,0.5],
}

theta = {
    'theta':[0.5,1,1.5,2],
}

xgboost = {
     'gamma':[0,3],
}
