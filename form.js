print = console.log

const formSubmit = event => {
  event.preventDefault()

  const formData =  Object.fromEntries( new FormData( event.target ).entries() )

  // convert
  formData.age = parseInt( formData.age )
  formData.salary = parseInt( formData.salary )
  formData.active = formData.active ? true : false

  print( formData )

  fetch( 'http://localhost:8000/employees', {
    method: 'POST',
    body: JSON.stringify( formData )
  } )
}

window.onload = () => document.getElementById('employee').addEventListener('submit', formSubmit)
