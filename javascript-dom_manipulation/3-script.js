function toggleClass() {
    const header = document.querySelector("header")
    header.classList.toggle("red")
    header.classList.toggle("green")
  }
  
  const tag = document.getElementById("toggle_header")
  tag.addEventListener("click", toggleClass)
