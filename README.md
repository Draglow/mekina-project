<h1>Carzone</h1>
    CarZone is a web-based platform designed to connect car buyers and sellers, 
    making the process of buying or selling a car hassle-free and convenient.

<h1>Features</h1>

 <h3> 1. User Authentication:</h3> . Secure user registration and login system to ensure data privacy and security.
 <h5> 2. Car Listings:</h5> . Browse through a wide range of car listings with detailed information including make, model, year, price, mileage, and more.
 <h5> 3. Search and Filter:</h5> . Easily search for specific cars based on various criteria such as make, model, price range, etc.
 <h5> 4. Seller Profiles:</h5> . View detailed profiles of car sellers, including their ratings and reviews from previous buyers.
 <h5> 5. Messaging System:</h5> . Communicate directly with sellers to ask questions or negotiate deals.
 <h5> 6. Admin Panel:</h5> . Admin dashboard to manage users, listings, and resolve disputes if any.

<h1>Technologies Used</h1>

  <h4> 1. Frontend:</h4> HTML, CSS, JavaScript (React)
  <h5> 2. Backend:</h5> Python (Django)
  <h5> 3. Database:</h5> PostgreSQL
  <h5> 4. Authentication:</h5> Django's built-in authentication system
  <h5> 5. Other Tools:</h5> Git for version control

<h1>Installation</h1>

1. Clone the repository:
 git clone https://github.com/Draglow/carspace-project.git
 
2. Navigate to the project directory:
 cd carspace

3. Install dependencies:
 pip install -r requirements.txt
 
4. Set up environment variables:
  Create a .env file in the root directory.
  Define environment variables such as DATABASE_URL, SECRET_KEY, etc.

6. Run migrations:
  python manage.py migrate
  
7. Create a superuser (admin account):
 python manage.py createsuperuser

8. Run the development server:
  python manage.py runserver
  Open your browser and navigate to http://localhost:8000 to view the application.










