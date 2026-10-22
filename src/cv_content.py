"""CV content, kept separate from layout so the DOCX and PDF always say the same thing.

Facts come from the author's published CV repo and project READMEs. Edit here, then run build_cv.py.
"""

NAME = "Emmanuel Omowumi"
TITLE = "Data Analyst | SQL, Python, Power BI | Fintech and Commercial Analytics"
CONTACT = [
    ("Lagos, Nigeria", None),
    ("emmanueloluwatobi2015@gmail.com", "mailto:emmanueloluwatobi2015@gmail.com"),
    ("linkedin.com/in/emmanuel-omowumi-98bb03139", "https://www.linkedin.com/in/emmanuel-omowumi-98bb03139/"),
    ("github.com/Nuelwumi2024", "https://github.com/Nuelwumi2024"),
]

SUMMARY = (
    "Data analyst with 3+ years of experience in business intelligence, SQL reporting and dashboard development, "
    "now working in sales analytics. M.Sc. in Microbiology, with earlier experience in laboratory and quality "
    "assurance, which built a habit of validating data, tracing deviations to root cause and reporting "
    "clearly to management. Builds end-to-end analytics projects on Nigerian data (inflation, payments, "
    "distribution, customer reviews) with tested code, stated limitations and recommendations a decision-maker "
    "can act on."
)

SKILLS = [
    ("Analysis & BI", "SQL (MySQL, SQL Server, DuckDB), Power BI (DAX, Power Query), Tableau, Excel"),
    ("Programming", "Python (pandas, NumPy, Matplotlib), R (tidyverse), pytest"),
    ("Data engineering", "ETL/ELT design, star-schema modelling, dbt, Airflow, data-quality testing, GitHub Actions CI"),
    ("Methods", "KPI and cohort analysis, forecasting, statistical testing and regression, risk metrics, root cause analysis"),
    ("Domains", "Sales analytics, fintech (payments, fraud, lending), FMCG distribution, quality assurance"),
]

EXPERIENCE = [
    {
        "role": "Data Analyst, Sales Department",
        "org": "Learn Africa Plc",
        "where": "Nigeria",
        "dates": "June 2025 - Present",
        "bullets": [
            "Turn sales data into reporting and insight that supports sales decisions, using SQL, Power BI and Excel.",
            "Present findings to the sales team as clear summaries and recommendations.",
        ],
    },
    {
        "role": "Senior Data Analyst",
        "org": "Softrays Information Technology",
        "where": "Ilorin, Kwara State, Nigeria",
        "dates": "January 2023 - March 2025",
        "bullets": [
            "Built and maintained Tableau and Power BI dashboards that tracked KPIs for projects and teams.",
            "Analysed customer survey data in Excel, R and Python to identify trends that shaped marketing strategy.",
            "Cleaned and prepared data for data science work, improving data accuracy and model performance.",
            "Queried relational databases with SQL for filtering and aggregation; applied hypothesis testing, correlation and regression.",
            "Worked with cross-functional teams to turn findings into reports, presentations and recommendations.",
        ],
    },
    {
        "role": "Quality In-Process Analyst",
        "org": "Olam",
        "where": "Ilorin, Kwara State, Nigeria",
        "dates": "February 2021 - December 2023",
        "bullets": [
            "Analysed microbiological and quality test data from raw materials, in-process samples and finished livestock-feed products to detect and prevent contamination.",
            "Led risk assessments and root cause analysis on quality deviations, and produced trend analysis and non-conformance reports for management.",
            "Wrote and rolled out SOPs and quality control procedures; kept production compliant with GMP, GHP and HACCP.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Nigeria Cost-of-Living Tracker",
        "stack": "Python, pandas, Power BI (DAX), pytest, GitHub Actions",
        "url": "github.com/Nuelwumi2024/nigeria-cost-of-living-tracker",
        "bullets": [
            "Parsed 30+ years of National Bureau of Statistics CPI data (1995-2026) into a validated dataset; recomputed year-on-year inflation matches NBS to 0.01 percentage points.",
            "Found that the published index drops about 2.8% every January in 2025 and 2026 (no January fell by more than 0.9% in 1996-2024), flagged it, and showed results with a sensitivity case and a two-scenario outlook.",
            "Quantified purchasing-power loss and the real value of the minimum wage; delivered an executive brief and a Power BI data model.",
        ],
    },
    {
        "name": "FMCG Distribution Analytics (synthetic data)",
        "stack": "SQL, DuckDB, Python, Power BI (DAX), pytest",
        "url": "github.com/Nuelwumi2024/nigeria-fmcg-distribution-analytics",
        "bullets": [
            "Analysed margin, product mix, channels, stock-outs and rep attainment in SQL; found gross margin falling from 18.8% to 11.8% as costs outran prices.",
            "Detected 23 silent outlets (about NGN 9.2M annual revenue at risk) and validated the detector and the stock-out loss estimate (within 11%) against the generator's known ground truth.",
        ],
    },
    {
        "name": "Nigerian App Review Analysis",
        "stack": "Python, pandas, regex NLP, pytest",
        "url": "github.com/Nuelwumi2024/nigeria-app-review-analysis",
        "bullets": [
            "Classified 34,000 public reviews of 7 fintech, bank and telecom apps into nine complaint themes with an auditable rule set; login and verification problems were the top complaint (17.5% of 1-2 star reviews).",
            "Estimated the star-rating cost of each theme with confidence intervals and produced a ranked fix list per app; removed personal data and published aggregates only.",
        ],
    },
    {
        "name": "Naira Payments ETL Pipeline (synthetic data)",
        "stack": "Python, DuckDB, SQL, Airflow, pytest, GitHub Actions",
        "url": "github.com/Nuelwumi2024/naira-payments-etl-pipeline",
        "bullets": [
            "Built a batch ETL with a star schema that processed 117,891 raw records, quarantined 1,051 bad rows with reasons and removed 703 duplicates; the run fails unless row counts reconcile.",
        ],
    },
    {
        "name": "Fintech dbt Analytics Warehouse and Fraud Analysis (synthetic data)",
        "stack": "dbt, DuckDB, SQL, Python",
        "url": "github.com/Nuelwumi2024/fintech-dbt-analytics-warehouse",
        "bullets": [
            "Built a layered dbt warehouse (8 models, 12 data tests, all passing) with CI running dbt build on every push.",
            "Showed fraud is about 2.9x likelier at night and that four simple rules catch 29% of fraud while reviewing 7.7% of traffic.",
        ],
    },
]

EDUCATION = [
    ("M.Sc. Microbiology", "Kwara State University, Malete", "2021 - 2023"),
    ("B.Sc. Microbiology", "Kwara State University, Malete", "2018 - 2020"),
    ("B.Sc. Botany / Plant Biology", "University of Ilorin", "2013 - 2017"),
]

CERTIFICATIONS = [
    "Microsoft PL-300: Power BI Data Analyst Associate (exam preparation in progress)",
    "Advanced Data Analytics 2025 (Excel, SQL, Power BI, Python)",
    "Advanced BI and DAX Modelling (Excel / Power Query)",
]

PORTFOLIO_LINE = "Portfolio of 8 projects with code, tests and write-ups: github.com/Nuelwumi2024"
