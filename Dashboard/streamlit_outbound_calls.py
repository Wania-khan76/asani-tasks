# # # # # # # # # import streamlit as st
# # # # # # # # # import pandas as pd
# # # # # # # # # import requests
# # # # # # # # # import datetime
# # # # # # # # # import matplotlib.pyplot as plt

# # # # # # # # # st.set_page_config(page_title="Outbound Calls Dashboard", layout="wide")

# # # # # # # # # st.title("📞 Outbound Calls Dashboard")

# # # # # # # # # # Select date range
# # # # # # # # # col1, col2 = st.columns(2)
# # # # # # # # # with col1:
# # # # # # # # #     start_date = st.date_input("Start Date", value=datetime.date(2025, 4, 1))
# # # # # # # # # with col2:
# # # # # # # # #     end_date = st.date_input("End Date", value=datetime.date(2025, 4, 5))

# # # # # # # # # if start_date > end_date:
# # # # # # # # #     st.warning("Start date must be before end date.")
# # # # # # # # # else:
# # # # # # # # #     if st.button("📥 Fetch Data"):
# # # # # # # # #         with st.spinner("Fetching data..."):
# # # # # # # # #             # Format dates
# # # # # # # # #             start_str = start_date.strftime("%Y-%m-%d")
# # # # # # # # #             end_str = end_date.strftime("%Y-%m-%d")
# # # # # # # # #             url = f"http://127.0.0.1:8000/api/v1/outbound-calls?start_date={start_str}&end_date={end_str}"
            
# # # # # # # # #             try:
# # # # # # # # #                 response = requests.get(url)
# # # # # # # # #                 response.raise_for_status()
# # # # # # # # #                 data = response.json()
# # # # # # # # #                 calls = data["calls"]

# # # # # # # # #                 if not calls:
# # # # # # # # #                     st.info("No calls found for selected date range.")
# # # # # # # # #                 else:
# # # # # # # # #                     # Convert to DataFrame
# # # # # # # # #                     df = pd.DataFrame(calls)
# # # # # # # # #                     df["time"] = pd.to_datetime(df["time"])

# # # # # # # # #                     # Total count
# # # # # # # # #                     st.metric("📊 Total Outbound Calls", len(df))

# # # # # # # # #                     # Prepare graph data
# # # # # # # # #                     df["date"] = df["time"].dt.date
# # # # # # # # #                     calls_per_day = df.groupby("date").size()

# # # # # # # # #                     # Plotting
# # # # # # # # #                     st.subheader("📈 Number of Calls per Day")
# # # # # # # # #                     fig, ax = plt.subplots()
# # # # # # # # #                     calls_per_day.plot(kind="bar", ax=ax, color="#4f8bf9")
# # # # # # # # #                     ax.set_xlabel("Date")
# # # # # # # # #                     ax.set_ylabel("Number of Calls")
# # # # # # # # #                     ax.set_title("Calls vs Dates")
# # # # # # # # #                     st.pyplot(fig)

# # # # # # # # #                     # Show table
# # # # # # # # #                     st.subheader("📋 Call Details Table")
# # # # # # # # #                     st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)

# # # # # # # # #             except requests.exceptions.RequestException as e:
# # # # # # # # #                 st.error(f"Error fetching data: {e}")

# # # # # # # # import streamlit as st
# # # # # # # # import plotly.graph_objects as go
# # # # # # # # import pandas as pd
# # # # # # # # from datetime import datetime, timedelta
# # # # # # # # import random

# # # # # # # # # Sample Data (replace with real data from your API)
# # # # # # # # dates = [datetime.now().date() - timedelta(days=i) for i in range(10)][::-1]
# # # # # # # # counts = [random.randint(20, 100) for _ in range(10)]
# # # # # # # # df = pd.DataFrame({"Date": dates, "Count": counts})

# # # # # # # # # Create a bar + line plot
# # # # # # # # fig = go.Figure()

# # # # # # # # # Bar chart
# # # # # # # # fig.add_trace(go.Bar(
# # # # # # # #     x=df["Date"],
# # # # # # # #     y=df["Count"],
# # # # # # # #     text=df["Count"],
# # # # # # # #     textposition='outside',
# # # # # # # #     marker=dict(
# # # # # # # #         color='rgba(255,0,0,0.6)',
# # # # # # # #         line=dict(color='rgba(255,0,0,1.0)', width=1.5)
# # # # # # # #     ),
# # # # # # # #     name='Call Count'
# # # # # # # # ))

# # # # # # # # # Line chart on top
# # # # # # # # fig.add_trace(go.Scatter(
# # # # # # # #     x=df["Date"],
# # # # # # # #     y=df["Count"],
# # # # # # # #     mode='lines+markers',
# # # # # # # #     name='Trend',
# # # # # # # #     line=dict(
# # # # # # # #         color='red',
# # # # # # # #         width=3,
# # # # # # # #         shape='spline'  # for smooth curves
# # # # # # # #     ),
# # # # # # # #     marker=dict(
# # # # # # # #         size=6,
# # # # # # # #         color='rgba(255,50,50,1)'
# # # # # # # #     )
# # # # # # # # ))

# # # # # # # # # Layout tweaks for clean design
# # # # # # # # fig.update_layout(
# # # # # # # #     title="Daily Call Counts",
# # # # # # # #     xaxis_title="Date",
# # # # # # # #     yaxis_title="Number of Calls",
# # # # # # # #     template="plotly_white",
# # # # # # # #     height=500,
# # # # # # # #     plot_bgcolor='rgba(0,0,0,0)',
# # # # # # # #     paper_bgcolor='rgba(0,0,0,0)',
# # # # # # # #     font=dict(size=14),
# # # # # # # #     margin=dict(t=60, l=20, r=20, b=40)
# # # # # # # # )

# # # # # # # # # Show in Streamlit
# # # # # # # # st.plotly_chart(fig, use_container_width=True)

# # # # # # # import streamlit as st
# # # # # # # import plotly.graph_objects as go
# # # # # # # import pandas as pd
# # # # # # # from datetime import datetime, timedelta
# # # # # # # import random
# # # # # # # import requests

# # # # # # # # Constants
# # # # # # # API_BASE_URL = "http://your_api_base_url"  # Replace with your API URL
# # # # # # # API_ENDPOINTS = {
# # # # # # #     "CALLS": "/calls"  # Replace with the correct API endpoint
# # # # # # # }

# # # # # # # # Fetch call data (Replace this with actual API call)
# # # # # # # def fetch_call_data(call_type, start_date, end_date):
# # # # # # #     # Construct the full API URL with parameters
# # # # # # #     url = f"{API_BASE_URL}{API_ENDPOINTS['CALLS']}"
# # # # # # #     params = {
# # # # # # #         "call_type": call_type,
# # # # # # #         "start_date": start_date,
# # # # # # #         "end_date": end_date
# # # # # # #     }
    
# # # # # # #     # Fetch the data (Here we use random data for the example)
# # # # # # #     response = requests.get(url, params=params)
    
# # # # # # #     # Simulating API response (for demonstration)
# # # # # # #     # This part should be replaced with actual logic to get the response from your API
# # # # # # #     if response.status_code == 200:
# # # # # # #         data = response.json()  # Assuming the API returns a JSON response
# # # # # # #         return data
# # # # # # #     else:
# # # # # # #         return []

# # # # # # # # Sample data (if you don't have an API, use this placeholder)
# # # # # # # dates = [datetime.now().date() - timedelta(days=i) for i in range(10)][::-1]
# # # # # # # counts = [random.randint(20, 100) for _ in range(10)]
# # # # # # # df = pd.DataFrame({"Date": dates, "Count": counts})

# # # # # # # # Fetch call data (assuming you're calling the API for real)
# # # # # # # # Replace these parameters with real inputs from the user
# # # # # # # call_type = "all"  # Example: 'all', 'outgoing', etc.
# # # # # # # start_date = datetime.now().date() - timedelta(days=10)
# # # # # # # end_date = datetime.now().date()

# # # # # # # # Uncomment this if you're using real API data
# # # # # # # # call_data = fetch_call_data(call_type, start_date, end_date)
# # # # # # # # df = pd.DataFrame(call_data)  # Replace this with actual call data

# # # # # # # # Create a Plotly bar + line chart
# # # # # # # fig = go.Figure()

# # # # # # # # Bar chart
# # # # # # # fig.add_trace(go.Bar(
# # # # # # #     x=df["Date"],
# # # # # # #     y=df["Count"],
# # # # # # #     text=df["Count"],
# # # # # # #     textposition='outside',
# # # # # # #     marker=dict(
# # # # # # #         color='rgba(255,0,0,0.6)',
# # # # # # #         line=dict(color='rgba(255,0,0,1.0)', width=1.5)
# # # # # # #     ),
# # # # # # #     name='Call Count'
# # # # # # # ))

# # # # # # # # Line chart on top
# # # # # # # fig.add_trace(go.Scatter(
# # # # # # #     x=df["Date"],
# # # # # # #     y=df["Count"],
# # # # # # #     mode='lines+markers',
# # # # # # #     name='Trend',
# # # # # # #     line=dict(
# # # # # # #         color='red',
# # # # # # #         width=3,
# # # # # # #         shape='spline'  # For smooth curves
# # # # # # #     ),
# # # # # # #     marker=dict(
# # # # # # #         size=6,
# # # # # # #         color='rgba(255,50,50,1)'
# # # # # # #     )
# # # # # # # ))

# # # # # # # # Layout tweaks for a clean design
# # # # # # # fig.update_layout(
# # # # # # #     title="Daily Call Counts",
# # # # # # #     xaxis_title="Date",
# # # # # # #     yaxis_title="Number of Calls",
# # # # # # #     template="plotly_white",
# # # # # # #     height=500,
# # # # # # #     plot_bgcolor='rgba(0,0,0,0)',
# # # # # # #     paper_bgcolor='rgba(0,0,0,0)',
# # # # # # #     font=dict(size=14),
# # # # # # #     margin=dict(t=60, l=20, r=20, b=40)
# # # # # # # )

# # # # # # # # Display the graph in Streamlit
# # # # # # # st.plotly_chart(fig, use_container_width=True)

# # # # # # # # Optionally, display raw data below the chart
# # # # # # # st.write("### Raw Data", df)


# # # # # # import streamlit as st
# # # # # # import plotly.graph_objects as go
# # # # # # import pandas as pd
# # # # # # from datetime import datetime, timedelta
# # # # # # import random
# # # # # # import requests

# # # # # # # Constants
# # # # # # API_BASE_URL = "http://localhost:8000/api/v1/outbound-calls?start_date=2025-04-01&end_date=2025-04-05"  # Replace with your API URL
# # # # # # API_ENDPOINTS = {
# # # # # #     "CALLS": "/calls"  # Replace with the correct API endpoint
# # # # # # }

# # # # # # # Fetch call data (Replace this with actual API call)
# # # # # # def fetch_call_data(call_type, start_date, end_date):
# # # # # #     # Construct the full API URL with parameters
# # # # # #     url = f"{API_BASE_URL}{API_ENDPOINTS['CALLS']}"
# # # # # #     params = {
# # # # # #         "call_type": call_type,
# # # # # #         "start_date": start_date,
# # # # # #         "end_date": end_date
# # # # # #     }
    
# # # # # #     # Fetch the data (Here we use random data for the example)
# # # # # #     response = requests.get(url, params=params)
    
# # # # # #     # Simulating API response (for demonstration)
# # # # # #     if response.status_code == 200:
# # # # # #         data = response.json()  # Assuming the API returns a JSON response
# # # # # #         return data
# # # # # #     else:
# # # # # #         return []

# # # # # # # Streamlit UI: Get the start and end dates from the user
# # # # # # st.title("Call Data Dashboard")

# # # # # # start_date = st.date_input("Select Start Date", datetime.now() - timedelta(days=10))
# # # # # # end_date = st.date_input("Select End Date", datetime.now())

# # # # # # # Ensure that start_date is not later than end_date
# # # # # # if start_date > end_date:
# # # # # #     st.error("Start date cannot be later than end date")
# # # # # # else:
# # # # # #     # Fetch the call data from the API
# # # # # #     call_type = "all"  # Example: 'all', 'outgoing', etc.
# # # # # #     call_data = fetch_call_data(call_type, start_date, end_date)

# # # # # #     # If data is fetched successfully, proceed
# # # # # #     if call_data:
# # # # # #         # Convert to DataFrame
# # # # # #         df = pd.DataFrame(call_data)
# # # # # #         if df.empty:
# # # # # #             st.warning("No call data found for the selected date range.")
# # # # # #         else:
# # # # # #             # Calculate the total number of calls
# # # # # #             total_calls = df['Count'].sum()
# # # # # #             st.write(f"### Total Calls from {start_date} to {end_date}: {total_calls}")

# # # # # #             # Create a Plotly bar + line chart
# # # # # #             fig = go.Figure()

# # # # # #             # Bar chart
# # # # # #             fig.add_trace(go.Bar(
# # # # # #                 x=df["Date"],
# # # # # #                 y=df["Count"],
# # # # # #                 text=df["Count"],
# # # # # #                 textposition='outside',
# # # # # #                 marker=dict(
# # # # # #                     color='rgba(255,0,0,0.6)',
# # # # # #                     line=dict(color='rgba(255,0,0,1.0)', width=1.5)
# # # # # #                 ),
# # # # # #                 name='Call Count'
# # # # # #             ))

# # # # # #             # Line chart on top
# # # # # #             fig.add_trace(go.Scatter(
# # # # # #                 x=df["Date"],
# # # # # #                 y=df["Count"],
# # # # # #                 mode='lines+markers',
# # # # # #                 name='Trend',
# # # # # #                 line=dict(
# # # # # #                     color='red',
# # # # # #                     width=3,
# # # # # #                     shape='spline'  # For smooth curves
# # # # # #                 ),
# # # # # #                 marker=dict(
# # # # # #                     size=6,
# # # # # #                     color='rgba(255,50,50,1)'
# # # # # #                 )
# # # # # #             ))

