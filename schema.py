from pydantic import BaseModel
from datetime import date

class Employee(BaseModel):
  id: int | None = None
  f_name: str
  m_name: str | None = None
  l_name: str
  title: str
  age: int
  city: str
  salary: int | None = None
  joining: date
  active: bool
