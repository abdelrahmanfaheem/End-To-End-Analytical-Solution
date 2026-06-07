# 🚀 End-to-End HR Analytics Solution

A complete **Data Engineering, Backend Development, Data Warehousing, Data Security, and Business Intelligence** solution that transforms raw HR Excel files into interactive decision-support dashboards.

This project demonstrates the full analytics lifecycle, starting from raw HR datasets and ending with strategic and analytical Power BI dashboards designed to support HR decision-making.

---

# 📌 Project Overview

The solution follows a complete end-to-end analytics architecture:

```text
Raw Excel Files
       ↓
Python ETL Pipeline
       ↓
SQL Server Database
       ↓
Spring Boot REST API
       ↓
Manager-Level Data Security
       ↓
Data Warehouse (Star Schema)
       ↓
Power BI Semantic Model
       ↓
Interactive HR Dashboards
```

---

# 🗺️ Project Roadmap

![Project Roadmap](Project%20Steps/1.png)



---

# 🎨 Dashboard Design Phase (Figma)

Before implementation, dashboard layouts and user experience were designed in Figma to ensure a clear analytical storytelling experience and maintain consistency throughout the development process.

### View Figma Project

[HR Analytics Project - Figma Prototype](https://www.figma.com/design/6XIAX4SkRi7lKupYhQeu34/HR-Project?node-id=42-502&t=AuHNDv6JpaE9wwIw-1)

---

## 📊 Analytical Dashboard Design

### Background Design

![Analytical Background](Project%20Steps/Analytical%20Mockups%20Backgroud.png)

### Figma Mockup

![Analytical Figma](Project%20Steps/Figma%20Analytical%20Dashboard.png)

---

## 🎯 Strategic Dashboard Design

### Background Design

![Strategic Background](Project%20Steps/Stratgic%20Mockups%20Backgroud.png)

### Figma Mockup

![Strategic Figma](Project%20Steps/Figma%20Stratgic%20Dashboard.png)

---

# 🐍 Python ETL Pipeline

The project starts with raw HR Excel datasets and processes them through a modular ETL architecture.

## Key Features

- Modular ETL architecture
- Extract, Transform, and Load layers
- SQLAlchemy ORM integration
- Structured exception handling
- Automated SQL Server loading
- Reusable and maintainable code structure

## ETL Workflow

```text
Excel Files
    ↓
Extract Layer
    ↓
Transform Layer
    ↓
Validation Layer
    ↓
Load Layer
    ↓
SQL Server
```

## Project Screens

![Python Structure 1](Project%20Steps/2.png)

![Python Structure 2](Project%20Steps/3.png)

## Technologies Used

- Python
- Pandas
- SQLAlchemy
- SQL Server

---

# ☕ Backend Development (Spring Boot)

A RESTful API was developed to expose HR data and provide a reliable data source for analytics and reporting.

## Key Features

- MVC Architecture
- Controller → Service → Repository Pattern
- JPA Entity Mapping
- Swagger Documentation
- RESTful API Design
- Git-Based Version Control

## Backend Architecture

```text
Controller
    ↓
Service Layer
    ↓
Repository Layer
    ↓
SQL Server Database
```

## Project Screens

![Java Screen 1](Project%20Steps/4.png)

![Java Screen 2](Project%20Steps/5.png)

![Java Screen 3](Project%20Steps/6.png)

## Technologies Used

- Java
- Spring Boot
- Spring Data JPA
- Swagger/OpenAPI

---

# 🔐 Dynamic Data Security & Personalized Analytics

To support manager-level reporting and data privacy, the solution implements dynamic data filtering through the API layer.

Instead of loading all employee records into Power BI, the dashboard requests only the data relevant to a specific manager.

## Power Query Integration

A Power Query parameter is used to pass the manager name dynamically to the API endpoint:

```powerquery
Web.Contents(
    "http://localhost:9090/Data/DepartmentByManagerName/" & ManagerName
)
```

## How It Works

1. User specifies a manager name.
2. Power Query sends the manager name to the API.
3. Spring Boot receives the parameter.
4. SQL query filters records based on the manager.
5. Only authorized department data is returned.
6. Power BI loads manager-specific records.

This approach improves performance while providing a personalized and secure reporting experience.

## Query Implementation

![Selected Query Code](Project%20Steps/Selected%20Query%20Code.png)

## Benefits

- Manager-Level Data Access
- Personalized Dashboards
- Reduced Data Transfer
- Improved Refresh Performance
- API-Level Data Security
- Dynamic Filtering

---

# 🏛️ Data Warehouse Design

A dimensional model was built to optimize analytical performance and support business reporting requirements.

## Star Schema

### Fact Table

- Fact_Employees

### Dimension Tables

- Dim_Employee
- Dim_Department
- Dim_Job
- Dim_Education
- Dim_Attrition
- Dim_Performance

## Features

- Star Schema Modeling
- API Integration
- Power Query Transformations
- Analytical Data Modeling
- Optimized Reporting Performance

## Data Warehouse Design

![Star Schema 1](Project%20Steps/7.png)

![Star Schema 2](Project%20Steps/8.png)

---

# 📊 Final Power BI Dashboards

The approved Figma designs were transformed into fully interactive Power BI dashboards.

## Analytical Dashboard

![Power BI Analytical Dashboard](Project%20Steps/PowerBI%20Analytical%20Dashboard.png)

---

## Strategic Dashboard

![Power BI Strategic Dashboard](Project%20Steps/PowerBI%20StratgicDashboard.png)

---

# 📖 Dynamic Storytelling & Insight Generation

To improve executive decision-making, dynamic storytelling components were implemented using Power BI Flip Cards and advanced DAX measures.

The storytelling layer automatically generates business insights based on the selected filters, KPIs, and dimensions.

## Features

- Dynamic Insight Generation
- Context-Aware Narratives
- KPI Explanations
- Department-Level Summaries
- Attrition Trend Commentary
- Workforce Performance Narratives
- Executive-Friendly Reporting

## Storytelling Capabilities

The dashboard automatically explains:

- Which department has the highest attrition rate
- Which manager has the strongest team performance
- Changes in employee satisfaction
- Workforce demographic trends
- Key business observations
- Department comparisons
- Performance insights

The generated narrative changes dynamically based on user selections and filters.

## Business Benefits

- Faster Decision Making
- Reduced Manual Analysis
- Improved Data Understanding
- Executive-Level Reporting
- Self-Service Analytics
- Automated Business Insights

---

# 📈 Business Intelligence Features

The Power BI solution includes advanced analytical capabilities:

- Dynamic KPI Monitoring
- Field Parameters
- Measure Parameters
- Advanced DAX Calculations
- Dynamic Measures
- Dynamic Storytelling
- Flip Card Narratives
- Conditional Formatting
- Interactive Filtering
- Drill-Through Analysis
- Dynamic Narrative Cards
- Comparative Analysis
- Employee Attrition Insights
- Department Performance Analysis
- Workforce Demographics Analysis

---

# 🏗️ Solution Architecture

```text
┌────────────────────┐
│     Excel Files    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   Python ETL       │
│ (Pandas/SQLAlchemy)│
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│    SQL Server      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Spring Boot API    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Dynamic Manager    │
│ Data Filtering     │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Data Warehouse     │
│   Star Schema      │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│     Power BI       │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Dynamic Storytelling│
│ & HR Analytics     │
└────────────────────┘
```

---

# ⚙️ Technology Stack

| Layer | Technology |
|---------|------------|
| Data Source | Excel |
| ETL | Python |
| Data Processing | Pandas |
| ORM | SQLAlchemy |
| Database | SQL Server |
| Backend API | Spring Boot |
| API Documentation | Swagger |
| Data Warehouse | Star Schema |
| Data Transformation | Power Query |
| Business Intelligence | Power BI |
| Analytics | DAX |
| Dashboard Design | Figma |
| Version Control | Git |
| Repository Hosting | GitHub |

---

# 📂 Project Structure

```text
HR-Analytics-Project
│
├── ETL
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── models.py
│
├── Backend
│   ├── controller
│   ├── service
│   ├── repository
│   ├── entity
│   └── configuration
│
├── Data Warehouse
│   ├── Fact Tables
│   └── Dimension Tables
│
├── Power BI
│   ├── Analytical Dashboard
│   └── Strategic Dashboard
│
├── Project Steps
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   ├── 7.png
│   ├── 8.png
│   ├── Analytical Mockups Backgroud.png
│   ├── Figma Analytical Dashboard.png
│   ├── Stratgic Mockups Backgroud.png
│   ├── Figma Stratgic Dashboard.png
│   ├── Selected Query Code.png
│   ├── PowerBI Analytical Dashboard.png
│   └── PowerBI StratgicDashboard.png
│
└── README.md
```

---

# 💡 Key Skills Demonstrated

## Data Engineering

- ETL Pipeline Development
- Data Validation
- Data Transformation
- SQLAlchemy ORM
- SQL Server Integration

## Backend Development

- REST API Development
- Spring Boot
- MVC Architecture
- JPA Mapping
- Swagger Documentation

## Data Security

- Manager-Level Data Filtering
- Dynamic API Parameters
- Personalized Reporting
- Secure Data Consumption
- Performance Optimization

## Data Warehousing

- Star Schema Design
- Fact & Dimension Modeling
- Analytical Data Modeling

## Business Intelligence

- Power BI Development
- Advanced DAX
- Dynamic Reporting
- KPI Design
- Interactive Dashboards
- Dynamic Storytelling

## Dashboard Design

- Figma Mockups
- Dashboard UX/UI Design
- Analytical Storytelling
- Executive Dashboard Design

---

# 🎯 Business Value

This solution enables HR stakeholders to:

- Monitor workforce performance
- Analyze employee attrition trends
- Evaluate department effectiveness
- Understand workforce demographics
- Track employee satisfaction indicators
- Support strategic workforce planning
- Access manager-specific reports
- Improve decision-making through dynamic insights
- Make data-driven HR decisions

---

# 👨‍💻 Author

**AbdelRahman Mohamed Faheem**

Business Intelligence Analyst | Data Engineer | Power BI Developer

### Core Skills

- Power BI
- SQL Server
- Python
- Spring Boot
- Data Warehousing
- ETL Development
- Business Intelligence
- Data Engineering

---

⭐ If you found this project useful, consider giving it a star.
