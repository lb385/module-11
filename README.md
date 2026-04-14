# Module 11 Calculation Service

This module adds a SQLAlchemy `Calculation` model, Pydantic validation, and a small factory for arithmetic operations.

## What is included

- SQLAlchemy model for calculations with `a`, `b`, `type`, and `result`
- Pydantic schemas for create/read validation
- Factory pattern for `Add`, `Sub`, `Multiply`, and `Divide`
- Unit tests and integration tests
- GitHub Actions workflow with PostgreSQL, Trivy scanning, and Docker Hub deployment

## Run the tests

```bash
python -m pip install -r requirements-dev.txt
pytest
```

To run against PostgreSQL locally, set `DATABASE_URL` or `TEST_DATABASE_URL` before running `pytest`.

## Docker

Build the image:

```bash
docker build -t module11 .
```

Run the container:

```bash
docker run --rm module11
```

## Docker Hub

Add your Docker Hub image link here, for example:

https://hub.docker.com/repository/docker/lohiteesh256/module11/general

## Notes

- The `CalculationCreate` schema rejects invalid operation types and division by zero.
- The application entry point is `python -m app`, which performs a sample calculation so the container is runnable even before Module 12 adds routes.
