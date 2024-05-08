from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Explicitly get the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("OpenAI API key not found. Make sure to set it in the .env file.")

client = OpenAI(api_key=api_key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommendation", methods=["POST"])
def get_recommendation():
    user_input = request.form["user_input"]
    print("User input:", user_input)


    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": user_input,
            }
        ],
        model="gpt-3.5-turbo",
    )

    chat_message = chat_completion.choices[0].message.content
    recommendation = f"{chat_message}"

    return render_template("recommendation.html", recommendation=recommendation)

@app.route("/genre/<genre>")
def genre_page(genre):
    # Prompt for OpenAI API to generate book recommendations
    if genre.lower() == "art":
        prompt = f"Please provide a list of popular books about visual arts, including topics such as painting, sculpture, art history, and art techniques in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "biography":
        prompt = f"Please provide a list of popular biographies and memoirs in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "business":
        prompt = f"Please provide a list of popular books on business, management, and entrepreneurship in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "children's":
        prompt = f"Please provide a list of popular children's books in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "christian":
        prompt = f"Please provide a list of popular Christian books, including fiction and non-fiction, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "classics":
        prompt = f"Please provide a list of popular classic books, including literary classics and timeless novels, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "comics":
        prompt = f"Please provide a list of popular comic books and graphic novels in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "cookbooks":
        prompt = f"Please provide a list of popular cookbooks and recipe books in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "ebooks":
        prompt = f"Please provide a list of popular ebooks across various genres with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "fantasy":
        prompt = f"Please provide a list of popular fantasy books, including epic fantasy, urban fantasy, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "fiction":
        prompt = f"Please provide a list of popular fiction books across various sub-genres (literary fiction, contemporary fiction, etc.) in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "graphic novels":
        prompt = f"Please provide a list of popular graphic novels in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "historical fiction":
        prompt = f"Please provide a list of popular historical fiction books in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "history":
        prompt = f"Please provide a list of popular history books, including biographies, historical accounts, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "horror":
        prompt = f"Please provide a list of popular horror books, including supernatural, psychological horror, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "memoir":
        prompt = f"Please provide a list of popular memoirs and autobiographies in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "music":
        prompt = f"Please provide a list of popular books about music, including biographies, histories, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "mystery":
        prompt = f"Please provide a list of popular mystery books, including detective fiction, crime thrillers, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "nonfiction":
        prompt = f"Please provide a list of popular non-fiction books across various topics (science, history, self-help, etc.) in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "poetry":
        prompt = f"Please provide a list of popular poetry books and collections in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "psychology":
        prompt = f"Please provide a list of popular books on psychology, mental health, and human behavior in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "romance":
        prompt = f"Please provide a list of popular romance books, including contemporary romance, historical romance, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "science":
        prompt = f"Please provide a list of popular science books, including physics, biology, chemistry, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "science fiction":
        prompt = f"Please provide a list of popular science fiction books, including space opera, cyberpunk, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "self help":
        prompt = f"Please provide a list of popular self-help books on personal development, productivity, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "sports":
        prompt = f"Please provide a list of popular books on sports, including biographies, histories, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "thriller":
        prompt = f"Please provide a list of popular thriller books, including psychological thrillers, suspense novels, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "travel":
        prompt = f"Please provide a list of popular travel books, including guidebooks, travelogues, and more, in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    elif genre.lower() == "young adult":
        prompt = f"Please provide a list of popular young adult books across various sub-genres (fantasy, contemporary, etc.) in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."
    else:
        prompt = f"Please provide a list of popular books in the {genre} genre with author and release date and a short description of the book, in a total of 10 books."

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "assistant",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    chat_response = chat_completion.choices[0].message.content
    book_recommendations = parse_chat_response(chat_response)
    
    return render_template("genre.html", genre=genre, books=book_recommendations)

def parse_chat_response(response):
    # Split the response into individual lines
    lines = response.strip().split('\n')

    # Extract book information from each line
    books = []
    for line in lines:
        # Remove any leading/trailing whitespace
        line = line.strip()

        # Split the line into parts
        parts = line.split(" - ", 1)
        if len(parts) == 2:
            book_info_part, description = parts

            # Split the book info part by " by "
            book_info_parts = book_info_part.split(" by ")
            if len(book_info_parts) == 2:
                title, author_and_date = book_info_parts

                # Split author and release date
                author, release_date = author_and_date.split(" (")
                release_date = release_date.strip(")")

                # Create a dictionary for the book information
                book_info = {
                    "title": title,
                    "author": author,
                    "release_date": release_date,
                    "description": description.strip()
                }
                books.append(book_info)

    return books


# Add this line to serve static files
app.static_folder = 'static'
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ == "__main__":
    app.run(debug=True)