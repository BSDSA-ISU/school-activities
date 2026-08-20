# Activity: Exploratory Data Analysis

- [Activity: Exploratory Data Analysis](#activity-exploratory-data-analysis)
  - [Project Overview](#project-overview)
  - [Dataset Selection](#dataset-selection)
  - [Activity Requirements](#activity-requirements)
  - [Deliverables](#deliverables)
  - [Grading Rubric](#grading-rubric)
  - [Example: Flight Delays Analysis](#example-flight-delays-analysis)
    - [Background](#background)
    - [Exercises](#exercises)

![aaa](./koishi-mmd.gif)

---

## Project Overview

What are the first steps to take when you start a project or get ahold of a new dataset?

In a real data science project, you will typically have a question or idea brought to you:

- How are people interacting with the new version of my software?
- How is weather in Echague changing in the last decade?
- What type of people are most likely to enroll in Data Science Analytics?

You will sometimes be given a dataset when asked one of these questions, or more often, a general description of the data you could get if you talked to the right people or interacted with the right software systems.

---

## Dataset Selection

Choose one of the following two options:

1. A dataset from the [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets) page
2. Your own data

---

## Activity Requirements

Complete the following tasks:

1. **Team Formation:** Identify team members (2 members per team).
2. **Broad Question:** Formulate a broad research question.
3. **Exploratory Data Analysis (EDA):** Perform EDA and describe the exact steps taken to arrive at your conclusions.
4. **Data Visualization:** Develop at least one visualization (or more) that tells a story about your specific research question/hypothesis.
   > **Note:** The story may very well be something along the lines of: *"We thought variable X would affect measure Y in way Z, but the evidence does not support that."*
5. **Data Collection Context:** Address critical questions regarding how the data was collected:
   - Is it a sample of a larger dataset?
   - If so, how was the sampling done (e.g., randomly, all cases during a specific timeframe, all data for a selected set of users)?
   - *Note:* Answers to these questions strongly impact the conclusions you can draw.
6. **Visual Progression:** Show a clear progression of visualizations that follow an exploratory narrative.

---

## Deliverables

1. **Documentation:** A detailed report of the steps performed and results achieved.
2. **Codebase:** A Python or R codebase demonstrating your full exploration process.

---

## Grading Rubric

| Criteria | Points |
| :--- | :---: |
| **Dataset Collection & Description** | 15 pts |
| **Pre-processing & Cleaning** | 25 pts |
| **Descriptive Statistics & Visualization** | 25 pts |
| **Outlier & Missing Data Analysis** | 15 pts |
| **Insights & Hypotheses** | 20 pts |
| **Total** | **100 pts** |

---

## Example: Flight Delays Analysis

### Background

Here are data about flight delays from [Kaggle](https://www.kaggle.com/usdot/flight-delays). There are three tables of data.

> **Note:** The full set of flight data has more than 5.8 million flights. To start, you are given a subset that includes all flights in the first 15 days of January 2015 and the first 15 days of July 2015. If at the end you wish to try your analysis on the whole dataset, you can download the original `.csv` file from the Kaggle page and substitute a link to it in your code.

There is a ton of data here, and it can be easy to be overwhelmed. We are going to focus our exploration by considering the following broad research question: **Which flights are most likely to be delayed?**

### Exercises

- **Exercise 15.1 (Data Source):** Where does this data come from? Who collected it?
- **Exercise 15.2 (Explore Codebook):** Review the codebook on the Kaggle site to understand which variables are contained in each of the three tables.
  - What are the levels of `CANCELLATION_REASON` and what do they mean?
  - What is the unit of observation for each table?
- **Exercise 15.3 (Possible Joins):** What variables link the three tables? How could you join data from one table to another?
- **Exercise 15.4 (Visualize and Describe):** Use univariate and bivariate visualizations to start exploring the dataset:
  - What do you see that is interesting?
  - Which values are most common or unusual (outliers)?
  - Is there a lot of missing data?
  - What type of variation occurs within the individual variables?
  - What might be causing the interesting findings?
  - How could you figure out whether your ideas are correct?
- **Exercise 15.5 (Formulate Specific Question):** Based on your preliminary visualizations and exploration, formulate a more specific research question, hypothesis, or conclusion within this broad area of understanding flight delay causes.
