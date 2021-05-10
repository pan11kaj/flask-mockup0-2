from flask import Flask
import csv;

with open("movies.csv",encoding='utf8' ) as file:
    reader = csv.reader(file)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
headers.append("poster_link")


with open('final.csv','a+',encoding='utf8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)

with open('movie_links.csv',encoding='utf8') as f:
    read = csv.reader(f)
    data = list(read)
    all_movie_links = data[1:]

for movie_item in all_movies:
    poster_count = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_count:
        for movie_link_item in all_movie_links:
            if movie_item[8] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 28:
                    with open("final.csv","a+",encoding='utf8') as f:
                        writer = csv.writer(f)
                        writer.writerow(movie_item)
