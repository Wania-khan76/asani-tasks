import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import date

# ---- UI Config ---- #
st.set_page_config(page_title="Call Dashboard", layout="wide")
st.title("📞 Call Analytics Dashboard")

# ---- Theme Selector ---- #
theme = st.selectbox("Choose Theme", ["Light", "Dark"])
bar_color = "black" if theme == "Dark" else "blue"

# ---- Date Picker ---- #
start_date = st.date_input("Start Date", date(2025, 4, 1))
end_date = st.date_input("End Date", date(2025, 4, 5))
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

# ---- Helper Function ---- #
def fetch_data(api_url):
    try:
        res = requests.get(api_url)
        if res.status_code == 200:
            json_data = res.json()
            data = json_data.get("data", [])
            count = json_data.get("total_count", 0)
            df = pd.DataFrame(data)
            if not df.empty and "time" in df:
                df["time"] = pd.to_datetime(df["time"])
            return df, count
    except Exception as e:
        st.error(f"Error fetching data: {e}")
    return pd.DataFrame(), 0

# ---- Outbound Calls ---- #
st.header("📤 Outbound Calls")
if st.button("Fetch Outbound Calls"):
    outbound_url = f"http://localhost:8000/api/v1/outbound-calls?start_date={start_date_str}&end_date={end_date_str}"
    df_outbound, count_outbound = fetch_data(outbound_url)
    st.metric("Total Outbound Calls", count_outbound)

    if not df_outbound.empty:
        df_outbound["date"] = df_outbound["time"].dt.date
        summary = df_outbound.groupby("date").size().reset_index(name="Calls")
        fig = px.bar(summary, x="date", y="Calls", title="📊 Outbound Calls per Day", color_discrete_sequence=[bar_color])
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("📋 Outbound Call Details"):
            st.dataframe(df_outbound)

            if "duration" in df_outbound.columns:
                avg_duration = df_outbound["duration"].mean()
                st.info(f"📈 Average Duration: {avg_duration:.2f} seconds")

            csv = df_outbound.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Outbound Calls as CSV", data=csv, file_name="outbound_calls.csv", mime="text/csv")

# ---- Connected Calls ---- #
st.header("✅ Connected Calls")
if st.button("Fetch Connected Calls"):
    connected_url = f"http://127.0.0.1:8000/api/v1/connected-calls?start_date={start_date_str}&end_date={end_date_str}"
    df_connected, count_connected = fetch_data(connected_url)
    st.metric("Total Connected Calls", count_connected)

    if not df_connected.empty:
        df_connected["date"] = df_connected["time"].dt.date
        summary = df_connected.groupby("date").size().reset_index(name="Calls")
        fig = px.bar(summary, x="date", y="Calls", title="📊 Connected Calls per Day", color_discrete_sequence=[bar_color])
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("📋 Connected Call Details"):
            st.dataframe(df_connected)

            if "duration" in df_connected.columns:
                avg_duration = df_connected["duration"].mean()
                st.info(f"📈 Average Duration: {avg_duration:.2f} seconds")

            csv = df_connected.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Connected Calls as CSV", data=csv, file_name="connected_calls.csv", mime="text/csv")

# ---- Connected Outbound Calls ---- #
st.header("📞 Connected Outbound Calls")
if st.button("Fetch Connected Outbound Calls"):
    connected_outbound_url = f"http://localhost:8000/api/v1/connected-outbound-calls?start_date={start_date_str}&end_date={end_date_str}"
    df_connected_outbound, count_connected_outbound = fetch_data(connected_outbound_url)
    st.metric("Total Connected Outbound Calls", count_connected_outbound)

    if not df_connected_outbound.empty:
        df_connected_outbound["date"] = df_connected_outbound["time"].dt.date
        summary = df_connected_outbound.groupby("date").size().reset_index(name="Calls")
        fig = px.bar(summary, x="date", y="Calls", title="📊 Connected Outbound Calls per Day", color_discrete_sequence=[bar_color])
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("📋 Connected Outbound Call Details"):
            st.dataframe(df_connected_outbound)

            if "duration" in df_connected_outbound.columns:
                avg_duration = df_connected_outbound["duration"].mean()
                st.info(f"📈 Average Duration: {avg_duration:.2f} seconds")

            csv = df_connected_outbound.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Connected Outbound Calls as CSV", data=csv, file_name="connected_outbound_calls.csv", mime="text/csv")
