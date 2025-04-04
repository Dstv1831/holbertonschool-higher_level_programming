function addClass() {
    const header = document.querySelector("header")
    header.classList.add('red')
}

const tag = document.getElementById("red_header")
tag.addEventListener("click", addClass)
