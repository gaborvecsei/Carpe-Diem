import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def generate_plot(age, max_age=99):
    assert age <= max_age, "You outlived this script!"
    assert age > 1, "You can't be this young"

    a = np.arange(0, 10, 1)
    aa = []
    bb = []
    for i in a:
        aa.extend([i] * len(a))
        bb.extend(a)

    lifetime_spent = np.floor((age / max_age) * 100).astype(int)

    fig = plt.figure(figsize=(4, 5), facecolor="w")
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(aa[:age], bb[:age], s=250, facecolors="r", edgecolors='none')
    ax.scatter(aa[age - 1], bb[age - 1], s=400, color="r")
    ax.scatter(aa[age:max_age], bb[age:max_age], s=250, facecolors='none', edgecolors="b", alpha=0.2)
    # ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])

    ax.annotate("age 1", xy=(0, 0),
                xycoords='data',
                xytext=(-3, 5),
                textcoords='data',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3,rad=0.4"))
    ax.annotate("age 99", xy=(9, 8),
                xycoords='data',
                xytext=(11, 4),
                textcoords='data',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3,rad=0.3"))

    ax.text(10.5, 2, "You already spent more than")
    ax.text(10.5, 1, "{0}%".format(lifetime_spent), fontsize=16, fontweight="bold")
    ax.text(10.5, 0.3, "of your life time")

    return fig


def generate_and_save(age, file_path="carpe_diem_plot.png"):
    f = generate_plot(age)
    f.savefig(file_path, bbox_inches="tight")


def create():
    parser = argparse.ArgumentParser(description='Script to learn basic argparse')
    parser.add_argument('-a', '--age', help='Your age in years', required=True, type=int)
    parser.add_argument('-o', '--output', help='output image file path', default="carpe_diem_plot.png", type=str)

    args = vars(parser.parse_args())

    age = args["age"]
    file_path = args["output"]

    file_folder = Path(file_path).parent
    if not file_folder.is_dir():
        print("Folder did not existed so I created it: {0}".format(file_folder))
        file_folder.mkdir(parents=True)

    generate_and_save(age, file_path)

    print("Plot is generated at: {0}".format(file_path))
