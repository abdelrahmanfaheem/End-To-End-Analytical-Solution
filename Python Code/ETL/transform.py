import pandas as pd
import numpy as np
from sqlalchemy import Boolean, NVARCHAR


def  change_column_type ():

    column_type = {
    'Attrition': NVARCHAR(length=50),
    'BusinessTravel': NVARCHAR(length=50),
    'Education': NVARCHAR(length=10),
    'EducationField': NVARCHAR(length=50),
    'Department': NVARCHAR(length=50),
    'OverTime': NVARCHAR(length=5),
    'Over18': NVARCHAR(length=5),
    }

    return column_type

def column_mapping ():
        
    COLUMN_MAPPING = {
        "EmployeeNumber": "employeenumber",
        "Age": "age",
        "Attrition": "attrition",
        "BusinessTravel": "businesstravel",
        "DailyRate": "dailyrate",
        "Department": "department",
        "DistanceFromHome": "distancefromhome",
        "Education": "education",
        "EducationField": "educationfield",
        "EmployeeCount": "employeecount",
        "EnvironmentSatisfaction": "environmentsatisfaction",
        "Gender": "gender",
        "HourlyRate": "hourlyrate",
        "JobInvolvement": "jobinvolvement",
        "JobLevel": "joblevel",
        "JobRole": "jobrole",
        "JobSatisfaction": "jobsatisfaction",
        "MaritalStatus": "maritalstatus",
        "MonthlyIncome": "monthlyincome",
        "MonthlyRate": "monthlyrate",
        "NumCompaniesWorked": "numcompaniesworked",
        "Over18": "over18",
        "OverTime": "overtime",
        "PercentSalaryHike": "percentsalaryhike",
        "PerformanceRating": "performancerating",
        "RelationshipSatisfaction": "relationshipsatisfaction",
        "StandardHours": "standardhours",
        "StockOptionLevel": "stockoptionlevel",
        "TotalWorkingYears": "totalworkingyears",
        "TrainingTimesLastYear": "trainingtimeslastyear",
        "WorkLifeBalance": "worklifebalance",
        "YearsAtCompany": "yearsatcompany",
        "YearsInCurrentRole": "yearsincurrentrole",
        "YearsSinceLastPromotion": "yearssincelastpromotion",
        "YearsWithCurrManager": "yearswithcurrmanager"
     }
    return COLUMN_MAPPING