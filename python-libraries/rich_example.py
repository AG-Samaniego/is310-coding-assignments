from rich.console import Console
from rich.table import Table 

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")

console = Console()

"""table = Table(title="Star Wars Movies")
table.add_column("Released", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right")
table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393151347")
table.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")"""

# Movie data stored in dictionaries
movies = [ 
    {
        "Released": "Dec 20, 2019",
        "Title": "Star Wars: The Rise of Skywalker",
        "Box Office": "$952,110,690"
    },
    {
        "Released": "May 25, 2018",
        "Title": "Solo: A Star Wars Story",
        "Box Office": "$393,151,347"
    },
    {
        "Released": "Dec 15, 2017",
        "Title": "Star Wars Ep. VIII: The Last Jedi",
        "Box Office": "$1,332,539,889"
    },
    {
        "Released": "Dec 16, 2016",
        "Title": "Rogue One: A Star Wars Story",
        "Box Office": "$1,332,439,889"
    }
]

#For-loop to loop thru movies
for movie in movies: 
    console.print("\n[bold cyan]Review movie information [/bold cyan]")
    for field, value in movie.items():
        console.print(f"[magenta]{field}[/magenta]: {value}")