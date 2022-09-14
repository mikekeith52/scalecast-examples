import pandas as pd

obs = 100
test_length = 10
colors = ['#CCB6F9','#92E985']

x = pd.DataFrame(
    {
        'Fold':[0,1,2,3,4][::-1],
        'Train Data':[75,60,45,30,15][::-1],
        'Validation Data':[15]*5,
    }
)

y = pd.DataFrame(
    {
        'Fold':[0,1,2,3,4][::-1],
        'Dropped':[60,45,30,15,0][::-1],
        'Train Data':[15]*5,
        'Validation Data':[15]*5,
    }
)

z = pd.DataFrame(
    {
        'Fold':[0,1,2,3,4][::-1],
        'Train Data':[72,54,36,18,0][::-1],
        'Validation Data':[18]*5,
        'Dropped':[72,54,36,18,0],
    }
)