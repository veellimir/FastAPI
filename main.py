from fastapi import FastAPI

# Install
# pip install fastapi[all]

# Start
# uvicorn main:app --reload

app = FastAPI()

@app.get('/')
def hello():
    return 'hello'
