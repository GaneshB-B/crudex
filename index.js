print = console.log

const addData = () => {
	const tbl = document.getElementById('employees')

	fetch( 'http://localhost:8000/employees' )
		.then( res => res.json() )
		.then( employees => employees.forEach(
			employee => {
				// print( employee )

				const row = tbl.insertRow(-1)

				const id = row.insertCell(-1)
				id.innerText = employee.id

				const f_name = row.insertCell(-1)
				f_name.innerText = employee.f_name

				const m_name = row.insertCell(-1)
				m_name.innerText = employee.m_name

				const l_name = row.insertCell(-1)
				l_name.innerText = employee.l_name

				const title = row.insertCell(-1)
				title.innerText = employee.title

				const age = row.insertCell(-1)
				age.innerText = employee.age

				const city = row.insertCell(-1)
				city.innerText = employee.city

				const salary = row.insertCell(-1)
				salary.innerText = employee.salary

				const joining = row.insertCell(-1)
				joining.innerText = employee.joining

				const active = row.insertCell(-1)
				active.innerText = employee.active ? 'yes' : 'no'
			}
		) )

}

window.onload = addData