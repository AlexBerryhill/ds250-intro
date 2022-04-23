import altair as alt
import pandas as pd

data = pd.read_csv("data.csv")
print(data.head(2))

iris_chart = alt.Chart(data, title="title").mark_circle().encode(
    alt.X("cty", title="City"),
    alt.Y("hwy", title="Hwy"),
    alt.Color("manufacturer")
).properties(width=400, height=300)

iris_chart

iris_chart.save("test_iris.png")