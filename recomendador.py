import pandas as pd
import re

def extract():
    df = pd.read_csv('anime.csv')
    return df

def transform(df):
    #Quitamos las columnas que no queremos
    df = df.drop(['anime_id', 'type', 'scored_by', 'status', 'episodes', 'start_date', 'end_date', 'source', 'members', 'favorites', 'episode_duration', 'total_duration', 'rating', 'sfw', 'approved', 'created_at', 'updated_at', 'start_year', 'start_season', 'real_start_date', 'real_end_date', 'broadcast_day', 'broadcast_time', 'themes', 'demographics', 'studios', 'producers', 'licensors', 'background', 'main_picture', 'url', 'trailer_url', 'title_english', 'title_japanese', 'title_synonyms'], axis=1)

    #Obtenemos todos los géneros que existen
    all_available_genres = df['genres'].unique()
    for i in range(len(all_available_genres)):
        all_available_genres[i] = re.sub(r'\[|\]|\'', '', all_available_genres[i]).split(", ")

    all_available_genres_res=[]
    for i in all_available_genres:
        all_available_genres_res.extend(i)
    
    list_of_unique_genres = []
    unique_genres = set(all_available_genres_res)
    for genre in unique_genres:
        if genre != '':
            list_of_unique_genres.append(genre)

    list_of_unique_genres.sort()

    #Obtenemos el género que se quiere buscar
    ok = False
    while ok == False:
        entrada = input("Would you like to see what genres are available? (y/n):\n")
        #create regex based on entrada that ignores case
        regex = re.compile(entrada, re.IGNORECASE)
        if regex.match("y"):
            print(list_of_unique_genres)
            ok = True
        elif regex.match("n"):
            ok = True
        else:
            print("Please enter a valid option")
    
    ok = False
    while ok == False:
        entrada = input("Please enter the genre you want to search:\n")
        #create regex based on entrada that ignores case
        regex = re.compile(entrada, re.IGNORECASE)
        if list(filter(regex.match, list_of_unique_genres)) != []:
            ok = True
        else:
            print("Please enter a valid genre")
    
    #Limpiamos la regex para que no de problemas a la hora de buscar en el dataframe
    filtered_genres = filter(regex.match, all_available_genres_res)
    filtered_genres = list(filtered_genres)
    genre = filtered_genres[0]

    #Obtenemos un nuevo dataframe sólo con las series que tienen el género que buscamos
    processed_df = df[df['genres'].str.contains(genre)]
    processed_df = processed_df.sort_values(by=['score'], ascending=False)
    return processed_df

def load(data):
    print("Recommending the 10 best anime for you:\n")
    #Imprimimos los 10 primeros de la forma -> Nombre de la serie (score)
    for i in range(10):
        print(str(i+1) + ".", data.iloc[i]['title'], "(", data.iloc[i]['score'], ")")
    
    ok = False
    while ok == False:
        entrada = input("Would you like to see the description of any anime? (1 to 10, or EXIT to exit app):\n")
        #Convert entrada to a valid number from 1 to 10 if possible
        try:
            entrada = int(entrada.replace(" ", ""))
            if entrada > 0 and entrada < 11:
                print(data.iloc[entrada-1]['title'], ":\n", data.iloc[entrada-1]['synopsis'],"\n")
        except:
            #regex to check if entrada is exit
            regex = re.compile(entrada, re.IGNORECASE)
            if regex.match("exit"):
                ok = True
            else:
                print("Please enter a valid option")
        
if __name__ == '__main__':
    df = extract()
    data = transform(df)
    load(data)