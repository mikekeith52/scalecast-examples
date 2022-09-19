# M4

The M4 competition was held in 2018 and measured forecast accuracy on 100,000 time series of varying lenghts and frequencies. This repository shows the scalecast approach to the problem. It uses only scikit-learn models with automated hyperparameter and input selection. It intentionally avoids classic statistical methods. Currently, the best OWA achieved by any one model is 0.92 (ElasticNet), which is better than the best Naive benchmark, but not quite as good as ARIMA (0.90) or Theta (0.89). The goal is to see scalecast achieve better results than all benchmarks.

## Notebooks
- [01 - evaluate_models.ipynb](01---evaluate_models.ipynb)
- [02 - evaluate_accuracy.ipynb](02---evaluate_accuracy.ipynb)

## Resources
- [M4 repository](https://github.com/Mcompetitions/M4-methods)  
- [M4 publication](https://www.sciencedirect.com/science/article/pii/S0169207019301128)  

## Ideas for improvement
- Stacking models  
- Larger hyperparmaeter grids, especially for tree models  
- Nonlinear feature selection  