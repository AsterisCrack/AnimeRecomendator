# AnimeRecomendator
## Description
This python program recommends anime series by genre. The program will ask for any genre available and then will select the best animes in the datasheet with that genre.
Then, you can also ask for the description of the recommended series.
The program is an ETL based on pandas.

## Instructions:
First, download the required depencdencies by running pip install -r requirements.txt
To run the program, run python recomendador.py and make sure your console supports inputs during the program execution.
If you wish to mount a docker image based on this program a dockerfile is included in the repo. To mount it, run docker build . -t AnimeRecomendator
