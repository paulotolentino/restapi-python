# Readme.md - Python Project with Flask and SQLite

This is an example of a Python project that uses the Flask framework to create a web API and SQLite as the database. This project provides a simple API for managing user information.

## Prerequisites

Before running this project, make sure you have Python and the following libraries installed:

- Flask: Used to create the web application.
- Flask-RESTful: An extension of Flask that simplifies the creation of RESTful APIs.
- SQLAlchemy: Used to interact with the SQLite database.
- SQLite: A lightweight, embedded database used to store user data.

You can install the dependencies using pip:

```bash
pip install flask flask-jsonpify flask-sqlalchemy flask-restful
```

## Project Structure

The project consists of a single Python file, but it's important to understand the structure of the classes and methods:

- `app.py`: The main file that contains the Flask application and the definition of API routes.

The classes and methods included in the `app.py` file are:

- `Users`: A class that handles operations related to users, such as listing all users (`GET`), creating a new user (`POST`), and updating an existing user (`PUT`).

- `UserById`: A class that handles operations for a specific user, such as retrieving user information by their ID (`GET`) and deleting a user by ID (`DELETE`).

## Usage

To run the project, you can simply execute the `app.py` file. Make sure you're in the directory where the file is located and run the following command:

```bash
python app.py
```

This will start the Flask application server, which will be available at http://localhost:5000/.

The API has the following routes:

- `GET /users`: Returns the list of all users.
- `POST /users`: Creates a new user.
- `PUT /users`: Updates the details of an existing user.
- `GET /users/<id>`: Retrieves information about a user by their ID.
- `DELETE /users/<id>`: Deletes a user by their ID.

Be sure to use an API client, such as Postman, to test the API operations.

## Database

This project uses SQLite as the database. The database file (`exemplo.db`) will be created automatically when the application is run for the first time. Ensure that the `exemplo.db` file is in the same directory as the `app.py` file.

## Contribution

Feel free to contribute to this project by reporting issues, providing improvements, or adding additional features. The project is open-source, and you can fork the repository and submit pull requests.

## License

This project is under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the LICENSE file for more details.