# # # # # #             # Layout tweaks for a clean design
# # # # # #             fig.update_layout(
# # # # # #                 title="Daily Call Counts",
# # # # # #                 xaxis_title="Date",
# # # # # #                 yaxis_title="Number of Calls",
# # # # # #                 template="plotly_white",
# # # # # #                 height=500,
# # # # # #                 plot_bgcolor='rgba(0,0,0,0)',
# # # # # #                 paper_bgcolor='rgba(0,0,0,0)',
# # # # # #                 font=dict(size=14),
# # # # # #                 margin=dict(t=60, l=20, r=20, b=40)
# # # # # #             )

# # # # # #             # Display the graph in Streamlit
# # # # # #             st.plotly_chart(fig, use_container_width=True)

# # # # # #             # Display the raw data below the graph
# # # # # #             st.write("### Raw Data", df)
# # # # # #     else:
# # # # # #         st.error("Failed to fetch call data. Please try again later.")
# # # # # import streamlit as st
# # # # # import pandas as pd
# # # # # import requests
# # # # # import datetime
# # # # # import matplotlib.pyplot as plt

# # # # # # Set up the Streamlit page configuration
# # # # # st.set_page_config(page_title="Outbound Calls Dashboard", layout="wide")

# # # # # # Set up the title of the page
# # # # # st.title("📞 Outbound Calls Dashboard")

# # # # # # Select the date range for the filter
# # # # # col1, col2 = st.columns(2)
# # # # # with col1:
# # # # #     start_date = st.date_input("Start Date", value=datetime.date(2025, 4, 1))
# # # # # with col2:
# # # # #     end_date = st.date_input("End Date", value=datetime.date(2025, 4, 5))

# # # # # # Check if start date is after the end date
# # # # # if start_date > end_date:
# # # # #     st.warning("Start date must be before the end date.")
# # # # # else:
# # # # #     # If the user clicks the "Fetch Data" button
# # # # #     if st.button("📥 Fetch Data"):
# # # # #         with st.spinner("Fetching data..."):
# # # # #             # Format the start and end dates for the API request
# # # # #             start_str = start_date.strftime("%Y-%m-%d")
# # # # #             end_str = end_date.strftime("%Y-%m-%d")
# # # # #             url = f"http://127.0.0.1:8000/api/v1/outbound-calls?start_date={start_str}&end_date={end_str}"

# # # # #             try:
# # # # #                 # Make the API request to fetch the call data
# # # # #                 response = requests.get(url)
# # # # #                 response.raise_for_status()
# # # # #                 data = response.json()
# # # # #                 calls = data.get("calls", [])

# # # # #                 # If there are no calls in the response
# # # # #                 if not calls:
# # # # #                     st.info("No calls found for the selected date range.")
# # # # #                 else:
# # # # #                     # Convert the call data into a DataFrame
# # # # #                     df = pd.DataFrame(calls)
# # # # #                     df["time"] = pd.to_datetime(df["time"])

# # # # #                     # Display total count of outbound calls
# # # # #                     st.metric("📊 Total Outbound Calls", len(df))

# # # # #                     # Prepare the data for plotting: group by date
# # # # #                     df["date"] = df["time"].dt.date
# # # # #                     calls_per_day = df.groupby("date").size()

# # # # #                     # Plotting the bar graph for number of calls per day
# # # # #                     st.subheader("📈 Number of Calls per Day")
# # # # #                     fig, ax = plt.subplots(figsize=(10, 6))
# # # # #                     calls_per_day.plot(kind="bar", ax=ax, color="#4f8bf9")

# # # # #                     # Add count on top of the bars
# # # # #                     for i, v in enumerate(calls_per_day):
# # # # #                         ax.text(i, v + 0.1, str(v), ha="center", va="bottom", color="black")

# # # # #                     ax.set_xlabel("Date")
# # # # #                     ax.set_ylabel("Number of Calls")
# # # # #                     ax.set_title("Calls vs Dates")
# # # # #                     st.pyplot(fig)

# # # # #                     # Show the full call details table
# # # # #                     st.subheader("📋 Call Details Table")
# # # # #                     st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)

# # # # #             except requests.exceptions.RequestException as e:
# # # # #                 st.error(f"Error fetching data: {e}")


# # # # import streamlit as st
# # # # import pandas as pd
# # # # import requests
# # # # import datetime
# # # # import matplotlib.pyplot as plt

# # # # # Set up the Streamlit page configuration
# # # # st.set_page_config(page_title="Outbound Calls Dashboard", layout="wide")

# # # # # Set up the title of the page
# # # # st.title("📞 Outbound Calls Dashboard")

