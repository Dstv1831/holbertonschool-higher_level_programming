function add_item() {
  list_item = document.createElement("li")
  const uno_list = document.querySelector("ul")
  uno_list.appendChild(list_item)
  }
  
  const tag = document.getElementById("add_item")
  tag.addEventListener("click", add_item)
