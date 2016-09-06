import media
import fresh_tomatoes
toy_story = media.Movie("Toy Stories", "Life of living toys",
"http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
       "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )
avatar = media.Movie("Avatar","New world war","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")
the_gift =media.Movie("The Gift","Suspenseful movie whee a man keep giving gifts","https://upload.wikimedia.org/wikipedia/en/thumb/9/97/The_Gift_2015_Film_Poster1.png/440px-The_Gift_2015_Film_Poster1.png","https://www.youtube.com/watch?v=I3IiZU9JBuE")
now_you_see_me_2=media.Movie("Now you see me 2","Movie about magicians saving the world","https://upload.wikimedia.org/wikipedia/en/9/9a/Now_You_See_Me_2_poster.jpg","https://www.youtube.com/watch?v=JzZh8kJJwe4")
angry_bird=media.Movie("The Angry Birds Movie","Birds and angry emotions to save their eggs","https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png","https://www.youtube.com/watch?v=QRmKa7vvct4")
movies=[toy_story,avatar,the_gift,now_you_see_me_2,angry_bird]
fresh_tomatoes.open_movies_page(movies)
