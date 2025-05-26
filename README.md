## Code-Challenge-Articles---without-SQLAlchemy

# Articles Management System

A simple Python project that manages authors, magazines, and articles using a SQLite database and raw SQL (no ORM).

---

## Features

- Create and manage **authors**, **magazines**, and **articles**
- Articles link authors and magazines
- Save and retrieve data from a SQLite database

---

## Project Structure

project/
├── lib/
│ ├── db/
│ │ ├── connection.py # DB connection
│ │ └── schema.sql # SQL schema (tables)
│ └── models/
│ ├── author.py # Author class (with bio)
│ ├── magazine.py # Magazine class
│ └── article.py # Article class
├── articles.db # SQLite database file
├── run.py # Script to test code
└── README.md # Project guide


---

## Setup

1. **Install Python 3**  
2. **Install dependencies** (optional, just `ipdb`):

   ```bash
   pip install ipdb
- Create the database and tables:

bash
Copy
Edit
sqlite3 articles.db < lib/db/schema.sql
Usage
- Run the example code in run.py:

bash
Copy
Edit
python run.py
This will:

Create an author, magazine, and article

Save them to the database

Retrieve and print them

Open an interactive debug session (ipdb)

# Debugging
The code uses ipdb for debugging.

When you see (Pdb), you can:

n → Next line

c → Continue

p variable → Print a variable

# Example Code
- In run.py:

python
Copy
Edit
from lib.models.author import Author

author1 = Author(name="John Doe", bio="A passionate writer")
author1.save()
- This creates an author and saves it to the database.

# Testing
- No automated tests yet, but you can manually test by:

- Running run.py

- Adding more test cases (e.g., multiple authors and articles)

- Querying the database directly with SQLite CLI or DB Browser