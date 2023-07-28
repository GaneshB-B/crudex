from fastapi import FastAPI, HTTPException
from typing import List, Optional
from db import Session
from model import Employee as EmployeeModel
from schema import Employee as EmployeeSchema

app = FastAPI()

@app.get('/')
async def root():
	return {'message': 'Hello World'}

@app.get('/employees', response_model=List[EmployeeSchema])
async def read(id: Optional[int] = None):
	with Session() as db:
		employees = db.query( EmployeeModel )

		if id:
			employees = employees.filter( EmployeeModel.id == id )

		employees = employees.all()

		if len(employees) == 0:
			raise HTTPException(status_code=404, detail='No Employees Found')

		return employees

@app.post('/employees', response_model=EmployeeSchema)
async def create(employee: EmployeeSchema):
	with Session() as db:
		try:
			db_employee = EmployeeModel(**employee.dict())

			db.add(db_employee)
			db.commit()
			db.refresh(db_employee)

		except Exception as e:
			print(e)
			db.rollback()

			raise HTTPException(status_code=400, detail='Employee Not Added')

		return db_employee

@app.put('/employees', response_model=EmployeeSchema)
async def update_employee(id: int, employee: EmployeeSchema):
	with Session() as db:
		db_employee = db.get(EmployeeModel, id)

		if db_employee is None:
			raise HTTPException(status_code=400, detail='Employee Not Found')

		try:
			employee_data = employee.dict(exclude_unset=True)

			for key, value in employee_data.items():
				setattr(db_employee, key, value)
			db.add(db_employee)
			db.commit()
			db.refresh(db_employee)

		except Exception as e:
			print(e)
			db.rollback()
			raise HTTPException(status_code=400, detail="Employee Update Failed")

	return db_employee

@app.delete('/employees')
async def delete(id: int):
	pass


# path param
# http://url/A1204

# query param
# http://url?id=A1204
