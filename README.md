# Project 3

Web Programming with Python and JavaScript

## Static:
   static folder contain 3 folders
   * images
   * css
   * js
## Templates:
   containers all of the templates 
   * cart.html -> Shows user item in table form
   * home.html -> just displays username and status about the orders
   * index.html -> main page for the whole site
   * menu.html -> displays all the menu
   * menu-item.html -> menu item shows specific item in category
     
## moels.py 
   Category model
   * Item -> stores just the name of items
   * ItemPrice -> have foreign key to size model and Item model, also contain price of each item
   * Cart -> cart table is used to store data of user cart
   * Order -> order is used to store order information 
     

## urls.py
   contains all of the mapping of routes to individual view functions

## views.py 
   * menu -> displays all of the categories
   * menu_dish -> individual dishes in the cateogry like pasta have alot of items.
   * menu_item -> used to show individual item in the cateogry in differnet html page.


Additional Feature:
Allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders
