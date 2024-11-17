# Mini Message App (Django)

This is a web-based instant messaging app, similar to Messenger, developed with **Python** and **Django**. It allows secure communication between users through private messages and offers a blog-like section where users can post content that is accessible to others.

## Features

- **User Authentication**: Users can create accounts and authenticate their sessions via a login system.
- **Private Messages**: Users can send messages to each other securely. Only users involved in a conversation can access its messages.
- **Security**: Access control is implemented to ensure that no one can view a conversation thread unless they are a participant.
- **Blog Posts**: Users can create blog-like posts, and other users can interact with them.
- **Simple and Functional Interface**: The interface is built with **Bootstrap** and designed for ease of use, allowing users to send messages, publish blog posts, and navigate through the app efficiently.

## Technologies Used

- **Python 3.10**
- **Django 5.1**
- **Pillow 10.4.0**
- **django-ckeditor 6.7.1**
- **Bootstrap**
- **JavaScript**
- **SQLite**

## Installation

### Prerequisites

1. Make sure **Python 3.10** is installed on your machine.
2. Make sure **pip** is installed (it typically comes with Python).
3. Have access to a command-line terminal.

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/SntgRM/web-playground.git
    cd web-playground
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Linux/macOS
    env\Scripts\activate  # On Windows
    ```

3. Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to manage the app (optional):
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/` to see the app in action.

Additionally, the app is deployed online. You can access the production version from the link available in the repository description.

## Using the Application

### Registration and Login

1. To get started, create an account in the **Registration** section.
2. Once registered, log in with your credentials.

### Sending and Receiving Messages

- Go to the **Messages** section.
- You can select another user from your contacts list or search for someone by their username.
- The messages you send will be securely stored in the database and only be accessible by the users participating in the conversation.
- To view a conversation thread, both users must be participants in it. It is not possible to access conversations you are not a part of.

### Blog Posts

- In the **Blog** section, users can create public posts.
- Users can comment and respond to posts, fostering interaction and content creation within the community.
- The text editor is implemented using **django-ckeditor**, providing a rich interface to write and format content.

### Security

- Access control is implemented in the messaging system to ensure that only participants of a conversation can access its contents.
- It is not possible to access a conversation thread via a direct link if you are not one of the users involved in that thread.

