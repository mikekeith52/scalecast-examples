model_params = {
    'test_only' : True,
    'dynamic_testing' : False,
}

dynamic_tuning = False
stop_at = 'auto'

grids = {
    'gbt':dict(
        n_estimators=[10000],
        max_depth=[2],
        max_features=['log2'],
        random_state=[20],
    ),
    'lasso':dict(
        alpha=[0.025],
    ),
    'xgboost':dict(
        n_estimators=[2000,5000,10000],
        subsample=[0.8,0.9],
        max_depth=[1,2,3,6], 
    ),
}