# Household Income Data Engineering Pipeline

## Project Overview

This project demonstrates the development of an end-to-end data engineering and analytics pipeline using household financial transaction data.

The project processes over 400,000 household transaction records, transforming raw data into structured, reliable and analysis-ready datasets for business intelligence reporting.

The solution implements a complete data workflow, covering data profiling, ingestion, database storage, transformation, analytical modelling and business intelligence visualisation.

The project was developed to demonstrate practical data engineering and analytics engineering skills, alongside the ability to translate raw transactional data into meaningful financial insights.

## Project Objectives

- Build an end-to-end data pipeline for processing household financial transactions.
- Apply Python for data profiling, validation and ingestion.
- Implement relational data storage using SQL Server.
- Develop modular and maintainable data transformations using dbt.
- Apply data quality checks and transformation testing.
- Develop analytical models for household income and expenditure analysis.
- Create BI reports to communicate household financial trends and insights.
- Apply version control and project documentation practices using Git and GitHub.

## Technology Stack

| Technology | Application |
|---|---|
| Python | Data profiling, preparation and ingestion |
| Pandas | Data manipulation and processing |
| SQL Server | Relational database and data storage |
| SQL | Data extraction, transformation and analysis |
| dbt | Data transformation, modelling and testing |
| Power BI | Business intelligence reporting and visualisation |
| Git & GitHub | Version control and project documentation |

## Dataset Description

The project uses a household financial transactions dataset containing over 400,000 records.

The dataset captures household-level financial activity, including:

- Household identifiers
- Transaction identifiers
- Account identifiers
- Transaction dates
- Transaction types and classifications
- Transaction categories and families
- Inflow and outflow indicators
- Transaction values in KES and USD
- Observation periods

The dataset was initially provided in CSV format and subsequently processed through the data pipeline.

The original raw data was preserved to maintain data integrity and provide a consistent source for the transformation process.

**Important analytical consideration:** Not every cash inflow represents income. The project considers transaction classifications and financial context when distinguishing income from other inflows.

## Pipeline Architecture

The project follows a structured data engineering workflow:

```text
             RAW DATA
                 |
                 v
          HOUSEHOLD CSV
                 |
                 v
              PYTHON
       Data Profiling & Validation
          Data Preparation
                 |
                 v
           SQL SERVER
           Data Storage
                 |
                 v
               dbt
                 |
                 v
          STAGING MODELS
       Cleaning and Standardisation
                 |
                 v
          ANALYTICAL MARTS
       Business Logic & Aggregation
                 |
                 v
          ANALYTICAL DATA
       Household Income Analysis
       Expenditure Analysis
       Cash Flow Metrics
                 |
                 v
             POWER BI
       BI Reports & Visualisations
```

## Project Structure

The repository is organised into modular directories to separate data, scripts, transformations and documentation.

```text
household_income_pipeline/
│
├── data/
│   └── raw/
│
├── scripts/
│   └── Python profiling and ingestion scripts
│
├── dbt_project/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   ├── tests/
│   ├── macros/
│   └── dbt_project.yml
│
├── reports/
│   └── BI reports and supporting outputs
│
├── .gitignore
└── README.md
```

*The structure above describes the logical organisation of the project; directory names should match the actual repository.*

## Implementation Details

### 1. Data Profiling and Exploration

Python was used to explore and understand the source dataset before ingestion.

Activities included:

- Inspecting dataset dimensions and column structures.
- Reviewing data types.
- Identifying missing values.
- Checking duplicate records.
- Examining transaction dates and observation periods.
- Reviewing transaction classifications.
- Analysing inflow and outflow distributions.
- Identifying potential data quality issues.

### 2. Data Ingestion and Database Storage

Python was used to prepare and ingest the household transaction data into SQL Server.

The ingestion process established a structured database layer for subsequent transformations and analysis.

SQL Server provided persistent relational storage and enabled the use of SQL for downstream data processing.

### 3. Data Transformation with dbt

dbt was implemented to organise SQL transformations into modular, reusable and testable models.

The transformation process included:

**Staging layer**
- Standardising column names.
- Casting and validating data types.
- Cleaning and preparing transaction records.
- Applying consistent transformation logic.

**Analytical marts**
- Developing household-level analytical datasets.
- Aggregating income and expenditure.
- Calculating household cash-flow metrics.
- Preparing structured datasets for business intelligence reporting.

dbt testing was incorporated to improve data reliability and validate transformation outputs.

### 4. Household Financial Analysis

The transformed datasets were used to explore household financial behaviour.

The analysis focused on:

- Household income patterns.
- Household expenditure patterns.
- Net cash flow.
- Income and expenditure trends over time.
- Household-level financial activity.
- Differences in financial behaviour across households.

### 5. Business Intelligence Reporting

Power BI was used to develop reports and visualise the analytical outputs.

The reporting layer translates the transformed data into accessible insights, enabling users to explore household financial activity and understand income and expenditure patterns.

The BI reports provide a business-facing layer on top of the engineered data pipeline.

## Data Governance and Security

The project incorporates basic data management and security practices:

- Preserving the original raw dataset.
- Separating raw data from transformed datasets.
- Excluding large source files from version control.
- Keeping database credentials and sensitive configuration files outside the repository.
- Using `.gitignore` to prevent accidental exposure of sensitive files.
- Applying data validation and testing throughout the transformation process.

## Project Completion Status

| Component | Status |
|---|---|
| Project setup and Git initialisation | Completed |
| Python environment configuration | Completed |
| Data profiling and exploration | Completed |
| SQL Server database setup | Completed |
| Python-based data ingestion | Completed |
| dbt project configuration | Completed |
| Staging transformations | Completed |
| Analytical data marts | Completed |
| Data quality testing | Completed |
| Household financial analysis | Completed |
| Power BI reporting | Completed |
| Project documentation | Completed |

## Key Learning Outcomes

This project provided practical experience in:

- Building an end-to-end data engineering pipeline.
- Processing large CSV datasets using Python.
- Designing and working with relational databases.
- Writing SQL for data transformation and analysis.
- Implementing ELT workflows using dbt.
- Developing modular analytical data models.
- Applying data quality checks and validation.
- Managing projects using Git and GitHub.
- Connecting engineered datasets to BI reporting tools.
- Translating financial transaction data into business insights.

## Conclusion

The Household Income Data Engineering Pipeline demonstrates the application of data engineering and analytics engineering principles to a real-world financial dataset.

By integrating Python, SQL Server, dbt and Power BI, the project establishes a complete workflow from raw data ingestion to business intelligence reporting.

Beyond producing analytical outputs, the project demonstrates an understanding of data pipeline architecture, data transformation, database management, data quality and the delivery of reliable datasets for business decision-making.

---

**Author:** Cynthia Nafula  
**Project:** Household Income Data Engineering Pipeline  
**Domain:** Household Financial Analytics  
**Focus Areas:** Data Engineering | Analytics Engineering | Business Intelligence
