// get CSRF Token for POST requests

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

// Add/Remove Favorites function

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
      const removal = this.classList.contains("btn-danger");

      if (removal) {
        if (!confirm("Are you sure?")) {
          return false;
        }
      }
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
          let panel = this.parentElement;
          while (!panel.classList.contains("panel")) {
            panel = panel.parentElement;
          }
          if (data.action === "added") {
            this.textContent = "Remove Favorite";
            this.classList.remove("btn-success");
            this.classList.add("btn-danger");
            panel.classList.add("bg-light");
          } else if (data.action === "removed") {
            this.textContent = "Add to Favorites";
            this.classList.remove("btn-danger");
            this.classList.add("btn-success");
            panel.classList.remove("bg-light");
          }
          if (removal) {
            location.reload();
          }
          this.blur();
        })
        .catch((error) => console.error("Error:", error));
    });
  });
});

// Update layout for responsivity

document.addEventListener("DOMContentLoaded", function () {
  const adjustOverviewLength = () => {
    const overviews = document.querySelectorAll(".overview");

    overviews.forEach((overview) => {
      // Store full text for restore
      if (!overview.dataset.fullText) {
        overview.dataset.fullText = overview.textContent;
      }
      const maxChars = window.innerWidth > 1100 ? 255 : 50;

      overview.textContent =
        overview.dataset.fullText.substr(0, maxChars) +
        (overview.dataset.fullText.length > maxChars ? "..." : "");
    });
  };

  adjustOverviewLength();
  window.addEventListener("resize", adjustOverviewLength);
});
