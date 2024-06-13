import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the mock data
data = pd.read_csv('mock_student_data.csv')

# Title of the Dashboard
st.title('Early Intervention Dashboard')

# Layout with columns
col1, col2 = st.columns(2)

# Student Risk Analysis
with col1:
    st.header('Student Risk Analysis')
    risk_fig = px.scatter(data, x='AcademicPerformance', y='Attendance', color='RiskLevel', title='Student Risk Analysis')
    st.plotly_chart(risk_fig)

# Predictive Alerts
with col1:
    st.header('Predictive Alerts')
    high_risk_students = data[data['RiskLevel'] == 'High']
    st.write(high_risk_students)

# Intervention Tracker
with col2:
    st.header('Intervention Tracker')
    intervention_fig = px.pie(data, names='InterventionStatus', title='Intervention Tracker')
    st.plotly_chart(intervention_fig)

# School Environment Metrics
with col2:
    st.header('School Environment Metrics')
    school_metrics_fig = px.scatter(data, x='SchoolInfrastructureScore', y='TeacherStudentRatio', title='School Environment Metrics')
    st.plotly_chart(school_metrics_fig)

# Provide a download button for the mock data
st.download_button(
    label="Download data as CSV",
    data=data.to_csv(index=False),
    file_name='mock_student_data.csv',
    mime='text/csv',
)
