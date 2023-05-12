
# Django E-Commerce App

This repository contains a fully functional e-commerce web application built using Django. The application provides a seamless user experience, allowing users to browse products, add items to their cart, and complete the checkout process. Users can also sign up, log in, and view their orders. The app utilizes Django views, models, and middlewares to achieve a professional and efficient performance.

## Features
- Product listing and details
- User registration and authentication
- Shopping cart management
- Checkout process
- Order history

## Installation

 ### 1. Clone the repository or download the project files.


```bash
git clone https://github.com/Swastikdan/E-Commerce-Django.git

```
 ### 2. Navigate to the project directory.
```bash
cd E-Commerce-Django

```
### 3. Install the required dependencies.
```bash
pip install -r requirements.txt

```

### 4. Install the required dependencies for Tailwind:

   ```
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   npm install flowbite
   npm install @tailwindcss/forms
   npm install @tailwindcss/aspect-ratio
   ```

### 5. Initialize Tailwind CSS by running `npx tailwindcss init`.

## Running the Project

### 1. Run the migrations:

   ```
   py manage.py migrate
   ```

### 2. Start the Django development server:

   ```
   python manage.py runserver
   ```

### 3. In a separate terminal, compile the Tailwind CSS:

   ```
  npx tailwindcss -i ./tailwind.css -o ./static/output.css  --watch
   ```

Now, you can access the e-commerce website at `http://localhost:8000`.


## Project Structure
The project consists of several Django apps and their corresponding views, models, and templates.

### Models
 - `Products`: Represents individual products with attributes like name, price, and category.
 - `Category`: Represents product categories.
 - `Customer`: Represents registered users.
 - `Order`: Represents orders placed by customers.
### Views
- `Index`: Displays the homepage with a list of products.
- `webstore`: Displays the webstore page.
- `ProductView`: Displays the details of a specific product.
- `Signup`: Handles user registration.
- `Login` and `logout`: Handles user authentication and session management.
- `Cart`: Manages the shopping cart.
- `CheckOut`: Handles the checkout process.
- `OrderView`: Displays the order history for authenticated users.
### Middleware
- `auth_middleware`: Checks user authentication and redirects unauthenticated users to the login page.

## ER and Use-Case Diagrams

![ER Diagram 1](https://ik.imagekit.io/swastik/ERDIAGRAM_AbWX9ho3-.jpg?updatedAt=1683300452141)

## 


![ER Diagram 2](https://ik.imagekit.io/swastik/o9RChwVA_4x_ZYbPH7a_8.jpg?updatedAt=1683300453692)

## Usage
 1. Browse products on the homepage or webstore page.
 2. Click on a product to view its details.
 3. Add products to the cart and proceed to checkout.
 4. Register or log in to complete the purchase.
 5. View your order history in the orders page.

## Customization

You can customize the app by modifying the views, templates, and styles to suit your needs. For example, you can add new product attributes, implement additional functionality, or change the look and feel of the app.

To customize the admin panel, you can use the `AdminProduct` and `CategoryAdmin` classes in the `admin.py` file. These classes inherit from Django's `admin.ModelAdmin` and allow you to customize the display of the `Products` and `Category` models in the admin panel.