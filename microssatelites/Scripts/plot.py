import matplotlib.pyplot as plt
import numpy as np
import os

def pyplot(path, title_graph, values, title_label, labels):
    fig, ax = plt.subplots(figsize=(10, 4), subplot_kw=dict(aspect="equal"))

    data = values


    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return "{:.1f}% ({:d})".format(pct, absolute)


    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="black"),
                                      pctdistance = 1.3)

    ax.legend(wedges, labels,
              title=title_label,
              loc="center left",
              bbox_to_anchor=(1.2, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title(title_graph)

    # plt.show()
    nstitle_graph = title_graph.replace(' ', '_')
    if os.path.isdir(f'{path}/Plots'):
        plt.savefig(f'{path}/Plots/{nstitle_graph}.png')
    else:
        os.system(f'mkdir {path}/Plots')
        plt.savefig(f'{path}/Plots/{nstitle_graph}.png')
