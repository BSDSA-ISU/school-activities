## Made By troy
print("Made by troy. use this as a base. so not copy and present it.")



from pandas import read_csv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn
import matplotlib.pyplot as plt

df = read_csv("./student_depression_dataset.csv", index_col=0)

dfclean = df.replace({"Male": 0, "Female":1,
  "Others": -1, "Unhealthy": 0,
  "Moderate": 1, "Healthy": 2,
  "'More than 8 hours'": 9,
  "'5-6 hours'": 5.5,
  "'Less than 5 hours'": 4,
  "'7-8 hours'": 7.5,
   "?": 0, "Yes": 1, "No": 0,
    "Pass": 1, "Fail": 0}).infer_objects(copy=False)


for i in dfclean["Degree"]:
    print(i)

M=0
F=0
for i in dfclean["Gender"]:
    if i == 1:
        F+=1
    elif i == 0:
        M+=1


X = dfclean[["Study Satisfaction" ,"Financial Stress", "Dietary Habits",
 "Age", "Sleep Duration", 
"suicidal thoughts", "Family History of Mental Illness",
 "CGPA", "Academic Pressure"]]
y = df["Depression"]

model = LogisticRegression()
model.fit(X, y)
prediction = model.predict(X)
cmatrix = confusion_matrix(y, prediction)

plt.figure(figsize=(8, 6))
seaborn.heatmap(cmatrix, annot=True, fmt="d")
plt.xlabel('Predicted Depression Status')
plt.ylabel('Actual Depression Status')
plt.title('Confusion Matrix: Student Depression Prediction')
plt.show()
plt.clf()

#show gender bar graph
plt.bar([1], [M], color="green", label=f"Male ({M})")
plt.bar([2], [F], color="pink", label=f"Female ({F})")
plt.legend()
plt.show()
plt.clf()


# show different degrees
# Course Counting
BPHARM = (dfclean["Degree"] == "B.Pharm").sum()
BSc = (dfclean["Degree"] == "BSc").sum()
BA = (dfclean["Degree"] == "BA").sum()
BCA = (dfclean["Degree"] == "BA").sum()
MTech = (dfclean["Degree"] == "M.Tech").sum()
MA = (dfclean["Degree"] == "MA").sum()
C12 = (dfclean["Degree"] == "'Class 12'").sum()
BTech = (dfclean["Degree"] == "B.Tech").sum()
BCom = (dfclean["Degree"] == "B.Com").sum()
MBBS = (dfclean["Degree"] == "MBBS").sum()
BArch = (dfclean["Degree"] == "B.Arch").sum()
MCom = (dfclean["Degree"] == "M.Com").sum()
PhD = (dfclean["Degree"] == "PhD").sum()
LLM = (dfclean["Degree"] == "LLM").sum()
BHM = (dfclean["Degree"] == "BHM").sum()
MHM = (dfclean["Degree"] == "MHM").sum()
plt.bar([1], [BPHARM], color="green", label=f"BPHARM ({BPHARM})")
plt.bar([2], [BSc], color="Yellow", label=f"BSc ({BSc})")
plt.bar([3], [BA], color="Magenta", label=f"BA ({BA})")
plt.bar([4], [BCA], color="blue", label=f"BCA ({BCA})")
plt.bar([5], [MTech], color="Orange", label=f"Mtech ({MTech})")
plt.bar([6], [MA], color="Red", label=f"MA ({MA})")
plt.bar([7], [C12], color="Violet", label=f"Class 12 ({C12})")
plt.bar([8], [BTech], color="Black", label=f"Btech ({BTech})")
plt.bar([9], [BCom], color="Purple", label=f"Bcom ({BCom})")
plt.bar([10], [MBBS], color="Gray", label=f"MBBS ({MBBS})")
plt.bar([11], [BArch], label=f"B.arch ({BArch})")
plt.bar([12], [MCom], label=f"M.Com ({MCom})")
plt.bar([13], [PhD], label=f"Phd ({PhD})")
plt.bar([14], [LLM], label=f"LLM ({LLM})")
plt.bar([15], [BHM], label=f"BHM ({BHM})")
plt.bar([16], [MHM], label=f"MHM ({MHM})")
plt.legend()
plt.show()
plt.clf()




acc = accuracy_score(y, prediction)
#acc = accuracy_score(sss, y)
print(y)
print("Accuracy" ,acc*100, "%")
print("Intercept:", model.intercept_)
print("kill Me plss")





