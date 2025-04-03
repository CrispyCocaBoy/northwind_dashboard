import duckdb
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Query duckdb
df = duckdb.query("""
SELECT cat.categoryname as CategoryName,  sum(od.Quantity) as Quantity
FROM sqlite_scan('northwind.db', 'Categories') as cat
JOIN sqlite_scan('northwind.db', 'products') as pd ON cat.CategoryID = pd.CategoryID
JOIN sqlite_scan('northwind.db', 'OrderDetails') as od ON pd.ProductID = od.ProductID
GROUP BY cat.categoryname
""").df()


# Grafico
fig = px.bar(
    df,
    x="Quantity",
    y="CategoryName",
    orientation="h",
    title="Quantità vendute per categoria",
    labels={"CategoryName": "Categoria", "Quantity": "Quantità"},
    color_discrete_sequence=["#17b897"]
)

# Layout Dash
external_stylesheets = [{
    "href": "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
    "rel": "stylesheet"
}]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Northwind Analytics"

app.layout = html.Div(children=[
    html.Div(children=[
        html.P("📦", className="header-emoji"),
        html.H1("Northwind Analytics", className="header-title"),
        html.P(
            "Visualizzazione della quantità totale di prodotti venduti per categoria.",
            className="header-description"
        ),
    ], className="header"),

    html.Div(children=[
        dcc.Graph(
            id="bar-chart",
            figure=fig,
            config={"displayModeBar": False}
        )
    ], className="wrapper"),
])

if __name__ == "__main__":
    app.run(debug=True)



