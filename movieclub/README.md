# MovieClub README.md

## Overview

MovieClub is a web application that connects movie enthusiasts through shared interests. Leveraging the TMDB API, it allows users to discover movies, curate personal lists, and compare these with others. This project stands out by integrating live data and offering a platform for interaction rather than just information consumption.

## Distinctiveness and Complexity

### Distinctiveness

MovieClub differentiates itself by enabling users to interact with a live movie database, compare personal movie lists, and discover common interests with others, moving beyond the static content delivery of typical projects.

### Complexity

The application's complexity is rooted in several areas:

- **TMDB API Integration**: Fetches and displays live movie data, handling API requests and responses.
- **User Authentication**: Manages user sessions, sign-ups, logins, and profile management.
- **Responsive Design**: Ensures the site is accessible across various devices, enhancing user experience.
- **Dynamic Content Management**: Allows users to add or remove movies from their lists and compare these lists with other users, requiring intricate backend logic and database management.

## Project Structure

### Templates:
- **`layout.html`**: The base template for the application, defining the navigation menu and layout.
- **`list_display.html`**: Serves as list generator to display movies on several other pages when included, and their corresponding user actions.
- **`my_list.html`**: When logged in, displays the favorites
- **`users.html`**: Gives the unique selling point of the site: compare your movie list with other users.
- **`login.html, register.html`**: Serving the user management


- **`styles.css`**: Contains custom CSS for styling the application.
- **`script.js`**: Handles client-side logic, including interactions with the TMDB API and dynamic updates.
- **`views.py`**: Defines the server-side logic, including endpoint definitions and interaction with the database.
- **`models.py`**: Outlines the data models for users and their movie lists.
- **`fetch_tmdb.py`**: Since fetching the movie objects is several lines of code, I moved the fetching functions into a separate py file.
- **`requirements.txt`**: Lists the project's Python dependencies.

## Running the Application

1. **Install Dependencies**: Run `pip install -r requirements.txt` to install necessary packages.
2. **TMDB API Key**: Sign up at TMDB to get an API key. Create a `.env` file in the project root and add `TMDB_API_KEY=your_api_key_here`.
3. **Initialize Database**: Execute `python manage.py migrate` to set up the database.
4. **Start the Server**: Use `python manage.py runserver` and visit `http://localhost:8000` to access the app.

## Additional Information

I'm particularly proud of integrating the TMDB API, which enriches MovieClub with a vast array of movie data. This feature is central to the application's functionality, enabling users to explore an extensive movie database and interact based on shared interests.

### Note

To use MovieClub, ensure you have a `.env` file set with your TMDB API key (`TMDB_API_KEY=xy`). I will provide the API key separately for security reasons.

---

MovieClub is more than a project; it's a portal for movie lovers to explore, connect, and share their passion for cinema. It represents a blend of technology and entertainment, bringing people together in their love for movies.