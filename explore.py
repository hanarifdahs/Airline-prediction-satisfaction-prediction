import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


DATA_URL = (
    'https://raw.githubusercontent.com/hanarifdahs/datasets/master/train.csv'
)


@st.cache
def load_data():
    df = pd.read_csv(DATA_URL)
    df.drop(['Unnamed: 0', 'id', 'Age', 'Gender', 'Gate location',
            'Arrival Delay in Minutes'], inplace=True, axis=1)
    return df


df = load_data()


def general_satisfied():
    fig, axs = plt.subplots(ncols=2, figsize=(10, 4))

    # First Graph
    bar = df['satisfaction'].value_counts().plot(kind='bar', ax=axs[0])

    # Show count value above bar
    for p in bar.patches:
        bar.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width()/2., p.get_height()),
                     ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    # Second Graph
    df['satisfaction'].value_counts().plot.pie(
        autopct='%1.1f%%', startangle=90, ax=axs[1])

    # Define seaborn/matplotlib di streamlit
    st.pyplot(fig)


def mean_services():
    data = {
        'Services': ['Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking', 'Food and drink', 'Online boarding', 'Seat comfort', 'Inflight entertainment', 'On-board service', 'Leg room service', 'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness'],
        'Rate': [df['Inflight wifi service'].mean(), df["Departure/Arrival time convenient"].mean(), df['Ease of Online booking'].mean(), df['Food and drink'].mean(), df['Online boarding'].mean(), df['Seat comfort'].mean(), df['Inflight entertainment'].mean(), df['On-board service'].mean(), df['Leg room service'].mean(), df['Baggage handling'].mean(), df['Checkin service'].mean(), df['Inflight service'].mean(), df['Cleanliness'].mean()]
    }
    fig = px.bar(data, x='Rate', y='Services', orientation='h')

    # Define plotly express di streamlit
    st.plotly_chart(fig)


def show_explore_page():
    st.header('✈️ Airplane Passenger Data Exploration ✈️')

    st.markdown('---')

    # Chart 1
    # general_satisfied()
    st.subheader("How many passengers are satisfied with the services?")
    general_satisfied()

    # Chart 2
    st.subheader("Which Service has the highest and lowest rate?")
    mean_services()
