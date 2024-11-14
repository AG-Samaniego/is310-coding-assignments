# Assignment Objectives

# Import Rich library & create console instance
from rich.console import Console
from rich.table import Table
import os


console = Console()
console.print("Hello!")


# Show user pre-created sample data using Rich
# Can use Table class, OR use console.print function

table = Table(title="Favorite Music Albums")
table.add_column("Favorite Album", style="cyan", no_wrap=True)
table.add_column("Artist Name", style="magenta")
table.add_column("Year of Release", justify="right")
table.add_row("Wasteland, Baby", "Hozier", "2019")
table.add_row("Melodrama", "Lorde", "2018")
table.add_row("Chromakopia", "Tyler the Creator", "2024")
table.add_row("To Pimp a Butterfly", "Kendrick Lamar", "2015")


fav_albums = [
    {
        "Album Name": "Wasteland, Baby",
        "Artist Name": "Hozier",
        "Year of Release": "2019"
    },
    {
        "Album Name": "Melodrama",
        "Artist Name": "Lorde",
        "Year of Release": "2018"
    },
    {
        "Album Name": "Chromakopia",
        "Artist Name": "Tyler the Creator",
        "Year of Release": "2024"
    },
    {
        "Album Name": "To Pimp a Butterfly",
        "Artist Name": "Kendrick Lamar",
        "Year of Release": "2015"
    }
]

# Gathering data from user
"""Use <input> function to ask user to enter data for each field
You could also use Rich's input method"""


console.print('\n[bold cyan] Welcome! I am making a collection of favorite albums. Please enter your favorite music album! [/bold cyan]')
while Console() == True:
    console.print(table)
    album = input('Enter your favorite song album: ')
    
    artistname = input('Enter the name of the artist who created the album: ')
    releaseyr = input('Now enter the year that the album was released: ')


# looping thru album list
for albums in fav_albums:
    console.print("\n[bold cyan]Checking album information: [/bold cyan]")
    for field, value in albums.items():
        console.print(f"[magenta]{field}[/magenta]: {value}")
    
