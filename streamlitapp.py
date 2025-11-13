import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_resource
def mySql():
    # Initialize connection.
    conn = st.connection('mysql', type='sql')
    # Perform query.
    df = conn.query('SELECT viikko, nimi, toistot, paino from kyykky LIMIT 100;', ttl=600)
    return df
    # Streamlit
def main():
    st.title("Plot data from MySql")
    st.write("kyykky kehitys viikkojen mukaan")
    data = mySql()
    #plot data
    if not data.empty:
        fig = px.line(data, x="viikko", y="paino", color="nimi",
                      title='Kyykky kehitys viikkojen mukaan', markers=True)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Ei dataa näytettäväksi")
if __name__ == "__main__":
    main()