# # # # # Select the date range for the filter
# # # # col1, col2 = st.columns(2)
# # # # with col1:
# # # #     start_date = st.date_input("Start Date", value=datetime.date(2025, 4, 1))
# # # # with col2:
# # # #     end_date = st.date_input("End Date", value=datetime.date(2025, 4, 5))

# # # # # Check if start date is after the end date
# # # # if start_date > end_date:
# # # #     st.warning("Start date must be before the end date.")
# # # # else:
# # # #     # If the user clicks the "Fetch Data" button
# # # #     if st.button("📥 Fetch Data"):
# # # #         with st.spinner("Fetching data..."):
# # # #             # Format the start and end dates for the API request
# # # #             start_str = start_date.strftime("%Y-%m-%d")
# # # #             end_str = end_date.strftime("%Y-%m-%d")
# # # #             url = f"http://127.0.0.1:8000/api/v1/outbound-calls?start_date={start_str}&end_date={end_str}"

# # # #             try:
# # # #                 # Make the API request to fetch the call data
# # # #                 response = requests.get(url)
# # # #                 response.raise_for_status()
# # # #                 data = response.json()
# # # #                 calls = data.get("calls", [])

# # # #                 # If there are no calls in the response
# # # #                 if not calls:
# # # #                     st.info("No calls found for the selected date range.")
# # # #                 else:
# # # #                     # Convert the call data into a DataFrame
# # # #                     df = pd.DataFrame(calls)
# # # #                     df["time"] = pd.to_datetime(df["time"])

# # # #                     # Display total count of outbound calls
# # # #                     st.metric("📊 Total Outbound Calls", len(df))

# # # #                     # Prepare the data for plotting: group by date
# # # #                     df["date"] = df["time"].dt.date
# # # #                     calls_per_day = df.groupby("date").size()

# # # #                     # Plotting the bar graph for number of calls per day
# # # #                     st.subheader("📈 Number of Calls per Day")
# # # #                     fig, ax = plt.subplots(figsize=(10, 6))
# # # #                     calls_per_day.plot(kind="bar", ax=ax, color="#4f8bf9")

# # # #                     # Add count on top of the bars
# # # #                     for i, v in enumerate(calls_per_day):
# # # #                         ax.text(i, v + 0.1, str(v), ha="center", va="bottom", color="black")

# # # #                     ax.set_xlabel("Date")
# # # #                     ax.set_ylabel("Number of Calls")
# # # #                     ax.set_title("Calls vs Dates")
# # # #                     st.pyplot(fig)

# # # #                     # Line graph showing the trend of calls per day
# # # #                     st.subheader("📉 Calls Trend per Day (Line Graph)")
# # # #                     fig, ax = plt.subplots(figsize=(10, 6))
# # # #                     calls_per_day.plot(kind="line", ax=ax, marker="o", color="#FF6347", linewidth=2)

# # # #                     ax.set_xlabel("Date")
# # # #                     ax.set_ylabel("Number of Calls")
# # # #                     ax.set_title("Calls Trend per Day")
# # # #                     st.pyplot(fig)

# # # #                     # Show the full call details table
# # # #                     st.subheader("📋 Call Details Table")
# # # #                     st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)

# # # #             except requests.exceptions.RequestException as e:
# # # #                 st.error(f"Error fetching data: {e}")

# # # import streamlit as st
# # # import pandas as pd
# # # import requests
# # # import datetime
# # # import matplotlib.pyplot as plt
# # # from matplotlib.ticker import MaxNLocator

# # # # Set up the Streamlit page configuration
# # # st.set_page_config(page_title="Outbound Calls Dashboard", layout="wide")

# # # # Set up the title of the page
# # # st.title("📞 Outbound Calls Dashboard")

# # # # Select the date range for the filter
# # # col1, col2 = st.columns(2)
# # # with col1:
# # #     start_date = st.date_input("Start Date", value=datetime.date(2025, 4, 1))
# # # with col2:
# # #     end_date = st.date_input("End Date", value=datetime.date(2025, 4, 5))

# # # # Check if start date is after the end date
# # # if start_date > end_date:
# # #     st.warning("Start date must be before the end date.")
# # # else:
# # #     # If the user clicks the "Fetch Data" button
# # #     if st.button("📥 Fetch Data"):
# # #         with st.spinner("Fetching data..."):
# # #             # Format the start and end dates for the API request
# # #             start_str = start_date.strftime("%Y-%m-%d")
# # #             end_str = end_date.strftime("%Y-%m-%d")
# # #             url = f"http://127.0.0.1:8000/api/v1/outbound-calls?start_date={start_str}&end_date={end_str}"

# # #             try:
# # #                 # Make the API request to fetch the call data
# # #                 response = requests.get(url)
# # #                 response.raise_for_status()
# # #                 data = response.json()
# # #                 calls = data.get("calls", [])

