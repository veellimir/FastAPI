from fastapi import FastAPI

# Install
# pip install fastapi[all]
# pip install sqlalchemy alembic psycopg2

# Start
# uvicorn main:app --reload

app = FastAPI(
    title='Site Vue 3'
)

fake_users = [
    {'id': 1, 'name': 'one'},
    {'id': 2, 'name': 'two'}
]
@app.get('/users/{user_id}')
def get_user(user_id):
    return user_id
