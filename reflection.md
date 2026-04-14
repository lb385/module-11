# Reflection

## Key Experiences

- Building the calculation feature was a good exercise in separating domain logic from persistence.
- The factory pattern made the arithmetic behavior easy to extend without changing the data model.
- Validating division by zero at the schema layer reduced the chance of bad data reaching the database.

## Challenges

- Keeping the model, schema, and tests aligned took a little extra care because the assignment focuses on validation rather than endpoints.
- Designing the CI workflow to support PostgreSQL while still working locally required a flexible test setup.
- Since Module 12 will add routes, I kept the application intentionally small and focused on the data layer.
