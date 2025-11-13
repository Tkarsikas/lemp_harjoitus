import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_resource
def mySql():
    # Initialize connection.
    conn = st.connection('mysql', type='sql')
    # Perform query.
    df = conn.query('SELECT viikko, nimi, toistot from treenit LIMIT 100;', ttl=600)
    return df
    # Streamlit
def main():
    st.title("Plot data from MySql")
    st.write("progression of weight lifting over weeks")
    data = mySql()
    #plot data
    df2 = pd.DataFrame(data, columns=["viikko", "nimi", "toistot"])
    totalKg = px.line(df2, x=df2.index, y="toistot", title='Total weight lifted over weeks')
    st.plotly_chart(totalKg, use_container_width=True)
if __name__ == "__main__":
    main()