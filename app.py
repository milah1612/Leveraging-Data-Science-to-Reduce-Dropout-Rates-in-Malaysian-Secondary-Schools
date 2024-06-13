import streamlit as st
import pandas as pd
import numpy as np

# Load the mock data
data = pd.read_csv('mock_student_data.csv')

# Title of the Dashboard
st.title('Early Intervention Dashboard')

# Student Risk Analysis
st.header('Student Risk Analysis')
risk_fig = px.scatter(data, x='AcademicPerformance', y='Attendance', color='RiskLevel', title='Student Risk Analysis')
st.plotly_chart(risk_fig)

# Predictive Alerts
st.header('Predictive Alerts')
high_risk_students = data[data['RiskLevel'] == 'High']
st.write(high_risk_students)

# Intervention Tracker
st.header('Intervention Tracker')
intervention_fig = px.pie(data, names='InterventionStatus', title='Intervention Tracker')
st.plotly_chart(intervention_fig)

# School Environment Metrics
st.header('School Environment Metrics')
school_metrics_fig = px.scatter(data, x='SchoolInfrastructureScore', y='TeacherStudentRatio', title='School Environment Metrics')
st.plotly_chart(school_metrics_fig)
