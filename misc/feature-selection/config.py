model_params = {
    'test_only' : True,
    'dynamic_testing' : False,
}

dynamic_tuning = False
stop_at = 100

grids = {
    'gbt':dict(
        n_estimators=[100],
        random_state=[20],
    ),
    'lasso':dict(
        alpha=[0.025],
    ),
    'xgboost':dict(
        n_estimators=[100,200,500],
        subsample=[0.8,0.9],
        max_depth=[1,2,3,6], 
    ),
}