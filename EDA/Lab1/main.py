import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import json
import matplotlib.ticker as ticker

with open("./censorship_index.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data["data"])

# df = df.head(10000)

# Basic eda

print(df.head(5))

# show the shape
print(df.shape)

# show the variables
print(df.info())

# Columns
print(df.isna().sum())

# Desriptive stat
pd.set_option("display.float_format", lambda x: "%.2f" % x)
print(df.describe())

# Top 15 Censored country
def Censored_top_15():
    top15 = df.nlargest(15, "censorship_score").sort_values("censorship_score")

    plt.figure(figsize=(10, 7))
    plt.barh(top15["country_name"], top15["censorship_score"])
    plt.xlabel("Censorship Score")
    plt.ylabel("Country")
    plt.title("Top 15 Countries by Censorship Score")
    plt.tight_layout()
    plt.show()

# ISPS COunt
def isp():
    plt.figure(figsize=(9, 6))
    plt.scatter(df["isp_count"], df["censorship_score"], alpha=0.7)

    plt.xlabel("Number of ISPs")
    plt.ylabel("Censorship Score")
    plt.title("ISP Count vs Censorship Score")
    plt.tight_layout()
    plt.show()

# Block rate dist
def block_rate():
    plt.figure(figsize=(9, 6))
    plt.scatter(df["censorship_score"], df["block_rate"], alpha=0.7)

    plt.xlabel("Censorship Score")
    plt.ylabel("Block Rate (%)")
    plt.title("Censorship Score vs Block Rate")
    plt.tight_layout()
    plt.show()

# Threat level distribution
def threat_dist():
    threat_counts = df["threat_level"].value_counts()

    plt.figure(figsize=(8, 5))
    plt.bar(threat_counts.index, threat_counts.values)

    plt.xlabel("Threat Level")
    plt.ylabel("Number of Countries")
    plt.title("Distribution of Countries by Threat Level")
    plt.tight_layout()
    plt.show()

# Average block rate by threat level
def average_block_rate():
    avg_block = (
        df.groupby("threat_level")["block_rate"]
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(8, 5))
    plt.bar(avg_block.index, avg_block.values)

    plt.xlabel("Threat Level")
    plt.ylabel("Average Block Rate (%)")
    plt.title("Average Block Rate by Threat Level")
    plt.tight_layout()
    plt.show()

# blocked vs unblocked
def blocked_vs_unblocked():
    df["unblocked_measurements"] = (
        df["total_measurements"] - df["blocked_measurements"]
    )
    top_measurements = (
        df.nlargest(15, "total_measurements")
        .sort_values("total_measurements")
    )

    plt.figure(figsize=(10, 7))

    plt.barh(
        top_measurements["country_name"],
        top_measurements["blocked_measurements"],
        label="Blocked"
    )

    plt.barh(
        top_measurements["country_name"],
        top_measurements["unblocked_measurements"],
        left=top_measurements["blocked_measurements"],
        label="Unblocked"
    )

    plt.xlabel("Measurements")
    plt.ylabel("Country")
    plt.title("Blocked vs Unblocked Measurements")
    plt.legend()

    plt.tight_layout()
    plt.show()

# Measurement vs blockrate
def plot_measurements_vs_blockrate():
    plt.figure(figsize=(10, 6))
    
    # Custom color mapping for clear threat-level contrast
    palette = {
        'free': '#2ca02c',     # Green
        'low': '#1f77b4',      # Blue
        'medium': '#ff7f0e',   # Orange
        'high': '#d62728',     # Red
        'severe': '#9467bd'    # Purple
    }
    
    sns.scatterplot(
        data=df,
        x="total_measurements",
        y="block_rate",
        hue="threat_level",
        palette=palette,
        alpha=0.85,
        s=70
    )
    
    plt.xscale("log")
    
    # Formats the x-axis to show regular numbers (e.g., 1,000) instead of scientific notation (10^3)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
    
    plt.xlabel("Total Measurements (Number of Tests Ran)")
    plt.ylabel("Block Rate (0 = 0%, 1.0 = 100%)")
    plt.title("Total Measurements vs. Block Rate by Threat Level")
    plt.legend(title="Threat Level")
    plt.grid(True, which="both", ls="--", alpha=0.3)
    plt.tight_layout()
    plt.show()

 # Plot censorship heatmap
def plot_censorship_correlation_heatmap():
    metrics = [
        "isp_count",
        "total_measurements",
        "blocked_measurements",
        "block_rate",
        "censorship_score",
    ]
    corr_matrix = df[metrics].corr()

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
    plt.title("Correlation Heatmap of Key Censorship Metrics")
    plt.tight_layout()
    plt.show()


plot_censorship_correlation_heatmap()