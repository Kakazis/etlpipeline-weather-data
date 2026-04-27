# 🌦️ ETL Weather Data Pipeline

End-to-end Data Engineering project designed to collect, transform, store, and orchestrate weather data using modern data stack tools.

This pipeline extracts real-time weather data from the OpenWeather API, processes and standardizes the information with Python/Pandas, loads the results into PostgreSQL, and orchestrates the workflow using Apache Airflow — all containerized with Docker.

---

## 🚀 Project Overview

This project simulates a real-world ETL pipeline and demonstrates practical skills in:

- Data Extraction from REST APIs
- Data Cleaning & Transformation
- Relational Database Loading
- Workflow Orchestration
- Dockerized Infrastructure
- Environment Variable Management
- Git Version Control

---

## 🏗️ Architecture

```text
OpenWeather API
      ↓
Extract (Python Requests)
      ↓
Transform (Pandas)
      ↓
Load (PostgreSQL)
      ↓
Orchestration (Apache Airflow)
      ↓
Dockerized Local Environment

⚙️ Tech Stack
Python 3.12
Pandas
SQLAlchemy
PostgreSQL
Apache Airflow
Docker & Docker Compose
UV Package Manager
Git / GitHub
WSL (Windows Subsystem for Linux)

📁 Project Structure
etlpipeline-weather-data/
│── dags/                 # Airflow DAGs
│── src/                  # Python ETL modules
│   ├── extract_data.py
│   ├── transform_data.py
│   └── load_data.py
│── config/               # Environment configs (.env ignored)
│── data/                 # Temporary/raw data
│── logs/                 # Airflow logs
│── docker-compose.yml
│── main.py               # Local pipeline execution
│── pyproject.toml
│── README.md

🔄 ETL Pipeline Steps
1️⃣ Extract

Fetches weather data from OpenWeather API.

2️⃣ Transform

Processes nested JSON data and performs:

Column normalization
Column renaming
Datetime conversion
Schema cleanup

3️⃣ Load

Loads transformed dataset into PostgreSQL.

4️⃣ Orchestration

Airflow schedules and monitors pipeline execution.

▶️ How to Run
Clone repository
git clone https://github.com/Kakazis/etlpipeline-weather-data.git
cd etlpipeline-weather-data
Start containers
docker compose up -d
Run local ETL test
uv run main.py
Access Airflow
http://localhost:8080

Default credentials:

Username: airflow
Password: airflow
📊 Sample Output
✅ Dados carregados com sucesso!
Total de registros na tabela: 1

💡 Key Learnings

During this project I practiced:

Building reproducible data environments with Docker
Managing Airflow workers and DAG orchestration
PostgreSQL networking inside containers
Handling secrets with .env files
Debugging real-world pipeline issues
End-to-end data engineering workflow

📌 Future Improvements
Incremental Loads
Historical Weather Storage
Data Quality Tests
CI/CD with GitHub Actions
Dashboard with Power BI / Metabase
Cloud Deployment (AWS / Azure / GCP)

👨‍💻 Author

Kaliton Oliveira
Data Analytics | Data Engineering | Databricks | AI

LinkedIn: https://www.linkedin.com/in/kalitonoliveira