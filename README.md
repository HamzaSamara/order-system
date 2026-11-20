# Order Processing System

A small order processing API, built step by step while learning DevOps.
It lets you create orders and read them back over HTTP.

## Tech stack

- Python 3.14
- FastAPI (web framework) + Uvicorn (server)
- Pydantic (input validation)
- SQLite (database, one file: `orders.db`)

## Project structure

```
order-system/
├── app/
│   ├── __init__.py      # makes "app" a Python package
│   ├── main.py          # FastAPI app and endpoints
│   └── database.py      # SQLite connection and table setup
├── requirements.txt     # Python dependencies (pinned versions)
├── .gitignore
└── README.md
```

## Setup (first time)

```bash
git clone git@github.com:HamzaSamara/order-system.git
cd order-system
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
source .venv/bin/activate
fastapi dev app/main.py
```

- API: http://127.0.0.1:8000
- Interactive docs: http://127.0.0.1:8000/docs

The database file and the `orders` table are created automatically on startup.

## API endpoints

| Method | Path                 | Description                     | Success | Errors   |
|--------|----------------------|---------------------------------|---------|----------|
| GET    | `/`                  | Welcome message                 | 200     |          |
| GET    | `/health`            | Health check                    | 200     |          |
| POST   | `/orders`            | Create a new order              | 201     | 422      |
| GET    | `/orders`            | List all orders                 | 200     |          |
| GET    | `/orders/{order_id}` | Get one order by id             | 200     | 404, 422 |

### Example

```bash
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{"customer_name": "Sara", "product": "Keyboard", "quantity": 1}'
```

Validation rules for a new order:

- `customer_name`: 1 to 50 characters
- `product`: at least 1 character
- `quantity`: from 1 to 100

## Configuration

| Variable        | Default     | Description                  |
|-----------------|-------------|------------------------------|
| `DATABASE_PATH` | `orders.db` | Path to the SQLite database  |

Example: `DATABASE_PATH=test.db fastapi dev app/main.py`

## Roadmap

- [x] Phase 0: Linux, WSL, Git, GitHub
- [x] Phase 1: FastAPI + SQLite
- [ ] Phase 2: SQL Server + SQLAlchemy + Alembic
- [ ] Phase 3: Docker + Docker Compose
- [ ] Phase 4: RabbitMQ worker
- [ ] Phase 5: Nginx + HAProxy + Redis
- [ ] Phase 6: CI/CD
- [ ] Phase 7: Azure
- [ ] Phase 8: Kubernetes + Helm
- [ ] Phase 9: Terraform + ArgoCD
- [ ] Phase 10: Monitoring + Security
