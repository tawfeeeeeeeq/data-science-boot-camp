import os                               # importing os - to help find the file path to open the movies.txt file
import spacy                            # importing spacy
nlp = spacy.load('en_core_web_md')      # loading the language model

"""
This function takes in the description of a movie the user has watched.
Using spacy we compare it with a list of movies and score the `Semantic Similarity`.
The movie that has the highest `Semantic Similarity` score will be returned by the function.
"""
def movie_recommendation(desc):
    # Open the `movies.txt` file, read the contents into a list, then close the file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "movies.txt")
    file = open(file_path, "r")
    movies = file.readlines()
    file.close()

    # initialising some variables to be used within the for loop below
    recommendation = ""
    score = 0
    model_movie = nlp(desc)

    # Loop through movies list that we created from each line of the movies.txt file
    for movie in movies:
        # Seperate the MovieID, and the MovieDesc into their own variables
        movie_info = movie.split(" :")
        movie_id = movie_info[0]
        movie_desc = movie_info[1]

        # Compare this movie desc with the one supplied by the user, and save the score in variable `similarity`
        similarity = nlp(movie_desc).similarity(model_movie)
        # If this movie has a higher simlarity than the previous movie we have compared then, then save the details
        # If Not, then ignore, and try the next movie in the list
        if similarity > score:
            score = similarity
            recommendation = movie_id
        
        # This below was used for debugging
        # print(movie_id, similarity, movie_desc)

    # After looping through all the movies, return the MovieID with the highest `Semantic Similarity`
    return recommendation
"""-------------------------------------------------------------------------------------------"""


# These are the details of a movie already watched
movie_name = "Planet Hulk"
movie_desc = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# This calls the function above, supplying the already watched movie description, a recommendation is returned
recommendation = movie_recommendation(movie_desc)
# Print the recommendation
print("After watching `", movie_name, "` , we recommend `", recommendation, "`")
