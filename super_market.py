import numpy as np 
import pandas as pd
from statistics import mode
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from datetime import datetime
df = pd.read_csv('supermarket_sales.csv')

# print(df.tail().T)


# print(df[df.duplicated(keep=False)])
# print(df.isna().sum())
# print(df.describe())
# df.info()
categoricals = ["Branch ", "City" , " Customer type" , "Gender" , "Product line" , "Payment"]
numericals = ["Unit price", "Quantity", "Tax 5%", "gross margin percentage", "gross income","Total", "Rating"] 

months = ["January", "February", "March",
         "April", "May", "June", "July",
         "August", "September", "October", "November",
         "December"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
           "Friday", "Saturday", "Sunday"]

def convert_date(x) :
     date = datetime.strptime(x, "%m/%d/%Y")
     return [months[date.month -1], date.day , weekdays[date.isoweekday() -1]]


df.head()

categoricals = ["Branch", "City", "Customer type", "Gender", "Product line",
               "Payment"]
numericals = ["Unit price", "Quantity", "Tax 5%", "gross margin percentage", "gross income",
             "Total", "Rating"]
months = ["January", "February", "March",
         "April", "May", "June", "July",
         "August", "September", "October", "November",
         "December"]

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday",
           "Friday", "Saturday", "Sunday"]
def convert_date(x):
    date = datetime.strptime(x, "%m/%d/%Y")
    return [months[date.month-1], date.day, weekdays[date.isoweekday()-1]]

def plot(df, name, num, axes):
    grouped = df.groupby(name)
    mean = grouped[num].mean()
    sns.barplot(x=mean.index, y=mean, ax=axes)
    for container in axes.containers:
        axes.bar_label(container, rotation=90, label_type="center")
    axes.set_xticklabels(axes.get_xticklabels(), rotation=90)
    
df["month"] = df["Date"].apply(lambda x: convert_date(x)[0])
df["day"] = df["Date"].apply(lambda x: convert_date(x)[1])
df["weekday"] = df["Date"].apply(lambda x: convert_date(x)[2])
df["Hour"] = df["Time"].apply(lambda x: int(x.split(':')[0]))



fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
sns.kdeplot(df, x="Total", hue="month", ax=axes[1])
sns.kdeplot(df, x="Total", hue="weekday", ax=axes[0])
plt.show()


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
sns.kdeplot(df, x="Rating", hue="month", ax=axes[0])
sns.kdeplot(df, x="Rating", hue="weekday", ax=axes[1])
plt.show()
print(df["month"].unique())

p=df[df['day']==6]
print(p.Total.sum(), p)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6),)
plot(df, "day" , 'Total', axes[0])
plot(df, "day", "Rating", axes[1])
plt.show()




sns.kdeplot(df , x='Hour' ,color="red",fill=True)
plt.show()

# print(df[categoricals[1]].value_counts()) 
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 6))
index = 0
for i in range(2):
    for j in range(3):
        df[categoricals[index]].value_counts().plot(kind="bar", ax=axes[i][j])
        index += 1
        for container in axes[i][j].containers:
            axes[i][j].bar_label(container)
        
plt.tight_layout()
plt.show()

print(df.columns)
cor = df.iloc[:, [6,7,8,14,15,16,]].corr()

plt.figure(figsize=(8,5))
sns.heatmap(cor, annot=True, linewidths=0.4, linecolor="darkgreen",annot_kws={'size': 11, 'rotation': 45}, fmt='.3f', cmap="Greens")
plt.show() 

df['Date'] = pd.to_datetime(df['Date'])

print(df['Date'])

Dayly_gross_income = df.groupby(df['Date'].dt.to_period('D'))['gross income'].sum()

# Membuat plot garis
Dayly_gross_income.plot(kind='line', marker='o', figsize=(10, 6))
plt.title('Dayly Gross Income')
plt.xlabel('Day')
plt.ylabel('Gross Income')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()




toto = df[df["month"]== "March"]
print(toto.Total.count())
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6),)
plot(df, "month" , 'Total', axes[0])
plot(df, "month", "Rating", axes[1])
plt.show()
import plotly.express as px
fig = px.bar(df, x="Gender", y="Total", color="Payment")
fig.show()

ProductRating = df.groupby('Product line')['Rating'].mean().sort_values(ascending=False)

col = {
    'Product' : ProductRating.index,
    'Ratings' : ProductRating.values
}
ProductRating = pd.DataFrame(col)

fig = px.bar(ProductRating, x='Ratings', y='Product', title='Product Line Average Ratings', color="Ratings", orientation='h')
fig.show()