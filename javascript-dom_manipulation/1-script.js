function changeColor() {
    const header = document.querySelector("header")
    header.style.color="#FF0000"
}

const tag = document.getElementById("red_header")
tag.addEventListener("click", changeColor)
