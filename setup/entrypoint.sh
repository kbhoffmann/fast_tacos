#!/bin/bash
python wait_for_db.py
sleep 10
alembic upgrade head
python -m uvicorn main:app --reload --port 8000 --host 127.0.0.1