# # #                 # If there are no calls in the response
# # #                 if not calls:
# # #                     st.info("No calls found for the selected date range.")
# # #                 else:
# # #                     # Convert the call data into a DataFrame
# # #                     df = pd.DataFrame(calls)
# # #                     df["time"] = pd.to_datetime(df["time"])

# # #                     # Display total count of outbound calls
# # #                     st.metric("📊 Total Outbound Calls", len(df))

# # #                     # Prepare the data for plotting: group by date
# # #                     df["date"] = df["time"].dt.date
# # #                     calls_per_day = df.groupby("date").size()

# # #                     # Plotting the bar graph for number of calls per day
# # #                     st.subheader("📈 Number of Calls per Day")
# # #                     with st.beta_expander("Click to Expand Bar Graph"):
# # #                         fig, ax = plt.subplots(figsize=(10, 6))
# # #                         bars = calls_per_day.plot(kind="bar", ax=ax, color=['#FF6347', '#FF7F50', '#FF4500', '#FF6347', '#FF4500'])

# # #                         # Add count on top of the bars
# # #                         for i, v in enumerate(calls_per_day):
# # #                             ax.text(i, v + 0.1, str(v), ha="center", va="bottom", color="black")

# # #                         ax.set_xlabel("Date")
# # #                         ax.set_ylabel("Number of Calls")
# # #                         ax.set_title("Calls vs Dates")
                        
# # #                         # Rotate the x-axis labels to avoid overlap
# # #                         plt.xticks(rotation=45, ha='right')

# # #                         # Make the graph more compact by adjusting the tick frequency
# # #                         ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='both'))
                        
# # #                         # Add border around the graph area
# # #                         plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
# # #                         st.pyplot(fig)

# # #                     # Line graph showing the trend of calls per day
# # #                     st.subheader("📉 Calls Trend per Day (Line Graph)")
# # #                     with st.beta_expander("Click to Expand Line Graph"):
# # #                         fig, ax = plt.subplots(figsize=(10, 6))
# # #                         calls_per_day.plot(kind="line", ax=ax, marker="o", color="red", linewidth=2, markerfacecolor='yellow')

# # #                         ax.set_xlabel("Date")
# # #                         ax.set_ylabel("Number of Calls")
# # #                         ax.set_title("Calls Trend per Day")

# # #                         # Rotate x-axis labels
# # #                         plt.xticks(rotation=45, ha='right')

# # #                         # Add border around the graph area
# # #                         plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)

# # #                         st.pyplot(fig)

# # #                     # Show the full call details table
# # #                     st.subheader("📋 Call Details Table")
# # #                     st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)

# # #             except requests.exceptions.RequestException as e:
# # #                 st.error(f"Error fetching data: {e}")

# # import streamlit as st
# # import pandas as pd
# # import requests
# # import datetime
# # import matplotlib.pyplot as plt
# # from matplotlib.ticker import MaxNLocator

# # # Page settings
# # st.set_page_config(page_title="Outbound Calls Dashboard", layout="wide")
# # st.title("📞 Outbound Calls Dashboard")

# # # Date selectors
# # col1, col2 = st.columns(2)
# # with col1:
# #     start_date = st.date_input("Start Date", value=datetime.date(2025, 4, 1))
# # with col2:
# #     end_date = st.date_input("End Date", value=datetime.date(2025, 4, 5))

# # # Validate dates
# # if start_date > end_date:
# #     st.warning("Start date must be before the end date.")
# # else:
# #     if st.button("📥 Fetch Data"):
# #         with st.spinner("Fetching data..."):
# #             start_str = start_date.strftime("%Y-%m-%d")
# #             end_str = end_date.strftime("%Y-%m-%d")
# #             url = f"http://127.0.0.1:8000/api/v1/outbound-calls?start_date={start_str}&end_date={end_str}"

# #             try:
# #                 response = requests.get(url)
# #                 response.raise_for_status()
# #                 data = response.json()
# #                 calls = data.get("calls", [])

# #                 if not calls:
# #                     st.info("No calls found for the selected date range.")
# #                 else:
# #                     df = pd.DataFrame(calls)
# #                     df["time"] = pd.to_datetime(df["time"])
# #                     df["date"] = df["time"].dt.date

# #                     # Total calls metric
# #                     st.metric("📊 Total Outbound Calls", len(df))

# #                     # Calls per day
# #                     calls_per_day = df.groupby("date").size()

# #                     # Bar Graph
# #                     st.subheader("📈 Number of Calls per Day")
# #                     with st.expander("Click to Expand Bar Graph"):
# #                         fig, ax = plt.subplots(figsize=(9, 5))
# #                         colors = plt.cm.Reds(range(100, 100 + len(calls_per_day)*10, 10))
# #                         bars = ax.bar(calls_per_day.index.astype(str), calls_per_day.values, color=colors)

