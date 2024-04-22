#!/usr/bin/env python
# coding: utf-8

# In[8]:


html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Luxury Pickup Service</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f1f1f1;
        }

        .header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 20px 0;
        }

        .container {
            padding: 20px;
            max-width: 600px;
            margin: auto;
        }

        .image-container {
            text-align: center;
            margin-bottom: 20px;
        }

        .image-container img {
            max-width: 100%;
            height: auto;
        }

        .button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #333;
            color: #fff;
            text-align: center;
            text-decoration: none;
            border: none;
            border-radius: 5px;
            margin-bottom: 10px;
        }

        .button:hover {
            background-color: #555;
        }

        .qr-code {
            text-align: center;
            margin-top: 20px;
        }

        .qr-code img {
            max-width: 200px;
            height: auto;
        }

        .description {
            text-align: justify;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Luxury Pickup Service</h1>
    </div>
    <div class="container">
        <div class="description">
            <p>Welcome to Luxury Pickup Service, your premier choice for luxury transportation. Unlike traditional ride-sharing services, we offer a superior experience tailored to your needs. Our fleet of black cars ensures style, comfort, and reliability on every journey.</p>
            <p>Whether you need a ride to the airport, a corporate event, or a special occasion, our professional drivers are here to provide first-class service. We go beyond just transportation; we deliver an unforgettable experience that's worth every penny.</p>
        </div>
        <div class="image-container">
            <img src="https://limoservice.biz/wp-content/uploads/2018/09/Black-Car-Service-Boston-1.jpg" alt="Luxury Car">
            <img src="https://www.westchestercountylimo.com/wp-content/uploads/2022/04/hourly-as-directed.jpg" alt="Luxury Pickup">
        </div>
        <a href="https://zuojenneh5.wixsite.com/onestop" class="button">Visit Website</a>
        <a href="mailto:gruoup5@gmail.com" class="button">Sign Up</a>
        </div>
    </div>
</body>
</html>
"""

from IPython.display import HTML
HTML(html_code)

