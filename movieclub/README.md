# MovieClub

## Overview

With the endless possibilities of different streaming platforms, I often experience that my friends have to spend a lot of time to discuss, what are the movies that they have both seen.

My cs50w final project aims to solve this problem:
Leveraging the TMDB API, it allows users to discover movies, create a personal list, and compare that with others. 

### Note

To use MovieClub, ensure you have a `.env` file set with your TMDB API key (`TMDB_API_KEY=xy`).  I will share my API key in the comments when submitting the form for testing purposes.

## Distinctiveness and Complexity

### Distinctiveness

My project differentiates itself by enabling the users to interact with a movie database, compare their personal movie lists, and discover common interests with others.
Integrating a third party API seemed like a useful extension to the components of the previous problems solved on this course, having lots of practical applications in the future.
I also had to understand how the layers stack on top of each other, for example I don't have the API key on the client JS side, so I have to create a call to my Django backend, and pass the data onward between the TMDB API and my browser.

### Complexity

The application's complexity is rooted in several areas:

- **TMDB API Integration**: Fetches and displays live movie data, handling API requests and responses.
- **User Authentication**: Manages user sessions, sign-ups, logins, and profile management.
- **Responsive Design**: Ensures the site is accessible across various devices with different viewports, enhancing user experience.
- **Dynamic Content Management**: Allows users to add or remove movies from their lists and compare these lists with other users, requiring intricate backend logic and database management.

## Project Structure


- **`views.py`**: Defines the server-side logic, including endpoint definitions and interaction with the database.
- **`models.py`**: Outlines the data models for users and their movie lists.
- **`fetch_tmdb.py`**: Since fetching the movie objects is several lines of code, I moved the fetching functions into a separate py file.
- **`urls.py`**: Handling routing to the different views based on the URL schemas
- **`script.js`**: Handles client-side logic, including interactions with the TMDB API and dynamic layout updates.
- **`styles.css`**: Contains custom CSS for styling the application, and handling parts of the responsive design.


### Templates:
- **`layout.html`**: The base template for the application, defining the navigation menu and layout.
- **`list_display.html`**: Serves as list generator to display movies on several other pages when included, and their corresponding user actions.
- **`my_list.html`**: When logged in, displays the favorites
- **`users.html`**: Gives the unique selling point of the site: compare your movie list with other users.
- **`login.html, register.html`**: Serving the user management

## Project summary

### Key challenges
**Fetching TMDB API from the browser**

As mentioned in the overview, for security reasons I decided not to use the API key in the .js parts of the application. To solve this, I created a workflow to have all the fetch requests running through my Django backend instead.

**Handling own movie entities in sync with TMDB**

Since during "My List" I preferred not to obtain every movie information again from the TMDB API, I cloned all the relevant information to my own database, and use it as a reference. I also use their picture storage to display the posters, so I store the poster_path, and build the link based on that.

When there is no movie poster, I use a dummy one.

**Creating a responsive design**

I had to realize that settings proper css attributes and using bootstrap and flex alone will not solve having half as wide displays as viewports. For this, I had to combine different solutions to handle wide, medium, and narrow screens. I use smaller texts, reduce the movie overview, or even stop displaying it if there is no space, keeping the layout intact.

**Handling search results pagination**

When more pages of search results return from the TMDB API, not only the page number, but the query string itself has to be passed during requests for proper functionality.

## Running the Application

**Start the Server:** Use `python manage.py runserver` and visit `http://127.0.0.1:8000` to access the app.

**TMDB API Key**: Please note that signing up at TMDB is needed to get an API key.  
Create a `.env` file in the project root and add `TMDB_API_KEY=your_api_key_here`.  
I will share my API key in the comments when submitting the form.


## Further feature ideas

- **Series:** Add support for fetching and storing series information, possibly with selecting the last episode one saw for finetuning the comparison
- **Friends and following:** Friend and follow requests for easier browsing, notification when a friend adds something new to their list
- **Rating and comments:** Add own experiences and thoughts about a movie or a series