# #                         for bar in bars:
# #                             height = bar.get_height()
# #                             ax.annotate(f'{int(height)}',
# #                                         xy=(bar.get_x() + bar.get_width() / 2, height),
# #                                         xytext=(0, 3),
# #                                         textcoords="offset points",
# #                                         ha='center', va='bottom')

# #                         ax.set_xlabel("Date")
# #                         ax.set_ylabel("Number of Calls")
# #                         ax.set_title("Calls vs Dates")
# #                         ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# #                         plt.xticks(rotation=45, ha='right')
# #                         st.pyplot(fig)

# #                     # Table
# #                     st.subheader("📋 Call Details Table")
# #                     st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)

# #                     # Line Graph
# #                     st.subheader("📉 Calls Trend per Day (Line Graph)")
# #                     with st.expander("Click to Expand Line Graph"):
# #                         fig2, ax2 = plt.subplots(figsize=(9, 5))
# #                         ax2.plot(calls_per_day.index.astype(str), calls_per_day.values, marker="o", color="red", linewidth=2, markerfacecolor='yellow')
# #                         ax2.set_xlabel("Date")
# #                         ax2.set_ylabel("Number of Calls")
# #                         ax2.set_title("Calls Trend per Day")
# #                         plt.xticks(rotation=45, ha='right')
# #                         st.pyplot(fig2)

# #             except requests.exceptions.RequestException as e:
# #                 st.error(f"Error fetching data: {e}")

# import streamlit as st
# import pandas as pd
# import requests
# import datetime
# import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator

# # Page settings
# st.set_page_config(page_title="Call Analytics Dashboard", layout="wide")
# st.title("📞 Call Analytics Dashboard")

# # Date selectors
# col1, col2 = st.columns(2)
# with col1:
#     start_date = st.date_input("Start Date", value=datetime.date(2025, 4, 1))
# with col2:
#     end_date = st.date_input("End Date", value=datetime.date(2025, 4, 5))

# # Validate date range
# if start_date > end_date:
#     st.warning("Start date must be before the end date.")
# else:
#     if st.button("📥 Fetch Data"):
#         with st.spinner("Fetching outbound calls data..."):
#             start_str = start_date.strftime("%Y-%m-%d")
#             end_str = end_date.strftime("%Y-%m-%d")
#             outbound_url = f"http://127.0.0.1:8000/api/v1/outbound-calls?start_date={start_str}&end_date={end_str}"
#             connected_url = f"http://127.0.0.1:8000/api/v1/connected-calls?start_date={start_str}&end_date={end_str}"

#             def fetch_and_display_calls(api_url, section_title, color_map):
#                 try:
#                     response = requests.get(api_url)
#                     response.raise_for_status()
#                     data = response.json()
#                     calls = data.get("calls", [])

#                     if not calls:
#                         st.info(f"No {section_title.lower()} found for the selected date range.")
#                         return

#                     df = pd.DataFrame(calls)
#                     df["time"] = pd.to_datetime(df["time"])
#                     df["date"] = df["time"].dt.date

#                     st.metric(f"📊 Total {section_title}", len(df))

#                     # Grouped data
#                     calls_per_day = df.groupby("date").size()

#                     # Bar Chart
#                     st.subheader(f"📈 Number of {section_title} per Day")
#                     with st.expander("Click to Expand Bar Graph"):
#                         fig, ax = plt.subplots(figsize=(9, 5))
#                         colors = plt.cm.get_cmap(color_map)(range(100, 100 + len(calls_per_day)*10, 10))
#                         bars = ax.bar(calls_per_day.index.astype(str), calls_per_day.values, color=colors)

#                         for bar in bars:
#                             height = bar.get_height()
#                             ax.annotate(f'{int(height)}',
#                                         xy=(bar.get_x() + bar.get_width() / 2, height),
#                                         xytext=(0, 3),
#                                         textcoords="offset points",
#                                         ha='center', va='bottom')

#                         ax.set_xlabel("Date")
#                         ax.set_ylabel("Number of Calls")
#                         ax.set_title(f"{section_title} vs Dates")
#                         ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#                         plt.xticks(rotation=45, ha='right')
#                         st.pyplot(fig)

#                     # Table
#                     st.subheader(f"📋 {section_title} Details Table")
#                     st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)

