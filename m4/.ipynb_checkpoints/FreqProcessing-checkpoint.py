import numpy as np

def process_all(f,fcst_horizon,m):
    f.add_ar_terms(fcst_horizon)
    f.set_test_length(fcst_horizon)
    f.set_validation_length(
        fcst_horizon*2 
        if len(f.y) >= 100 
        else 1
    )
    f.add_time_trend('t')
    f.add_logged_terms('t',drop=True)
    f.integrate(
        max_integration=1,
        critical_pval=0.01
    )
    f.set_validation_metric('mae')
    
def process_Yearly(f,fcst_horizon,m=1):
    if len(f.y) >= 100:
        f.add_cycle(fcst_horizon)
    f.tune_test_forecast(
        f.models,
        dynamic_tuning=fcst_horizon,
        error='ignore',
        limit_grid_size=.5,
    )

def process_Quarterly(f,fcst_horizon,m=4):
    f.add_seasonal_regressors(
        'quarter',
        raw=False,
        sincos=True,
    )
    if len(f.y) >= 100:
        f.add_AR_terms((3,m))
        f.keep_smaller_history(250)
    f.tune_test_forecast(
        f.models,
        dynamic_tuning=fcst_horizon,
        error='ignore',
        limit_grid_size=.25,
    )
    
def process_Monthly(f,fcst_horizon,m=12):
    f.add_seasonal_regressors(
        'month',
        raw=False,
        sincos=True,
    )
    if len(f.y) >= 100:
        f.add_AR_terms((3,m))
        f.add_cycle(3) # quarterly
        f.keep_smaller_history(250)
    f.tune_test_forecast(
        f.models,
        dynamic_tuning=fcst_horizon,
        error='ignore',
        limit_grid_size=.25,
    )
    
def process_Weekly(f,fcst_horizon,m=1):
    f.add_seasonal_regressors(
        'week',
        raw=False,
        sincos=True,
    )
    if len(f.y) >= 100:
        f.add_AR_terms((2,13))
        f.add_cycle(13)
    f.tune_test_forecast(
        f.models,
        dynamic_tuning=fcst_horizon,
        error='ignore',
        limit_grid_size=.25,
    )
    
def process_Daily(f,fcst_horizon,m=1):
    f.add_seasonal_regressors(
        'dayofweek',
        raw=False,
        sincos=True
    )
    if len(f.y) >= 366:
        f.add_seasonal_regressors(
            'day',
            raw=False,
            sincos=True,
        )
        f.add_AR_terms((4,7))
        f.keep_smaller_history(900)
    if len(f.y) >= 100:
        f.add_cycle(365.25/4)
    f.tune_test_forecast(
        f.models,
        dynamic_tuning=fcst_horizon,
        error='ignore',
        limit_grid_size=.25,
    )
    
def process_Hourly(f,fcst_horizon,m=24):
    f.add_seasonal_regressors(
        'hour',
        'dayofweek',
        raw=False,
        sincos=True,
    )
    if len(f.y) >= 100:
        f.add_AR_terms((2,m))
    f.tune_test_forecast(
        f.models,
        dynamic_tuning=fcst_horizon,
        error='ignore',
        limit_grid_size=.25,
    )