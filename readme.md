# Flask MongoDB Atlas Assignment

## Project Description
This project is a Flask-based web application that provides a REST API and a frontend form.
The API reads data from a backend JSON file and returns it as a JSON response.
The form collects user input and stores the data in MongoDB Atlas using PyMongo.

---

## Features
- Flask REST API (`/api`) returning JSON data
- Frontend form for user input
- MongoDB Atlas integration using PyMongo
- Success redirection and error handling

---

## Technologies Used
- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML
- JSON

---

## Project Structure
flask-mongo-assignment/
│
├── app.py
├── data.json
├── requirements.txt
├── .env
├── templates/
│ ├── form.html
│ └── success.html
└── README.md

yaml
Copy code

---

## Setup Instructions

### 1. Install Dependencies
```bash
pip install flask pymongo dnspython python-dotenv
2. Configure MongoDB Connection
Create a .env file:

ini
Copy code
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
3. Run the Application
bash
Copy code
python app.py
Usage
API Endpoint: http://127.0.0.1:5000/api

Form Page: http://127.0.0.1:5000/

Output
JSON data returned from backend file

Form data successfully stored in MongoDB Atlas
