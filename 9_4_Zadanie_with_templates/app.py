from flask import Flask, request, render_template, redirect, url_for

from forms import BookForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

books = [
    {
        "title": "From Here to Eternity",
        "author": "James Jones",
        "description": "The debut novel of American author James Jones, published by Scribner's in 1951. Set in 1941, the novel focuses on several members of a U.S. Army infantry company stationed in Hawaii in the months leading up to the Japanese attack on Pearl Harbor",
        "num_pages": 861,
        "read": True
    },
    {
        "title": "Look Homeward Angel",
        "author": "Thomas Wolfe",
        "description": "It is a 1929 novel by Thomas Wolfe. It is Wolfe's first novel, and is considered a highly autobiographical American coming-of-age story. The character of Eugene Gant is generally believed to be a depiction of Wolfe himself. The novel briefly recounts Eugene's father's early life, but primarily covers the span of time from Eugene's birth in 1900 to his definitive departure from home at the age of 19. The setting is a fictionalization of his home town of Asheville, North Carolina, called Altamont in the novel.",
        "num_pages": 544,
        "read": True 
    },
    {
        "title": "Absalom, Absalom!",
        "author": "William Faulkner",
        "description": "It is a novel by the American author William Faulkner, first published in 1936. Taking place before, during, and after the American Civil War, it is a story about three families of the American South, with a focus on the life of Thomas Sutpen.",
        "num_pages": 384,
        "read": True 
    },
    {
        "title": "Of Mice and Men",
        "author": "John Steinbeck",
        "description": "It is a 1937 novella written by American author John Steinbeck. It narrates the experiences of George Milton and Lennie Small, two displaced migrant ranch workers, who move from place to place in California in search of new job opportunities during the Great Depression in the United States.",
        "num_pages": 107,
        "read": False 
    },
    {
        "title": "Islands in the Stream",
        "author": "Ernest Hemingway",
        "description": "It is the first of the posthumously published novels of Ernest Hemingway. The book was originally intended to revive Hemingway's reputation after the negative reviews of Across the River and Into the Trees. He began writing it in 1950 and advanced greatly through 1951.",
        "num_pages": 448,
        "read": False  
    }
]

@app.route("/books/", methods=["GET", "POST"])
def books_list():
    form = BookForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            books.save_all()
        return redirect(url_for("books_list"))
    
    return render_template("books.html", form=form, books=books.all(), error=error)

@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)
