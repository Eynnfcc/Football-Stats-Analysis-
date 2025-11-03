import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")

#------------------------------------------------
# Basic Overview
#------------------------------------------------
print("Total Goals:", len(df))
print("Total Opponents faced:", df['Opponent'].nunique())
print("Total Competitions:", df['Competition'].nunique())
print("\n")

#------------------------------------------------
# Left-footed, Right-footed, and Header distribution
#------------------------------------------------
type_counts = df['Type'].value_counts()
print("Goal Type Distribution:")
print(type_counts)
print("\n")

plt.figure(figsize=(10,8))
type_counts.plot(kind='bar', color=['gold', 'skyblue', 'lightcoral'])
plt.title("Goals by Type")
plt.xlabel("Goal Type")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()
plt.show()

#------------------------------------------------
# Top & Least Teams by Left Foot
#------------------------------------------------
left_footed = df[df["Type"] == "Left-footed shot"]
goals_by_team = left_footed["Opponent"].value_counts()
print("Top 5 teams Messi scored against by left foot:")
print(goals_by_team.head(5), "\n")
print("Lowest 5 teams Messi scored against by left foot:")
print(goals_by_team.tail(5), "\n")

plt.figure(figsize=(10,5))
goals_by_team.head(5).plot(kind='bar', color='gold')
plt.title("Top 5 Teams Scored Against (Left Foot)")
plt.xlabel("Opponent")
plt.ylabel("Goals")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#------------------------------------------------
# Top & Least Teams Overall
#------------------------------------------------
total_goals_by_team = df["Opponent"].value_counts()
print("Top 5 teams Messi scored against overall:")
print(total_goals_by_team.head(5), "\n")
print("Lowest 5 teams Messi scored against overall:")
print(total_goals_by_team.tail(5), "\n")

plt.figure(figsize=(10,5))
total_goals_by_team.head(5).plot(kind='bar', color='orange')
plt.title("Top 5 Teams Scored Against (Overall)")
plt.xlabel("Opponent")
plt.ylabel("Goals")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#------------------------------------------------
# Top 5 Assisters
#------------------------------------------------
top_assisters = df['Goal_assist'].value_counts().head(5)
print("Top 5 players who assisted Messi the most:")
print(top_assisters, "\n")

plt.figure(figsize=(10,4))
top_assisters.plot(kind='bar', color='limegreen')
plt.title("Top 5 Assisters")
plt.xlabel("Player")
plt.ylabel("Assists")
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()
plt.show()

#------------------------------------------------
# Headers Count
#------------------------------------------------
headers_count = len(df[df["Type"] == "Header"])
print(f"Messi scored {headers_count} headers from 2005 to 2023.\n")

#------------------------------------------------
# Real Madrid Analysis
#------------------------------------------------
madrid_goals = df[df["Opponent"] == "Real Madrid"]
madrid_type = madrid_goals["Type"].value_counts()
print("Goal types vs Real Madrid:")
print(madrid_type, "\n")

plt.figure(figsize=(14,4))
madrid_type.plot(kind='bar', color='red')
plt.title("Messi’s Goal Types vs Real Madrid")
plt.xlabel("Type")
plt.ylabel("Count")
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()
plt.show()

#------------------------------------------------
# Goals per Season
#------------------------------------------------
goals_per_season = df['Season'].value_counts().sort_index()
print("Goals per Season:")
print(goals_per_season)
print("\n")

plt.figure(figsize=(10,5))
goals_per_season.plot(kind='line', marker='o', color='orange')
plt.title("Messi Goals per Season (2005–2023)")
plt.xlabel("Season")
plt.ylabel("Goals")
plt.grid(True)
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()
plt.show()

#------------------------------------------------
# Goals per Competition
#------------------------------------------------
goals_by_comp = df['Competition'].value_counts()
print("Goals by Competition:")
print(goals_by_comp)
print("\n")

plt.figure(figsize=(8,5))
goals_by_comp.plot(kind='bar', color='cyan')
plt.title("Goals by Competition")
plt.xlabel("Competition")
plt.ylabel("Goals")
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()
plt.show()

#------------------------------------------------
# Foot Usage Ratio
#------------------------------------------------
left_count = len(df[df['Type'] == 'Left-footed shot'])
right_count = len(df[df['Type'] == 'Right-footed shot'])
header_count = len(df[df['Type'] == 'Header'])
total = len(df)

print(f"Left Foot: {left_count/total*100:.2f}%")
print(f"Right Foot: {right_count/total*100:.2f}%")
print(f"Header: {header_count/total*100:.2f}%\n")

plt.figure(figsize=(6,6))
plt.pie([left_count, right_count, header_count],
        labels=['Left Foot', 'Right Foot', 'Header'],
        autopct='%1.1f%%',
        colors=['gold', 'skyblue', 'lightcoral'],
        startangle=140)
plt.title("Goal Type Percentage (2005–2023)")
plt.show()

#------------------------------------------------
# Most common type of goal per opponent 
#------------------------------------------------
most_common_types = df.groupby("Opponent")["Type"].agg(lambda x: x.mode()[0])
print("Most common goal type per opponent:")
print(most_common_types.head(10))
print("\n")

#------------------------------------------------
# Top 10 Opponents by Goal Type Breakdown
#------------------------------------------------
top10_teams = df['Opponent'].value_counts().head(10).index
subset = df[df['Opponent'].isin(top10_teams)]
pivot = subset.pivot_table(index='Opponent', columns='Type', aggfunc='size', fill_value=0)
pivot.plot(kind='bar', stacked=True, figsize=(14,6))
plt.title("Top 10 Opponents — Goals Breakdown by Type")
plt.xlabel("Opponent")
plt.ylabel("Goals")
plt.legend(title='Goal Type', loc='center left', bbox_to_anchor=(1.02, 0.5))
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()
plt.show()

#------------------------------------------------
# Average Goals per Season 
#------------------------------------------------
avg_goals_per_season = goals_per_season.mean()
print(f"Average goals per season: {avg_goals_per_season:.2f}")

plt.figure(figsize=(6,4))
plt.bar(["Average Goals/Season"], [avg_goals_per_season], color='violet')
plt.title("Average Goals per Season (2005–2023)")
plt.ylabel("Goals")
plt.tight_layout()
