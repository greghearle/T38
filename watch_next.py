import spacy
nlp = spacy.load('en_core_web_md')
'''
load_movies reads through movies.txt (or other; takes filename as argument).
Populates a list called movie_list, which can be used for the watch_next function.
'''
def load_movies(file):
    movie_list = []
    with open(file, "r") as f:
        for line in f:
            movie_desc = line.strip("\n") # strips line breaks
            movie_list.append(movie_desc) # adds each line of the text file to a list
    return movie_list

'''
watch_next takes a description of the watched film, and the list returned by load_movies as arguments

'''

def watch_next(description,list):
    seen_film = input("Have you watched 'Planet Hulk?'").upper() # checks whether user has seen film
    if seen_film == "YES": 
        most_similar = 0 # variable to track most suitable film to watch next
        for movie in list:
            movie_description = nlp(movie[9:]) # [9:0] extracts the description only from each line
            similarity_score = description.similarity(movie_description) # calculates similarity of given description with each description in text file
            if similarity_score > most_similar:
                most_similar = similarity_score # updates most_similar if it's the highest score so far
                suggested_movie = movie[0:8] # [0:8] extracts the movie name only from each line
        print(f"Your suggested next movie is: {suggested_movie}")
    elif seen_film == "NO":
        print("No matching data for suggestions- please see a list of films below")
        for film in list: # prints all films+descriptions in case that user hasn't seen Planet Hulk
            print(film)
    else:
        print("Input not recognised; please try again")

description = nlp('Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.')
movie_list = load_movies("movies.txt")
watch_next(description, movie_list)