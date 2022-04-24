import altair as alt
import pandas as pd

data = pd.read_csv("data.csv")
print(data.head(2))

chart = alt.Chart(data, title="title").mark_circle().encode(
    alt.X("cty", title="City"),
    alt.Y("hwy", title="Hwy"),
    alt.Color("manufacturer")
).properties(width=400, height=300)

chart

# chart.save("test_iris.png")

print(data
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))