from sqlalchemy import Column, Integer, String
 
from .base import Base

 

class HR_table(Base):
    __tablename__ = 'employee'

 
    rowid = Column("rowid", Integer, primary_key=True, autoincrement=True)

    employeenumber = Column("employeenumber", Integer)
    age = Column("age", Integer)
    attrition = Column("attrition", String(10))
    businesstravel = Column("businesstravel", String(50))
    dailyrate = Column("dailyrate", Integer)
    department = Column("department", String(50))
    distancefromhome = Column("distancefromhome", Integer)
    education = Column("education", String(50))
    educationfield = Column("educationfield", String(50))
    employeecount = Column("employeecount", Integer)
    environmentsatisfaction = Column("environmentsatisfaction", Integer)
    gender = Column("gender", String(10))
    hourlyrate = Column("hourlyrate", Integer)
    jobinvolvement = Column("jobinvolvement", Integer)
    joblevel = Column("joblevel", Integer)
    jobrole = Column("jobrole", String(50))
    jobsatisfaction = Column("jobsatisfaction", Integer)
    maritalstatus = Column("maritalstatus", String(20))
    monthlyincome = Column("monthlyincome", Integer)
    monthlyrate = Column("monthlyrate", Integer)
    numcompaniesworked = Column("numcompaniesworked", Integer)
    over18 = Column("over18", String(5))
    overtime = Column("overtime", String(5))
    percentsalaryhike = Column("percentsalaryhike", Integer)
    performancerating = Column("performancerating", Integer)
    relationshipsatisfaction = Column("relationshipsatisfaction", Integer)
    standardhours = Column("standardhours", Integer)
    stockoptionlevel = Column("stockoptionlevel", Integer)
    totalworkingyears = Column("totalworkingyears", Integer)
    trainingtimeslastyear = Column("trainingtimeslastyear", Integer)
    worklifebalance = Column("worklifebalance", Integer)
    yearsatcompany = Column("yearsatcompany", Integer)
    yearsincurrentrole = Column("yearsincurrentrole", Integer)
    yearssincelastpromotion = Column("yearssincelastpromotion", Integer)
    yearswithcurrmanager = Column("yearswithcurrmanager", Integer)
    
 