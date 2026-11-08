import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    line_data = df.copy()
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(line_data.index, line_data["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    bar_data = df.copy()
    bar_data["year"] = bar_data.index.year
    bar_data["month"] = bar_data.index.month
    bar_data = bar_data.groupby(["year", "month"])["value"].mean().unstack()

    fig = bar_data.plot(kind="bar", figsize=(12, 8)).figure
    ax = fig.axes[0]
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        title="Months",
    )
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    box_data = df.copy().reset_index()
    box_data["year"] = box_data["date"].dt.year
    box_data["month"] = box_data["date"].dt.strftime("%b")
    box_data["month_num"] = box_data["date"].dt.month
    box_data = box_data.sort_values("month_num")

    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    sns.boxplot(data=box_data, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(data=box_data, x="month", y="value", ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
