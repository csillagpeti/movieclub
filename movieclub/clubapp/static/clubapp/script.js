function getCSRFToken() {
  let cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.startsWith("csrftoken=")) {
      return cookie.substring("csrftoken=".length, cookie.length);
    }
  }
  return "";
}

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".togglelistbutton").forEach((button) => {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      console.log("Button clicked:", this.getAttribute("data-id"));
      const movieId = this.getAttribute("data-id");
      const movieTitle = this.getAttribute("data-title");

      // Use fetch to send a POST request
      fetch("toggle_movie_list/", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": getCSRFToken(),
        },
        body: "movie_id=" + movieId + "&movie_title=" + movieTitle,
      })
        .then((response) => response.text())
        .then((text) => {
          if (text === "added") {
            this.textContent = "Remove from Favorites";
          } else if (text === "removed") {
            this.textContent = "Add to Favorites";
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  });
});
