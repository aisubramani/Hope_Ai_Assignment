-- NetFlix Database MySQL Assignment
-- Dr. Subramani

-- 1. List all users subscribed to the Premium plan:
SELECT name, email, plan 
FROM Users 
WHERE plan = 'Premium';

-- 2. Retrieve all movies in the Drama genre with a rating higher than 8.5:
SELECT Title, Genre, Rating 
FROM Movies 
WHERE genre = 'Drama' AND rating > 8.5;

-- 3. Find the average rating of all movies released after 2015:
SELECT AVG(rating) AS average_rating 
FROM Movies 
WHERE release_year > 2015;

-- 4. List the names of users who have watched the movie Stranger Things along with their completion percentage:
SELECT 
users.Name, 
Movies.Title,
WatchHistory.Completion_percentage
FROM users
join WatchHistory ON users.user_id= WatchHistory.user_id
Join movies USING(movie_id)
where movies.title = "Stranger Things";


-- 5. Find the name of the user(s) who rated a movie the highest among all reviews:
SELECT 
users.Name, 
reviews.Rating
FROM Users
JOIN reviews USING(user_id)
WHERE reviews.rating =(select MAX(rating) from reviews);

-- 6. Calculate the number of movies watched by each user and sort by the highest count:
SELECT 
Users.Name, COUNT(WatchHistory.watch_id) AS Movies_watched 
FROM Users
JOIN WatchHistory USING(user_id)
GROUP BY Users.user_id 
ORDER BY movies_watched DESC;

-- 7.List all movies watched by John Doe, including their genre, rating, and his completion percentage:
SELECT U.Name, M.Title, M.Genre, M.Rating, W.Completion_percentage 
FROM Movies M
JOIN WatchHistory W USING(movie_id)
JOIN Users U USING(user_id)
WHERE U.name = 'John Doe';

-- 8.Update the movie's rating for Stranger Things:
UPDATE Movies 
SET rating = 8.9 
WHERE title = 'Stranger Things';
select * from movies;

-- 9.Remove all reviews for movies with a rating below 4.0:
DELETE FROM reviews
WHERE rating < 4.0;
select * from reviews;

-- 10. Fetch all users who have reviewed a movie but have not watched it completely (completion percentage < 100):
SELECT U.name, M.title, R.review_text ,W.completion_percentage
FROM Users U
JOIN Reviews R USING(user_id)
JOIN Movies M USING(movie_id)
LEFT JOIN WatchHistory W USING(movie_id)
WHERE (W.completion_percentage IS NULL OR W.completion_percentage < 100);

-- 11. List all movies watched by John Doe along with their genre and his completion percentage:
SELECT M.title, M.genre, W.completion_percentage 
FROM Movies M
JOIN WatchHistory W ON M.movie_id = W.movie_id
JOIN Users U ON W.user_id = U.user_id
WHERE U.name = 'John Doe';

-- 12.Retrieve all users who have reviewed the movie Stranger Things, including their review text and rating:
SELECT U.name, M.title, R.review_text, R.rating 
FROM Users U
JOIN Reviews R ON U.user_id = R.user_id
JOIN Movies M ON R.movie_id = M.movie_id
WHERE M.title = 'Stranger Things';

-- 13. Fetch the watch history of all users, including their name, email, movie title, 
-- genre, watched date, and completion percentage:
SELECT U.name, U.email, M.title, M.genre, W.watched_date, W.completion_percentage 
FROM Users U
JOIN WatchHistory W ON U.user_id = W.user_id
JOIN Movies M ON W.movie_id = M.movie_id;

-- 14.List all movies along with the total number of reviews and average rating 
-- for each movie, including only movies with at least two reviews:
SELECT M.title, COUNT(R.review_id) AS total_reviews, AVG(R.rating) AS average_rating 
FROM Movies M
JOIN Reviews R ON M.movie_id = R.movie_id
GROUP BY M.movie_id
HAVING COUNT(R.review_id) >= 2;

