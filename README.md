# E-commerce Django Backend

Welcome to the E-commerce Django Backend repository! This backend server is built using Django REST Framework in Python.

## Project Overview

This project serves as the backend for the E-shop application. It provides endpoints for managing users, products, categories, orders, and more.

## Features

- User Management: CRUD operations for managing users.
- Product Catalog: CRUD operations for managing products, including descriptions, images, prices, and available quantity.
- Product Categories: CRUD operations for managing product categories.
- Wishlist: Endpoint for managing user wishlists.
- Shopping Cart: Endpoint for managing user shopping carts.
- Payment Gateway Integration: Integration with a payment gateway for secure online payments.
- Order Management: CRUD operations for managing orders, including order status tracking and order cancellation.
- User Authentication and Authorization: User registration, login, authentication, and authorization features.
- Responsive Design: Ensures compatibility with various devices and screen sizes.

## Getting Started

<details>
  <summary><strong>Click to expand</strong></summary>

  ### Prerequisites
  
  - Python and Django installed on your machine.
  - MySQL installed and configured.

  ### Installation

  1. Clone the repository:
     ```bash
     git clone https://github.com/hadeer-khaled/E-commerce-Django-Part.git
     ```

  2. Navigate to the project directory:
     ```bash
     cd E-commerce-Django-Part
     ```

  3. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

  ### Database Setup

  1. Make sure you have MySQL installed and running on your machine.
  2. Create a new MySQL database for the project.
  3. Configure the database settings in the `settings.py` file.

  ### Run the Application

  1. Apply migrations:
     ```bash
     python manage.py migrate
     ```

  2. Start the development server:
     ```bash
     python manage.py runserver
     ```

  3. The backend server will be running at [http://localhost:8000](http://localhost:8000).

  ### Running the Frontend

  To run the frontend application, please go to the [E-commerce React Frontend repository](https://github.com/hadeer-khaled/E-commerce-React-Part/) and follow the instructions in the README.

</details>

## License

This project is licensed under the GNU General Public License v3.0.

## Screenshots

- Products Page
  <br>
  ![Products Page](https://raw.githubusercontent.com/hadeer-khaled/E-commerce-Django-Part/main/assets/1-products.png)
  <br>

- Categories Page
  <br>
  ![Categories Page](https://raw.githubusercontent.com/hadeer-khaled/E-commerce-Django-Part/main/assets/2-categories.png)
  <br>

- Orders Page
  <br>
  ![Orders Page](https://raw.githubusercontent.com/hadeer-khaled/E-commerce-Django-Part/main/assets/3-orders.png)
  <br>

## Contact

For any inquiries, please contact us
