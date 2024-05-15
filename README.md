CarZone: Online Car Market
  Welcome to CarZone, your ultimate destination for buying and selling cars online.
  CarZone is a web-based platform designed to connect car buyers and sellers, 
  making the process of buying or selling a car hassle-free and convenient.

Features
. User Authentication: Secure user registration and login system to ensure data privacy and security.
. Car Listings: Browse through a wide range of car listings with detailed information including make, model, year, price, mileage, and more.
. Search and Filter: Easily search for specific cars based on various criteria such as make, model, price range, etc.
. Seller Profiles: View detailed profiles of car sellers, including their ratings and reviews from previous buyers.
. Messaging System: Communicate directly with sellers to ask questions or negotiate deals.
. Admin Panel: Admin dashboard to manage users, listings, and resolve disputes if any.

Technologies Used
. Frontend: HTML, CSS, JavaScript (React)
. Backend: Python (Django)
. Database: PostgreSQL
. Authentication: Django's built-in authentication system
. Other Tools: Git for version control

Installation
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
