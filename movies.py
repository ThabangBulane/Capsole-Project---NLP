import spacy

nlp = spacy.load('en_core_web_md')
from spacy.lang.en import English

moviesList = {}
m = open("movies.txt", "r")
cnt = 0
watchedMovieName = "Planet Hulk"
watchedMovieDesc = "Will he save their world or destroy it? When the Hulk "
"becomes too dangerous for the Earth, The Illuminati trick Hulk into a shuttle"
" and launch him into space to a planet where the Hulk can live in peace."
" Unfortunately, Hulk land on the planet Sakaar where he is sold into salvery"
" and trained as a gladiator"
highestSim = 0
RecomMovie = ""


def RecMovies(watchedMovieDesc):
    print("Recommended Movie : ")
    for line in m:
        t, k = line.split(":", 1)
        moviesList[cnt] = {t: k}
        cnt = cnt + 1
        Sim = watchedMovieDesc.similarity(k)
        if Sim > highest:
            highest = Sim
            RecomMovie = t
    return RecomMovie


# When i try to run the code it gives me an error(ModuleNotFoundError: No module named 'spacy') STILL
# so i could answer answer the question because of that.

