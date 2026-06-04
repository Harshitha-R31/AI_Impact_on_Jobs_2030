import streamlit as st
import pandas as pd
from collections import Counter
import plotly.express as px

df = pd.read_csv("data/AI_Impact_on_Jobs_2030.csv")

skills = []

for item in df["Required_Skills"]:
    skills.extend(item.split(","))

counter = Counter([x.strip() for x in skills])

skill_df = pd.DataFrame(
    counter.items(),
    columns=["Skill","Count"]
)

skill_df = skill_df.sort_values(
    "Count",
    ascending=False
).head(20)

fig = px.bar(
    skill_df,
    x="Count",
    y="Skill",
    orientation="h",
    title="Top Skills"
)

st.plotly_chart(fig,use_container_width=True)
