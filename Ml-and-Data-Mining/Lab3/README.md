# Decision Tree Classification Laboratory Activity

- [Decision Tree Classification Laboratory Activity](#decision-tree-classification-laboratory-activity)
  - [Learning Objectives](#learning-objectives)
  - [1. Establish the Classification Problem](#1-establish-the-classification-problem)
  - [2. Collect and Describe the Dataset](#2-collect-and-describe-the-dataset)
  - [3. Preprocess the Data and Perform Exploratory Data Analysis (EDA)](#3-preprocess-the-data-and-perform-exploratory-data-analysis-eda)
  - [4. Split the Data](#4-split-the-data)
  - [5. Build a Baseline Decision Tree Model](#5-build-a-baseline-decision-tree-model)
  - [6. Experiment with Decision Tree Parameters](#6-experiment-with-decision-tree-parameters)
    - [Parameters to Investigate](#parameters-to-investigate)
    - [Experiment Procedure](#experiment-procedure)
    - [Parameter Experimentation Summary Table](#parameter-experimentation-summary-table)
  - [7. Evaluate and Compare the Models](#7-evaluate-and-compare-the-models)
  - [8. Visualize and Interpret the Decision Tree](#8-visualize-and-interpret-the-decision-tree)
  - [9. Required Submission](#9-required-submission)
  - [10. Reflection Questions](#10-reflection-questions)

---

## Learning Objectives

- Identify a real-world classification problem that can be addressed using a Decision Tree.
- Prepare and explore a classification dataset containing at least 1,000 records (rows).
- Build and evaluate a baseline Decision Tree classifier in Python.
- Experiment with different Decision Tree parameters and compare their effects on model performance and complexity.
- Interpret the resulting tree, evaluation metrics, and evidence of underfitting or overfitting.

## 1. Establish the Classification Problem

Identify a real-world classification problem. Answer the following questions:

1. What problem do you want to solve?
2. What is the dependent (target) variable?
3. What are the independent (input) variables?
4. Why is the problem suitable for classification using a Decision Tree?

## 2. Collect and Describe the Dataset

The dataset must contain a minimum of **1,000 records (rows)*- before the train-test split. Datasets with fewer than 1,000 rows will not be accepted for this activity.

- Use a reliable source such as Kaggle, the UCI Machine Learning Repository, another credible open-data repository, or an instructor-approved dataset.
- Provide the dataset name, source, number of records, number of features, target variable, and a brief description of what each record represents.
- Confirm that the target variable contains at least two classes and report the number of records per class.

## 3. Preprocess the Data and Perform Exploratory Data Analysis (EDA)

- Check and handle missing or invalid values, if present.
- Encode categorical input variables using an appropriate method such as mapping, one-hot encoding, or `LabelEncoder` when appropriate.
- Scale numerical features only when needed for other comparisons; note that Decision Trees generally do not require feature scaling.
- Inspect value counts, feature distributions, duplicate records, and class balance.
- Briefly explain each preprocessing step and why it was necessary.

## 4. Split the Data

Divide the dataset into training (**80%**) and testing (**20%**) subsets using `train_test_split` from scikit-learn.

## 5. Build a Baseline Decision Tree Model

1. Import `DecisionTreeClassifier` from `sklearn.tree`.
2. Create a baseline model using the default parameters.
3. Train the model using the training dataset.
4. Generate predictions for both the training set and the testing set.
5. Record the baseline training accuracy and testing accuracy before changing any Decision Tree parameters.

## 6. Experiment with Decision Tree Parameters

Train and evaluate at least **three (3) Decision Tree configurations*- in addition to the baseline model. Change parameters systematically and document every trial.

### Parameters to Investigate

- **`criterion`**: Compare at least `gini` and `entropy` (or `log_loss` if supported in your environment).
- **`max_depth`**: Test at least three values, including a shallow tree and a deeper tree (for example: `3`, `5`, `10`, or `None`).
- **`min_samples_split`**: Test at least two values (for example: `2`, `5`, `10`, or `20`).
- **`min_samples_leaf`**: Test at least two values (for example: `1`, `2`, `5`, or `10`).
- **Optional extension**: Experiment with `max_features`, `splitter`, `class_weight`, or `ccp_alpha` if they are relevant to your dataset.

### Experiment Procedure

1. Begin with the baseline model.
2. Change one parameter at a time for the first set of trials so you can observe its individual effect.
3. After the individual tests, you may combine promising parameter values into one or more additional configurations.
4. Keep the same training/testing split and `random_state` for all trials.
5. For every configuration, record the parameter values, training accuracy, testing accuracy, precision, recall, F1-score, tree depth, and number of leaves.
6. Compare the models and explain which parameter changes reduced overfitting, caused underfitting, or improved generalization. Do not select a model based only on training accuracy.

### Parameter Experimentation Summary Table

| Trial    | Criterion | Max Depth | Min Split | Min Leaf | Train Acc. | Test Acc. | F1-Score | Depth | Leaves |
| -------- | --------- | --------: | --------: | -------: | ---------: | --------: | -------: | ----: | -----: |
| Baseline |           |           |           |          |            |           |          |       |        |
| Trial 1  |           |           |           |          |            |           |          |       |        |
| Trial 2  |           |           |           |          |            |           |          |       |        |
| Trial 3  |           |           |           |          |            |           |          |       |        |

## 7. Evaluate and Compare the Models

1. Use the trained models to predict the test dataset.
2. For each model, report accuracy, confusion matrix, and classification report (precision, recall, and F1-score).
3. Compare training and testing performance to identify possible overfitting or underfitting.
4. Identify the configuration that gives the most reasonable balance between predictive performance and model simplicity, and justify your choice using the recorded metrics.
5. Discuss which classes are predicted well and which classes are commonly misclassified.

## 8. Visualize and Interpret the Decision Tree

- Use `plot_tree` from `sklearn.tree` to visualize the selected Decision Tree model.
- If the tree is too large, visualize only a limited depth or use a readable figure size.
- Interpret at least three important splits and explain how the model uses feature values to make a classification decision.
- Compare the visual complexity of a shallow tree and a deeper tree from your experiments.

## 9. Required Submission

- Python notebook containing preprocessing, EDA, model training, parameter experiments, evaluation, and visualization.
- Dataset file or a working source link, with evidence that the dataset contains at least 1,000 rows.
- Completed parameter experimentation summary table.
- Interpretation of EDA, experimentation, and results, including answers to the reflection questions.

## 10. Reflection Questions

1. How does a Decision Tree decide where to split the data?
2. What happened to model performance when `max_depth` was increased or decreased?
3. How did changing `min_samples_split` or `min_samples_leaf` affect the complexity and generalization of the tree?
4. Did `gini` and `entropy` produce the same tree and performance? Explain the differences you observed.
5. Which experimental configuration provided the best balance between training performance, testing performance, and tree complexity? Support your answer with evidence from your results.
6. What are the advantages and limitations of Decision Trees for your chosen dataset?
