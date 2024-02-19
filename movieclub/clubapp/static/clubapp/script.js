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
      const movieId = this.getAttribute("data-id");
      const movieTitle = this.getAttribute("data-title");
      const moviePosterPath = this.getAttribute("data-poster-path");
      const movieOverview = this.getAttribute("data-overview");
      const movieReleaseDate = this.getAttribute("data-release-date");
      const movieVoteAverage = this.getAttribute("data-vote-average");

      fetch("toggle_movie_list/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify({
          movie_id: movieId,
          movie_title: movieTitle,
          movie_poster_path: moviePosterPath,
          movie_overview: movieOverview,
          movie_release_date: movieReleaseDate,
          movie_vote_average: movieVoteAverage,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.action === "added") {
            this.textContent = "Remove from Favorites";
          } else if (data.action === "removed") {
            this.textContent = "Add to Favorites";
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  });
});
