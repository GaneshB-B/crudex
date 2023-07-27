from fastapi import FastAPI, HTTPException
from typing import Optional
from db import Session
from model import Employee

app = FastAPI()

@app.get('/')
async def root():
	return {'message': 'Hello World'}

@app.get('/employees')
async def read(id: Optional[int] = None):
	with Session() as db:
		employees = db.query( Employee )

		if id:
			employees = employees.filter( Employee.id == id )

		employees = employees.all()

		if len(employees) == 0:
			raise HTTPException(status_code=404, detail='No Employees Found')

		return employees

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
