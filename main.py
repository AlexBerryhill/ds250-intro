#Import Libraries
import altair as alt
import pandas as pd

#get the data
data = pd.read_csv("data.csv")

#create the Altair Chart
chart = alt.Chart(data, title="title").mark_circle().encode(
    alt.X("displ", title="Displ"),
    alt.Y("hwy", title="Hwy"),
    alt.Color("manufacturer")
).properties(width=400, height=300)

#Print the chart
chart

#Save the chart as a PNG
chart.save("screenshots/altair_viz_1.png")

#Print the Table for the report
print(data
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))