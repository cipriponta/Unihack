from app import app, db
from app.database_models import Person

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Person': Person}