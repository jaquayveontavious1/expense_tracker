# Personal Expense Tracker

A Django-based web application to manage personal expenses securely and efficiently.

## Features

- **User Authentication**: Users can register, log in, and manage their expenses securely.
- **Expense Management**: Users can add, edit, and delete expense entries.
- **Expense Search**: Users can search through their expense records by categories or descriptions.
- **Expense Summary**: Provides a summary of expenses categorized by date, category, and description.

## Requirements

- Python 3.x
- Django 3.x or higher

## Setup Instructions

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker


2.**Create a Virtual Environment:**

```sh

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate

```
3.**Install Dependencies:**

    
    
    pip install -r requirements.txt
    

4.**Apply Migrations:**

```sh

python manage.py makemigrations
python manage.py migrate
```
5.**Create a Superuser:**

```sh
python manage.py createsuperuser
```
6.**Run the Development Server:**

```sh
python manage.py runserver
```
7.<h4>Access the Application:</h4>

Open your web browser and navigate to http://127.0.0.1:8000.

<h2>Project Structure</h2>
<ul>
<li><strong>'expenses/':</strong> Contains the main expense tracker application.</li>
<li><strong>'expenses/models.py':</strong> Defines the Expense model.</li>
<li><strong>'expenses/forms.py':</strong> Contains forms for user registration, login, and expense data entry.</li>
<li><strong>'expenses/views.py'</strong>: Handles the business logic with class-based views.</li>
<li><strong>'expenses/templates/expenses/':</strong> Contains HTML templates for the application.</li>
<li><strong>urls.py:</strong> Defines URL patterns for the application.</li>
<li><strong>settings.py:</strong> Contains project settings and configurations.</li>
</ul>
<h3>Models</h3>
<ul>
<li>User: Uses Django’s built-in User model for authentication.</li>
<li>Expense:
    <ul>
        <li>username: ForeignKey to User.</li>
        <li>amount: DecimalField to store the amount spent.</li>
        <li>date: DateField for the transaction date.</li>
        <li>category: CharField with choices for expense categories.</li>
        <li>description: TextField for a short description of the expense.</li>
    </ul>
</li>
</ul>
<h3>Forms</h3>
<ul>
<li><strong>User Registration Form:</strong> For user sign-up.</li>
<li><strong>User Login Form:</strong> For user login.</li>
<li><strong>Expense Form:</strong> For adding and editing expense entries.</li>
</ul>

<h3>Views</h3>
<ul>
<li><strong>ExpenseListView:</strong> Displays a list of expenses for the logged-in user.</li>
<li><strong>ExpenseCreateView:</strong> Allows users to create new expense entries.</li>
<li><strong>ExpenseUpdateView:</strong> Allows users to edit existing expense entries.</li>
<li><strong>ExpenseDeleteView:</strong> Allows users to delete expense entries.</li>
</ul>

<h3>Templates</h3>
<ul>
<li><strong>expense_list.html:</strong> Template for listing expenses.</li>
<li><strong>expense_form.html:</strong> Template for creating and editing expenses.</li>
<li><strong>expense_confirm_delete.html:</strong> Template for confirming expense deletion.</li>
</ul>
<h3>License</h3>
<p>This project is licensed under the MIT License.</p>
<h3>Contact</h3>
<p>For any queries or issues, please contact kanyingitiffany@gmail.com.</p>

