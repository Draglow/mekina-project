<h1>Carzone</h1>
    CarZone is a web-based platform designed to connect car buyers and sellers, 
    making the process of buying or selling a car hassle-free and convenient.

<h1>Features</h1>

 1. <h5>User Authentication:</h5> . Secure user registration and login system to ensure data privacy and security.
 2. <h5>Car Listings:</h5> . Browse through a wide range of car listings with detailed information including make, model, year, price, mileage, and more.
 3. <h5>Search and Filter:</h5> . Easily search for specific cars based on various criteria such as make, model, price range, etc.
 4. <h5>Seller Profiles:</h5> . View detailed profiles of car sellers, including their ratings and reviews from previous buyers.
 5. <h5>Messaging System:</h5> . Communicate directly with sellers to ask questions or negotiate deals.
 6. <h5>Admin Panel:</h5> . Admin dashboard to manage users, listings, and resolve disputes if any.

<h1>Technologies Used</h1>

 1. <h4>Frontend:</h4> HTML, CSS, JavaScript (React)
 2. <h5>Backend:</h5> Python (Django)
 3. <h5>Database:</h5> PostgreSQL
 4. <h5>Authentication:</h5> Django's built-in authentication system
 5. <h5>Other Tools:</h5> Git for version control

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










<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CarZone - Your Ultimate Destination for Car Shopping</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
        }

        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #007bff;
            margin-bottom: 20px;
        }

        .logo {
            display: block;
            margin: 0 auto;
            width: 200px;
        }

        .section {
            margin-bottom: 20px;
        }

        .feature {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .feature img {
            width: 50px;
            margin-right: 20px;
        }

        .feature h3 {
            font-size: 24px;
            color: #333;
            margin: 0;
        }

        p {
            color: #666;
        }

        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            font-size: 18px;
        }

        .button:hover {
            background-color: #0056b3;
        }

        .footer {
            text-align: center;
            margin-top: 20px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to CarZone</h1>
        <img src="carzone_logo.png" alt="CarZone Logo" class="logo">

        <div class="section">
            <div class="feature">
                <img src="sleek_interface.png" alt="Sleek Interface">
                <h3>Sleek Interface</h3>
            </div>
            <p>Our Django-powered platform offers a sleek and modern interface designed to enhance your browsing and shopping experience.</p>
        </div>

        <div class="section">
            <div class="feature">
                <img src="advanced_search.png" alt="Advanced Search">
                <h3>Advanced Search</h3>
            </div>
            <p>With powerful Django filters, finding your dream car is easier than ever. Search by make, model, year, price range, and more!</p>
        </div>

        <div class="section">
            <div class="feature">
                <img src="user_authentication.png" alt="User Authentication">
                <h3>User Authentication</h3>
            </div>
            <p>Secure user authentication system ensures your data stays safe while you browse, buy, or sell.</p>
        </div>

        <div class="section">
            <div class="feature">
                <img src="community_interaction.png" alt="Community Interaction">
                <h3>Community Interaction</h3>
            </div>
            <p>Engage with fellow car enthusiasts, share experiences, and gain insights from the vibrant CarZone community.</p>
        </div>

        <div class="section">
            <h2>Getting Started</h2>
            <p>Getting started with CarZone is easy:</p>
            <pre>
git clone https://github.com/yourusername/carzone.git
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
            </pre>
            <a href="#" class="button">Join Now</a>
        </div>
    </div>

    <div class="footer">
        <p>&copy; 2024 CarZone. All rights reserved.</p>
    </div>
</body>
</html>

