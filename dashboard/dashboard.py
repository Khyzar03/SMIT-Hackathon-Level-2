import streamlit as st
from etl.extract import extract
from etl.transform import transform
from etl.load_cache import load_cache, save_cache
from analysis.stats import basic_stats
from analysis.visualizations import temp_graph, humidity_graph

def run_dashboard():
    st.title("🌦 Live Weather ETL Dashboard")

    city = st.text_input("Enter City:", value="Karachi")

    if st.button("Fetch Data"):
        cache = load_cache()

        # check cache first
        if city in cache:
            st.write(f"📌 Loaded from cache: {city}")
            raw = cache[city]
        else:
            raw = extract(city)
            save_cache(city, raw)
            st.write(f"🌐 API Fetched: {city}")

        df = transform(raw)

        # stats section
        stats = basic_stats(df)
        st.subheader("Weather Stats")
        st.json(stats)

        # graphs
        st.plotly_chart(temp_graph(df))
        st.plotly_chart(humidity_graph(df))
