# Architecture Rules
- Keep responsibilities separated and interfaces explicit.
- Preferred layers: Presentation/UI, Flask routes, Application/service logic, Priority scoring, ML prediction, Database/repository layer.
- Do not put the entire application into a single giant app.py file.
- Avoid circular dependencies.
- Keep reusable business logic outside route handlers where practical.