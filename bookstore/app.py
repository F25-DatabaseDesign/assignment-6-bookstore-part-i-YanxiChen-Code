from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

categories = [
    {"id": 1, "name": "Detective", "image": "detective.jpg"},
    {"id": 2, "name": "Mystery",   "image": "mystery.jpg"},
    {"id": 3, "name": "SciFi",     "image": "scifi.jpg"},
    {"id": 4, "name": "Textbooks", "image": "textbooks.jpg"},
]
# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

books = [
    # Detective
    {"id": 1,  "categoryId": 1, "title": "The Hound of the Baskervilles", "author": "Arthur Conan Doyle",
     "isbn": "9780451528018", "price": 10.99, "image": "hound_baskervilles.jpg", "readNow": True},
    {"id": 2,  "categoryId": 1, "title": "The Maltese Falcon", "author": "Dashiell Hammett",
     "isbn": "9780679722649", "price": 12.50, "image": "maltese_falcon.jpg", "readNow": False},
    {"id": 3,  "categoryId": 1, "title": "The Big Sleep", "author": "Raymond Chandler",
     "isbn": "9780394758282", "price": 11.75, "image": "big_sleep.jpg", "readNow": True},
    {"id": 4,  "categoryId": 1, "title": "Murder on the Orient Express", "author": "Agatha Christie",
     "isbn": "9780062693662", "price": 9.99, "image": "orient_express.jpg", "readNow": False},

    # Mystery
    {"id": 5,  "categoryId": 2, "title": "Gone Girl", "author": "Gillian Flynn",
     "isbn": "9780307588371", "price": 14.50, "image": "gone_girl.jpg", "readNow": True},
    {"id": 6,  "categoryId": 2, "title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson",
     "isbn": "9780307454546", "price": 15.00, "image": "dragon_tattoo.jpg", "readNow": False},
    {"id": 7,  "categoryId": 2, "title": "And Then There Were None", "author": "Agatha Christie",
     "isbn": "9780062073488", "price": 8.99, "image": "and_then_none.jpg", "readNow": True},
    {"id": 8,  "categoryId": 2, "title": "The Da Vinci Code", "author": "Dan Brown",
     "isbn": "9780307474278", "price": 12.99, "image": "da_vinci_code.jpg", "readNow": False},

    # Sci-Fi
    {"id": 9,  "categoryId": 3, "title": "Dune", "author": "Frank Herbert",
     "isbn": "9780441013593", "price": 18.99, "image": "dune.jpg", "readNow": True},
    {"id": 10, "categoryId": 3, "title": "Neuromancer", "author": "William Gibson",
     "isbn": "9780441569595", "price": 11.50, "image": "neuromancer.jpg", "readNow": False},
    {"id": 11, "categoryId": 3, "title": "Ender's Game", "author": "Orson Scott Card",
     "isbn": "9780812550702", "price": 9.99, "image": "enders_game.jpg", "readNow": True},
    {"id": 12, "categoryId": 3, "title": "Foundation", "author": "Isaac Asimov",
     "isbn": "9780553293357", "price": 8.50, "image": "foundation.jpg", "readNow": False},

    # Textbooks
    {"id": 13, "categoryId": 4, "title": "Introduction to Algorithms (CLRS)", "author": "Cormen, Leiserson, Rivest, Stein",
     "isbn": "9780262046305", "price": 89.99, "image": "clrs.jpg", "readNow": False},
    {"id": 14, "categoryId": 4, "title": "Campbell Biology", "author": "Reece et al.",
     "isbn": "9780134093413", "price": 79.50, "image": "campbell_biology.jpg", "readNow": True},
    {"id": 15, "categoryId": 4, "title": "Organic Chemistry", "author": "Wade",
     "isbn": "9780134161600", "price": 65.00, "image": "orgo_wade.jpg", "readNow": False},
    {"id": 16, "categoryId": 4, "title": "Calculus", "author": "James Stewart",
     "isbn": "9781285740621", "price": 59.99, "image": "stewart_calculus.jpg", "readNow": True},
]


# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template('index.html', categories=categories)

@app.route('/category/<int:category_id>')
def category(category_id):
    
    # Store the categoryId passed as a URL parameter into a variable

    # Create a new list called selected_books containing a list of books that have the selected category

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    selected = next((c for c in categories if c["id"] == category_id), None)
    if not selected:
        abort(404)

    selected_books = [b for b in books if b["categoryId"] == category_id]

    return render_template(
        'category.html',
        categories=categories,
        books=selected_books,
        selectedCategoryId=category_id
    )

@app.route('/search')
def search():
    #Link to the search results page.

    query = request.args.get('q', '').strip()
    results = []
    if query:
        q_lower = query.lower()
        for b in books:
            if q_lower in b['title'].lower() or q_lower in b['author'].lower() or q_lower in b['isbn'].lower():
                results.append(b)
    return render_template('search.html', categories=categories, query=query, results=results)


@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
