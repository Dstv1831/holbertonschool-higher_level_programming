  document.addEventListener('DOMContentLoaded', () =>
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`)
        }
      return response.json()
    })
      .then(data => {
      console.log(data)
      const greetings = document.getElementById('hello')
      greetings.textContent=data.hello
    })
    .catch(error => {
      console.error('Error:', error)
    })
  )