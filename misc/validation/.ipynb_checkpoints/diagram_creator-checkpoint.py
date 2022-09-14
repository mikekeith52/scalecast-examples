import diagram_cfg
import matplotlib.pyplot as plt

def create_cv():
    _, ax = plt.subplots()
    diagram_cfg.x.set_index('Fold').plot.barh(
        stacked=True,
        color=diagram_cfg.colors, 
        legend=False, 
        figsize=(12,8),
        ax=ax
    )

    backwards = list(range(diagram_cfg.x.shape[0]))
    for i, v in diagram_cfg.x.iterrows():
        plt.text(4,backwards[i] - .1,'Train',color='#615F66',size=14)
        plt.text(v['Train Data']+ 4,backwards[i] - .1,'Val',color='#615F66',size=14)

    ax.axvline(75,color = 'white',ymax=1)
    ax.axvline(60,color = 'white',ymax=.8)
    ax.axvline(45,color = 'white',ymax=.6)
    ax.axvline(30,color = 'white',ymax=.4)
    ax.axvline(15,color = 'white',ymax=.2)

    plt.title('Time Series Cross-Validation',size=20)
    plt.ylabel('Fold',size=16)
    plt.xlabel('Time Observation Index',size=16)
    plt.show()

def create_rolling_cv():
    _, ax = plt.subplots()
    diagram_cfg.y.set_index('Fold').plot.barh(
        stacked=True,
        color=['white'] + diagram_cfg.colors, 
        legend=False, 
        figsize=(12,8),
        ax=ax,
    )

    backwards = list(range(diagram_cfg.y.shape[0]))
    for i, v in diagram_cfg.y.iterrows():
        plt.text(v['Train Data'] + v['Dropped'] - 15 + 4,backwards[i] - .1,'Train',color='#615F66',size=14)
        plt.text(v['Train Data'] + v['Dropped'] + 4,backwards[i] - .1,'Val',color='#615F66',size=14)
        ax.axvline(15*(i+1),color = 'white')

    plt.title('Rolling Time Series Cross-Validation',size=20)
    plt.ylabel('Fold',size=16)
    plt.xlabel('Time Observation Index',size=16)
    plt.show()