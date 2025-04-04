function update_text() {
  const header = document.querySelector("header")
  header.innerHTML="New Header!!!"
  }
  
  const tag = document.getElementById("update_header")
  tag.addEventListener("click", update_text)
