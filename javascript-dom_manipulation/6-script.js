  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    return response.json()
  })
  .then(data => {
      const tag = document.getElementById("character")
      tag.innerHTML = data.name
  })
  .catch(error => {
    console.error('Error:', error)
  })