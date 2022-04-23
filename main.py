import altair as alt
import pandas as pd

data = pd.read_csv("data.csv")

iris_chart = alt.Chart(data, title="title").mark_circle().encode(
    alt.X("cty", title="x"),
    alt.Y("hwy", title="y"),
    alt.Color("manufacturer")
).properties(width=400, height=300)

iris_chart

iris_chart.save("test_iris.png")