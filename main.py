from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
	return {'message': 'Hello World'}

@app.get('/employees')
async def read_all():
	pass

@app.get('/employees/{id}')
async def read_path(id: int):
	pass

@app.get('/employees')
async def read_query(id: int):
	pass

@app.post('/employees')
async def create():
	pass

@app.put('/employees')
async def update(id: int):
	pass

@app.delete('/employees')
async def delete(id: int):
	pass


# path param
# http://url/A1204

# query param
# http://url?id=A1204
