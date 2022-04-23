from turtle import width
import altair as alt
import pandas as pd

data = pd.read_csv("data.csv")

iris_chart = alt.Chart(data, title="title").mark_circle().encode(
    alt.X("x", title="x"),
    alt.Y("y", title="y"),
    alt.Color("Species")
).properties(width=400, height=300)

iris_chart

iris_chart.save("test_iris.png")