#                     # Line Graph
#                     st.subheader(f"📉 {section_title} Trend per Day (Line Graph)")
#                     with st.expander("Click to Expand Line Graph"):
#                         fig2, ax2 = plt.subplots(figsize=(9, 5))
#                         ax2.plot(calls_per_day.index.astype(str), calls_per_day.values, marker="o", linewidth=2, color="orange", markerfacecolor="yellow")
#                         ax2.set_xlabel("Date")
#                         ax2.set_ylabel("Number of Calls")
#                         ax2.set_title(f"{section_title} Trend")
#                         plt.xticks(rotation=45, ha='right')
#                         st.pyplot(fig2)

#                 except requests.exceptions.RequestException as e:
#                     st.error(f"Error fetching {section_title.lower()} data: {e}")

#         # Show outbound section
#         st.header("📤 Outbound Calls")
#         fetch_and_display_calls(outbound_url, "Outbound Calls", "Reds")

#         # Show connected section
#         st.header("✅ Connected Calls")
#         with st.spinner("Fetching connected calls data..."):
#             fetch_and_display_calls(connected_url, "Connected Calls", "Blues")

import streamlit as st
import pandas as pd
import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Page configuration
st.set_page_config(page_title="Call Analytics Dashboard", layout="wide")
st.title("📞 Call Analytics Dashboard")

# Date selection
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", value=datetime.date(2025, 4, 1))
with col2:
    end_date = st.date_input("End Date", value=datetime.date(2025, 4, 15))

# Validate date range
if start_date > end_date:
    st.warning("Start date must be before the end date.")
else:
    if st.button("📥 Fetch Data"):
        with st.spinner("Fetching call data..."):
            start_str = start_date.strftime("%Y-%m-%d")
            end_str = end_date.strftime("%Y-%m-%d")
            endpoints = [
                {
                    "url": f"http://127.0.0.1:8000/api/v1/outbound-calls?start_date={start_str}&end_date={end_str}",
                    "title": "Outbound Calls",
                    "color": "Reds"
                },
                {
                    "url": f"http://127.0.0.1:8000/api/v1/connected-calls?start_date={start_str}&end_date={end_str}",
                    "title": "Connected Calls",
                    "color": "Blues"
                },
                {
                    "url": f"http://127.0.0.1:8000/api/v1/connected-outbound-calls?start_date={start_str}&end_date={end_str}",
                    "title": "Outbound-Connected Calls",
                    "color": "Greens"
                }
            ]

            def fetch_and_display_calls(api_url, section_title, color_map):
                try:
                    response = requests.get(api_url)
                    response.raise_for_status()
                    data = response.json()
                    calls = data.get("calls", [])

                    if not calls:
                        st.info(f"No {section_title.lower()} found for the selected date range.")
                        return

                    df = pd.DataFrame(calls)
                    df["time"] = pd.to_datetime(df["time"])
                    df["date"] = df["time"].dt.date

                    st.metric(f"📊 Total {section_title}", len(df))

                    # Group data
                    calls_per_day = df.groupby("date").size()

                    # Bar Graph
                    st.subheader(f"📈 {section_title} per Day")
                    with st.expander("Click to Expand Bar Graph"):
                        fig, ax = plt.subplots(figsize=(9, 5))
                        colors = plt.cm.get_cmap(color_map)(range(100, 100 + len(calls_per_day)*10, 10))
                        bars = ax.bar(calls_per_day.index.astype(str), calls_per_day.values, color=colors, edgecolor='black')

                        for bar in bars:
                            height = bar.get_height()
                            ax.annotate(f'{int(height)}',
                                        xy=(bar.get_x() + bar.get_width() / 2, height),
                                        xytext=(0, 3),
                                        textcoords="offset points",
                                        ha='center', va='bottom')

                        ax.set_xlabel("Date")
                        ax.set_ylabel("Number of Calls")
                        ax.set_title(f"{section_title} vs Dates")
                        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
                        plt.xticks(rotation=45, ha='right')
                        st.pyplot(fig)

                    # Table
                    st.subheader(f"📋 {section_title} Table")
                    st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)

                    # Line Chart
                    st.subheader(f"📉 {section_title} Trend")
                    with st.expander("Click to Expand Line Graph"):
                        fig2, ax2 = plt.subplots(figsize=(9, 5))
                        ax2.plot(calls_per_day.index.astype(str), calls_per_day.values, marker="o", linewidth=2,
                                 color="orange", markerfacecolor="yellow")
                        ax2.set_xlabel("Date")
                        ax2.set_ylabel("Number of Calls")
                        ax2.set_title(f"{section_title} Trend")
                        plt.xticks(rotation=45, ha='right')
                        st.pyplot(fig2)

                except requests.exceptions.RequestException as e:
                    st.error(f"Error fetching {section_title.lower()} data: {e}")

            # Loop through all APIs and display each section
            for api in endpoints:
                st.header(f"📂 {api['title']}")
                fetch_and_display_calls(api["url"], api["title"], api["color"])
