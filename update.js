print = console.log

const id = 3

const fetchData = async form => {
	const res = await fetch( `http://localhost:8000/employees?id=${id}` )
	const employees = await res.json()
  const employee = employees[0]

  print( employee )
  form.elements[0].value = employee.f_name
  form.elements[1].value = employee.m_name
  form.elements[2].value = employee.l_name
  form.elements[3].value = employee.title
  form.elements[4].value = employee.age
  form.elements[5].value = employee.city
  form.elements[6].value = employee.salary
  form.elements[7].value = employee.joining
  form.elements[8].checked = employee.active
}

const formSubmit = event => {
  event.preventDefault()

  const formData =  Object.fromEntries( new FormData( event.target ).entries() )

  // convert
  formData.age = parseInt( formData.age )
  formData.salary = parseInt( formData.salary )
  formData.active = formData.active ? true : false

  print( formData )

  fetch( `http://localhost:8000/employees?id=${id}`, {
    method: 'PUT',
    body: JSON.stringify( formData )
  } )
}

window.onload = () => {
  const form = document.getElementById('employee')
  
  fetchData( form )

  form.addEventListener('submit', formSubmit)
}
