# ecommerce
-------INTRODUCTION--------
The goal is to develop a Django web application with REST APIs for a fictional e-commerce store.

Template is written with django 4.2 and python 3 in mind.

-------FEATURES------------
- APIs related to Admin should have the capabilities to:
* Manage Products & their inventory:
* Can add, edit, and delete products.
* Each product should have a name, description, price, and quantity.
* Can upload and change product image
* Manage Orders: Can view and update order statuses
* Manage user accounts.
* Can view, edit, and delete user accounts
* Each user account should have username, firstName, lastName, phone and email

- APIs related to Customer should have the capabilities to:
* Get a list of available products along with their image even if unauthenticated
* Register and Authenticate using JSON Web Tokens (JWT).
* Cart Functionality: Authenticated users can add products to their cart.
* Users can view their cart, update quantities, and remove items from the cart.
* Order Placement: Authenticated users can place an order for the items in their cart.
* Each order should capture the user's details, selected products, and total amount.
* See order history

-------SETUP---------------
The first thing to do is to clone the repository:
- git clone https://github.com/srivastavapriyanshi/ecommerce.git
- cd ecommerce

Create a virtual environment to install dependencies in and activate it:
- python -m venv env
- env\Scripts\activate (for windows) 
- source env/bin/activate (for linux/macOS)

Then install the dependencies:
- (env)$ pip install -r requirements.txt

Once pip has finished downloading the dependencies, then simply apply the migrations:
-(env)$ python manage.py migrate

You can now run the development server:
- (env)$ python manage.py runserver

