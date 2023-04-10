let elList = document.querySelector("#list");
// http://127.0.0.1:8000/swagger/
// http://127.0.0.1:8000/redoc/
async function userRenderFunc(element) {
  let data = await fetch("http://127.0.0.1:8000/redoc/")
    .then((res) => res.json())
    .then((data) => data)
    .catch((error) => console.log(error));

    console.log(data)
}

