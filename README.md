# End-to-End Analytical Solution: HR Analytics Project

This repository contains a complete **end-to-end HR analytics solution**, demonstrating modern Data Engineering, Backend Development, and Business Intelligence integration. The project covers everything from raw Excel data extraction to interactive Power BI dashboards.

---

## 📌 Project Roadmap

The project workflow is summarized in the roadmap below:

![Project Roadmap](Project%20Steps/1.png)

---

## 1️⃣ Python ETL Pipeline

We begin with raw HR Excel datasets and build a modular ETL pipeline:

- **Modular structure:** `extract.py`, `transform.py`, `load.py`  
- **SQLAlchemy ORM** schema modeling  
- **Structured exception handling** for reliable processing  
- **Integration with SQL Server** for automated data storage  

**Project Images:**

![Python Structure 1](Project%20Steps/2.png)  
![Python Structure 2](Project%20Steps/3.png)  

---

## 2️⃣ Backend – RESTful API (Spring Boot, MVC)

Built a RESTful API to provide reliable access to the HR data:

- **Controller → Service → Repository** layered architecture  
- **JPA entity mapping** aligned with SQL schema  
- **API documentation & testing** using Swagger  
- **Version control** using GitHub  

**Project Images:**

![Java Screen 1](Project%20Steps/4.png)  
![Java Screen 2](Project%20Steps/5.png)  
![Java Screen 3](Project%20Steps/6.png)  

---

## 3️⃣ Data Warehouse Design – Star Schema

Designed a **star schema** to optimize analytics in Power BI:

- Centralized **Fact_Employees** table  
- Supporting dimension tables: `Dim_Employee`, `Dim_Department`, `Dim_Job`, `Dim_Education`, `Dim_Attrition`, `Dim_Performance`  
- **Power Query** for data transformation  
- **API integration** to read processed data  

**Project Images:**

![Star Schema 1](Project%20Steps/7.png)  
![Star Schema 2](Project%20Steps/8.png)  

---

## 4️⃣ Power BI Dashboard & Business Intelligence

Developed an **interactive decision-support dashboard** with dynamic insights:

- **Field and Measure Parameters** for flexible analysis  
- Automated insights generated dynamically based on filters and slicers  
- **Advanced DAX measures** for comparisons and conditional logic  
- Dynamic text cards displaying contextual insights  

**Project Images:**

![Power BI Dashboard 1](Project%20Steps/9.png)  
![Power BI Dashboard 2](Project%20Steps/10.png)  
![Power BI Dashboard 3](Project%20Steps/11.png)  
![Power BI Dashboard 4](Project%20Steps/12.png)  
![Power BI Dashboard 5](Project%20Steps/13.png)  
![Power BI Dashboard 6](Project%20Steps/14.png)  
![Power BI Dashboard 7](Project%20Steps/15.png)  
![Power BI Dashboard 8](Project%20Steps/16.png)  
![Power BI Dashboard 9](Project%20Steps/17.png)  
![Power BI Dashboard 10](Project%20Steps/18.png)  

---

## ⚙️ Technologies Used

- **Python:** ETL, SQLAlchemy, pandas  
- **SQL Server:** Data storage & management  
- **Java (Spring Boot):** RESTful API, Swagger documentation  
- **Power BI:** Star schema modeling, interactive dashboards  
- **DAX:** Advanced calculations & dynamic insights  
- **GitHub:** Version control  

---

## 🔗 Project Structure
