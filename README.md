# Django eCommerce Website

Welcome to the Django eCommerce Website project! This is a fully-featured eCommerce platform built using Django, designed for managing product listings, shopping carts, customer authentication, and payment processing.
## Features

- User registration and authentication
- Product catalog with categories and filtering
- Product search functionality
- Shopping cart and checkout process
- Payment gateway integration (e.g., PayPal, Stripe)
- Admin dashboard for managing products, orders, and users


## Requirements

- Python 3.9+
- Django 4.x
- MySQL (or any other supported database)
- Stripe or PayPal API keys (for payment integration)
## Installation

1. Clone the Repo

```bash
  git clone https://github.com/chemoiko/Django-Ecommerce-Website.git
  cd django-ecommerce

```
2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

```

3. Install dependencies

```bash
  pip install -r requirements.txt


```

4. Set up environment variables
    
  ```bash
 SECRET_KEY=<your-secret-key>
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
DATABASE_URL=postgres://<db_user>:<db_password>@localhost:5432/<db_name>
STRIPE_API_KEY=<your-stripe-api-key>
PAYPAL_API_KEY=<your-paypal-api-key>


```

5. Set up the database

  ```bash
python manage.py migrate
python manage.py createsuperuser


```

6. Run the development server

  ```bash
  python manage.py runserver


```
## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

## Usage

1. The home page contains all the products. You can add the products to your cart by clicking on the Add To Cart button and you will see the number of items in the cart icon update dynamically.
<img src="https://imgur.com/dkLzsUy">

2. Click on the cart icon in nav to see all the items you added to cart.

3. The up and down arrow buttons can be used to change the quantity and the prices and total will change automatically.

4. The user can confirm order using the Checkout button.
5. If the user is logged in, he will not be asked to fill in his name and email.
6. The user will fill in the shipping details and click continue to payment.
<img src="https://imgur.com/undefined">
7. A guest user can also order items through cookies.

_Reference Dennis Ivy YouTube tutorial_
