  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`)
    }
    return response.json()
  })
  .then(data => {
    const uno_lis = document.querySelector("ul")
    data.results.forEach(element => {
      movie_title = document.createElement("li")
      movie_title.innerHTML=element.title
      uno_lis.appendChild(movie_title)
    });
  })
  .catch(error => {
    console.error('Error:', error)
  })