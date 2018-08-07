# -*- coding: utf-8 -*-

import media
import xlrd
import fresh_tomatoes as ft
import io

def get_movies_from_excel(filename):
    """
    Get list of favorite movies from csv format file.
    You can modify the csv format file like favorite_movies.csv
    to add or delete the information of movies.
    
    Args:
        filename: The file name of excel format file
    
    return:
        movies_list: A list of favorite movies
    """

    movies_list=[]
    excel = xlrd.open_workbook(filename) # open the xls file
    table = excel.sheets()[0] # open the first table in the sheet
    nrows = table.nrows      # get the total row number of the sheet

    for row in range(nrows):
        if row != 0: # remove the first row(the title of each column)
            #print(table.row_values(row)[2])
            movie = media.Movie(table.row_values(row)[0],table.row_values(row)[4],table.row_values(row)[5],table.row_values(row)[1],table.row_values(row)[2],table.row_values(row)[3],table.row_values(row)[6])
            movies_list.append(movie)
    return movies_list	

if __name__ == '__main__': 
	movies = get_movies_from_excel("favorite_movies.xls")
	ft.open_movies_page(movies)


#toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
#	"http://","")

#avatar = media.Movie("Avatar","A marine on an alien planet","http://","http://")

#print (toy_story.storyline)	
#avatar.show_trailer()
