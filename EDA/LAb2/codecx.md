# i want 2 kms lmao

## Sheeesh

1

### Step 1: Place files in the same folder

Make sure `CampaignSpending.csv` and `CPS_2018.csv` are in the **same folder** as your `.Rmd` file.

### Step 2: Copy & Paste this into RMarkdown

```md
---
title: "Lab Activity 2: Visualizing & Modeling Relationships"
output: html_document
---

7

## 1. Votes vs. Incumbency

### a. Visualization

```{r task1-plot}
ggplot(campaign_data, aes(x = incumb, y = votes1st, fill = incumb)) +
  geom_boxplot() +
  labs(
    title = "1st Preference Votes by Incumbency",
    x = "Incumbent Status",
    y = "1st Preference Votes"
  )

```

### b. Linear Model

```{r task1-model}
model1 <- lm(votes1st ~ incumb, data = campaign_data)
summary(model1)

```

**Model Formula:**


$$\text{votes1st} = \beta_0 + \beta_1 \cdot \text{incumbYes}$$

* **Interpretation:**
* Intercept ($\beta_0$): [Write your interpretation here]
* `incumbYes` ($\beta_1$): [Write your interpretation here]



### c. Average Votes

```{r task1-means}
# Compute baseline challenger mean and incumbent mean
coef(model1)[1]                   # Challenger average votes
coef(model1)[1] + coef(model1)[2] # Incumbent average votes

```

---

## 2. Votes vs. Incumbency Status & Campaign Spending

### a. Visualization

```{r task2-plot}
ggplot(campaign_data, aes(x = totalexp, y = votes1st, color = incumb)) +
  geom_point(alpha = 0.6) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(
    title = "Votes vs Expenditure by Incumbency",
    x = "Total Spending",
    y = "1st Preference Votes"
  )

```

### b. Additive Model (`model2`)

```{r task2-model}
model2 <- lm(votes1st ~ totalexp + incumb, data = campaign_data)
summary(model2)

```

**Formulas:**

1. **Full Model:** $\text{votes1st} = \beta_0 + \beta_1(\text{totalexp}) + \beta_2(\text{incumbYes})$
2. **Challengers:** $\text{votes1st} = \beta_0 + \beta_1(\text{totalexp})$
3. **Incumbents:** $\text{votes1st} = (\beta_0 + \beta_2) + \beta_1(\text{totalexp})$

### c. Interpret Coefficients

* Intercept ($\beta_0$): [Write your interpretation here]
* `totalexp` ($\beta_1$): [Write your interpretation here]
* `incumbYes` ($\beta_2$): [Write your interpretation here]

### d & e. Predictions

```{r task2-predict}
new_candidates <- data.frame(
  incumb = c("No", "Yes"),
  totalexp = c(10000, 10000)
)

predict(model2, newdata = new_candidates)

```

---

## 3. Interaction Models

### a. Interaction Formulas

* **Full Model:** $\text{votes1st} = \beta_0 + \beta_1(\text{totalexp}) + \beta_2(\text{incumbYes}) + \beta_3(\text{totalexp} \cdot \text{incumbYes})$
* **Challengers:** $\text{votes1st} = \beta_0 + \beta_1(\text{totalexp})$
* **Incumbents:** $\text{votes1st} = (\beta_0 + \beta_2) + (\beta_1 + \beta_3)(\text{totalexp})$

### b. Interaction Model & Predictions

```{r task3-model}
new_model <- lm(votes1st ~ totalexp * incumb, data = campaign_data)
summary(new_model)

# Predictions for 10,000 spenders
predict(new_model, newdata = new_candidates)

```

### c. Visualization

```{r task3-plot}
ggplot(campaign_data, aes(x = totalexp, y = votes1st, color = incumb)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(
    title = "Interaction Model: Differing Slopes & Intercepts",
    x = "Total Expenditure",
    y = "1st Preference Votes"
  )

```

**Commentary on differing slopes/intercepts:**
[Write your interpretation here]

### d. Interpret 4 Model Coefficients

* Intercept ($\beta_0$): [Write your interpretation here]
* `totalexp`: [Write your interpretation here]
* `incumbYes`: [Write your interpretation here]
* `totalexp:incumbYes`: [Write your interpretation here]

---

## 4. Correlation vs. Causation

**10 Confounding Variables:**

1. Age
2. Education level
3. Years of work experience
4. Industry / Occupation
5. Hours worked per week
6. Geographic region / Cost of living
7. Career tenure / Seniority
8. Full-time vs. Part-time status
9. Job stability
10. Household financial need

---

## 5. Including Covariates (Wages, Marital, Age)

### a. Model without interaction

```{r task5-model}
cps_mod1 <- lm(wage ~ marital + age, data = cps_data)
summary(cps_mod1)

```

### b. Visualization

```{r task5-plot}
ggplot(cps_data, aes(x = age, y = wage, color = marital)) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Wage vs. Age by Marital Status", x = "Age", y = "Wage")

```

**Do age and marital status interact?**
[Write your interpretation here]

### c & d. Worker Comparisons

* **20-year-olds difference:** [Write your interpretation here]
* **30-year-olds difference:** [Write your interpretation here]

---

## 6. Controlling for More Covariates

### Model

```{r task6-model}
cps_mod3 <- lm(wage ~ marital + age + educ + industry, data = cps_data)
summary(cps_mod3)

```

### Questions

* **a. Geometry of Model:** [Select: 12 parallel lines / 12 non-parallel lines / 12 parallel planes / 12 non-parallel planes]
* **b. Difference for 20-year-olds in Service Industry:** [Write your calculated value here]
* **c. Difference for 30-year-olds in Construction Industry:** [Write your calculated value here]
* **d. Interpretation of `maritalsingle`:** [Write your interpretation here]
* **e. Significance of changing coefficient:** [Write your explanation here]

---

## 7. Model 3 Coefficients Analysis

* **a. Reference level of industry:** [Write baseline industry name here]
* **b. Highest & Lowest Earning Industry:**
* Highest: [Write industry here]
* Lowest: [Write industry here]


* **c. Interpretation of education coefficient:** [Write your interpretation here]
* **d. Interpretation of management coefficient:** [Write your interpretation here]

```

Go ahead and get some sleep! You can run the code chunks and fill in your written interpretations whenever you wake up.

```