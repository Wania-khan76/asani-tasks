import streamlit as st
from components.header import setup_header
from components.date_selector import date_selector
from components.call_type import call_type_selector
from components.data_fetcher import fetch_call_data
from components.data_display import display_call_metrics, display_call_data
from components.charts import display_call_charts

def main():
    # Setup UI configuration and header
    setup_header()
    
    # Get date range from user
    start_date, end_date = date_selector()
    
    # Get call type selection
    call_type = call_type_selector()
    
    # Only show fetch button when valid selections are made
    if call_type != "None" and start_date and end_date:
        if st.sidebar.button("🚀 Fetch Calls", help="Click to fetch call data"):
            data, count = fetch_call_data(call_type, start_date, end_date)
            
            if not data.empty:
                # Display metrics
                display_call_metrics(count, call_type)
                
                # Display charts
                display_call_charts(data, call_type)
                
                # Display detailed data
                display_call_data(data, call_type)
    else:
        st.info("Please select a call type and valid date range to fetch data")

if __name__ == "__main__":
    main()