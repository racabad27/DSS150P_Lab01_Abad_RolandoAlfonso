# DSS150P Weeks 1–2 Starter Repository

This repository is intentionally incomplete. You should inspect and extend it,
not copy a completed pipeline.

## Included sources
- `data/customers.csv`
- `data/orders.json`
- `data/products.parquet`
- optional `products_optional_compare.csv` and `.json`
- `sql/seed_support_tickets.sql`
- public REST API configured in `src/fetch_api.py`

## Quick start
1. `python -m venv .venv`
2. Activate the virtual environment.
3. `pip install -r requirements.txt`
4. Copy `.env.example` to `.env`.
5. `docker compose up -d`
6. Load `sql/seed_support_tickets.sql` into PostgreSQL.
7. Run the starter scripts.
8. Extend the code only as required by the laboratory activity.

The starter files intentionally stop before a complete data pipeline.

## REST API choices
- Public: `https://jsonplaceholder.typicode.com/posts`
- Local fallback: run `python src/local_api_server.py`, then call
  `http://localhost:8000/api/orders`

The local option is useful when your internet access is unreliable.

## Lab Activity #1 (Rolando Alfonso C. Abad/2022136475)

## Purpose of Laboratory 
-  Learn and get familiar with the setup of the data engineering field using various software and previously learned concepts.
## Software Requirements
- Python 3.x
- Git
- Docker Desktop (with WSL/Windows integration)
- PostgreSQL 16 (via Docker)
- Visual Studio Code

## Exact steps to reproduce the environment
- Clone/create folder for repository
- Create the virtual environment
- Activate the venv
- Create the requirements.txt for dependencies
- Install appropriate dependencies (pandas,pyarrow, requests, sqlalchemy, psycopg2-binary)
## Exact commands to start and stop PostgreSQL
  Start:
```powershell
docker compose up -d
```

Confirm it's running:
```powershell
docker ps
```

Stop (preserves data):
```powershell
docker compose down
```

Stop and wipe all data (fresh start):
```powershell
docker compose down -v
```
## How to run each Python script
- Make sure that you have venv enabled first 
- python src\verify_environment.py — connects to PostgreSQL, prints version and database name
- python src\profile_sources.py` — profiles customers.csv, orders.json, products.parquet
- python src\inspect_api.py — retrieves and inspects the REST API, saves api_snapshot.json
## Description of each source
- Customer_csv =  A structured csv file containing customer records.
- orders.json = A semi-structured JSON file that contains containing records for orders, which also has nested fields and a primary key "order_id".
- REST API =  Providing continuously updating records.
- POSTGRE SQL = Live DB with a defined schema, with ticket_id as the primary key.
## Known limitations or unresolved questions 
- Owner, freshness_expectation0 are listed as unknown 
- Ai usage was used mostly for synthesizing and revising codes from task 2.2 onwards.