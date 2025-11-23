import plotly.express as px

def temp_graph(df):
    return px.line(df, x="datetime", y="temp", title="Temperature Over Time")

def humidity_graph(df):
    return px.line(df, x="datetime", y="humidity", title="Humidity Over Time")
