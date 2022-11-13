# Recipe API

## **Identification of the problem you are trying to solve by building this partiular app. And why? (R1, R2)**  
  
I like to cook. Like, I like to cook a LOT. I also really like trying new recipes. I often find myself scouring the internet for recipes, only to be astounded by the endless possibilities and lack of organisation on most recipe sites. After scouring the internet for the perfect recipe, I'll eventually give up and just select one whatever's on my screen by that point.
  
On my recipe searches, I encounter way too many recipe blogs that bombard you with a life story of minimal importance, requiring way too much scrolling to get to the actual recipe at the bottom of the page.  

These unfortunately frequent recipe-hunting experiences had me thinking about the need for some sort of social recipe sharing API, in which users could upload and share their collection of recipes. Creating an API that's focused on what actually matters (i.e. the recipe!) and presenting it right where you would want to see it (i.e. the top of the page!) seems like a thing the world of online recipes needs.

---

## **Why have I chosen this database system? What are the drawbacks compared to others? (R3)**

For this app, I have chosen to use PostgresSQL. PostgresSQL belongs to the category of Relational Database Management System's (RDBMS). RDBMS involve the use of the Structured Database Query Language (SQL). SQL allows a database system to access and manipulate the databases within. Notably, information redundancy and real-time flexibility are distinct perks of using a RDBMS over a non-relational DBMS. Information can be easily normalized, and when dealing with bigger databases RDBMS's can maintain better data consistency.

Why PostgresSQL though? PostgresSQL is open-source software, meaning that anyone can use it for whatever their intended purpose is. PostgresSQL has a large community of dedicated developers behind it, along with an extensive history and strong reputation for its architecture, data integrity and extensibility. As a student, being able to access such a powerful RDBMS for free is highly appreciated.  

Whilst not many, there are a few drawbacks to PostgresSQL. PostgresSQL has been found to be slower than another RDBMS, MySQL. MySQL also has a larger library of supported open-source apps than PostgresSQL. However, for my app neither of these drawbacks were considered to be much of a problem.

---

## **Identify and discuss the key functionalities and benefits of an ORM (R4)**

An ORM (Object-Relational-Mapper) allows you to interact with relational databases in the language of your choice. Whilst SQL is considered an incredibly powerful language, an ORM can let you develop your own queries in a language you are more comfortable in. This can increase the speed in which an application can be developed. Furthermore, ORM's can allow you to switch RDBMS's easily (if neccessary).

An ORM has a collection of built-in queries that can be used on a database (within the chosen ORM language), further saving time for the developer. Removing the necessity for constant switching between languages can lead to quicker production times.

ORM's generate objects which map to tables in the selected database. Once these connections have been made the ORM acts as an abstraction layer for the application towards the database, allowing the developer to code away in the preferred language, which can then be reflected in the database.

---

## **Document all endpoints for the API (R5)**

## /auth/users/

- Methods: GET
- Arguments: None
- Description: Admin can retrieve a list of users and all their assoicated information (excluding password)
- Authentication/Authorization: Done through JWT Bearer token (admin only)
- Request Body: n/a
- Response Body:
  
```JSON
[
    {
        "recipes": [],
        "username": "HEADCHEF",
        "id": 1,
        "first_name": null,
        "is_admin": true
    },
    {
        "recipes": [
            {
                "recipe_name": "Pasta Carbonara",
                "date_created": "2022-11-13"
            },
            {
                "recipe_name": "Super Classic Bacon and Eggs",
                "date_created": "2022-11-13"
            }
        ],
        "username": "JiroDreams",
        "id": 2,
        "first_name": "Jiro",
        "is_admin": false
    },
    {
        "recipes": [
            {
                "recipe_name": "Hells Kitchen Secret Sphaghetti",
                "date_created": "2022-11-13"
            }
        ],
        "username": "Hells_Kitchen",
        "id": 3,
        "first_name": "Gordon",
        "is_admin": false
    },
    {
        "recipes": [
            {
                "recipe_name": "Stir fry",
                "date_created": "2022-11-13"
            }
        ],
        "username": "metalfingers",
        "id": 4,
        "first_name": "DOOM",
        "is_admin": false
    }
]
```

## /auth/register/

- Methods: POST
- Arguments: n/a
- Description: Register a new user.
- Authentication: n/a
- Authorization: n/a
- Request Body:
  
```JSON
  
{   "username": "Californiacooking",
    "first_name": "Cali",
    "password": "dontreadthis"
}

```

- Response Body:
  
```JSON
{
    "is_admin": false,
    "username": "Californiacooking",
    "id": 5,
    "first_name": "Cali",
    "recipes": []
}
```

## /auth/login/

- Methods: POST
- Arguments: n/a
- Description: Login into an existing user.
- Authentication: n/a
- Authorization: n/a
- Request Body:
  
```JSON
{   
    "username": "Californiacooking",
    "password": "dontreadthis"
}
```

- Response Body:
  
```JSON
{
    "username": "Californiacooking",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODMzNjYzOSwianRpIjoiMWY5MDRiZTMtM2JmOC00Nzc2LWE5ZGUtMDY0ZjU1Y2U0MjgyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjUiLCJuYmYiOjE2NjgzMzY2MzksImV4cCI6MTY2ODQyMzAzOX0.5oo5forU2oW8o9vTrcQ_9HbeS0S0-5qMYRUSZUqKV7w"
}
```

## /auth/users/\<username>/

- Methods: GET
- Arguments: username
- Description: Check a single user's information (excluding password).
- Authentication: JWT bearer token
- Authorization: Only users with is_admin = True can access.
- Request Body: n/a
- Response Body:
  
```JSON
{
    "is_admin": false,
    "username": "Californiacooking",
    "id": 5,
    "first_name": "Cali",
    "recipes": []
}
```

## /auth/users/\<username>/del/

- Methods: DELETE
- Arguments: username
- Description: Delete a user and any associated recipes.
- Authentication: JWT bearer token
- Authorization: Only users with is_admin = True can access.
- Request Body: n/a
- Response Body:
  
```JSON
{
    "message": "Californiacooking has been deleted"
}
```

## /recipes/

- Methods: GET
- Arguments: n/a
- Description: View all recipes and ingredient_lists in the database.
- Authentication: n/a
- Authorization: n/a
- Request Body: n/a
- Response Body:

```JSON
[
    {
        "id": 4,
        "recipe_name": "Stir fry",
        "preparation_time": "20 mins",
        "cooking_time": "10 mins",
        "servings": 4,
        "process": "Finely chop or slice the vegetables into pieces roughly the same size. Slice the carrots diagonally, slice the baby corn, cut the broccoli into small florets, then slice the stem, and finely slice the peppers, cabbage or pak choi. Heat the oil in a large frying pan or wok, then fry the garlic and ginger for 1 min. Add the veg and toss to coat. Fry for 2-3 mins, then add the soy sauce and chilli sauce, if using, and mix well. Cook for 2-3 mins more until the veg is tender. Stir in the prawns, salmon or chicken and heat through. Serve over the noodles.",
        "date_created": "2022-11-13",
        "user_id": 4,
        "ingredient_lists": [
            {
                "id": 30,
                "measurement": "250 grams",
                "ingredient": {
                    "name": "carrots"
                },
                "recipe": {
                    "recipe_name": "Stir fry"
                }
            },
            {
                "id": 31,
                "measurement": "250 grams",
                "ingredient": {
                    "name": "mushrooms"
                },
                "recipe": {
                    "recipe_name": "Stir fry"
                }
            },
            {
                "id": 32,
                "measurement": "2",
                "ingredient": {
                    "name": "minced garlic cloves"
                },
                "recipe": {
                    "recipe_name": "Stir fry"
                }
            }
        ]
    },
    {
        "id": 3,
        "recipe_name": "Super Classic Bacon and Eggs",
        "preparation_time": "10 mins",
        "cooking_time": "10 mins",
        "servings": 4,
        "process": "Fry bacon in a pan on medium-low flame until they are crispy. Transfer them into a plate. Use the same pan to cook eggs. Crack eggs in the pan and cook them as you like; sunny side up. Cover the pan so that the egg cooks properly. Add seasoning and garnish with chopped fresh parsley. Serve bacon and eggs hot.",
        "date_created": "2022-11-13",
        "user_id": 2,
        "ingredient_lists": [
            {
                "id": 25,
                "measurement": "8",
                "ingredient": {
                    "name": "eggs"
                },
                "recipe": {
                    "recipe_name": "Super Classic Bacon and Eggs"
                }
            },
            {
                "id": 26,
                "measurement": "150 grams",
                "ingredient": {
                    "name": "bacon"
                },
                "recipe": {
                    "recipe_name": "Super Classic Bacon and Eggs"
                }
            },
            {
                "id": 27,
                "measurement": "1/4 cup",
                "ingredient": {
                    "name": "parsley"
                },
                "recipe": {
                    "recipe_name": "Super Classic Bacon and Eggs"
                }
            },
            {
                "id": 28,
                "measurement": "to taste",
                "ingredient": {
                    "name": "salt"
                },
                "recipe": {
                    "recipe_name": "Super Classic Bacon and Eggs"
                }
            },
            {
                "id": 29,
                "measurement": "to taste",
                "ingredient": {
                    "name": "pepper"
                },
                "recipe": {
                    "recipe_name": "Super Classic Bacon and Eggs"
                }
            }
        ]
    }
]
```

*^^it continues on for longer, but I thought I would trim it down.*
  
## /recipes/\<int:user_id\>/

- Methods: GET
- Arguments: user_id
- Description: View a single users created recipes.
- Authentication: n/a
- Authorization: n/a
- Request Body: n/a
- Response Body:
  
```JSON
[
    {
        "id": 4,
        "recipe_name": "Stir fry",
        "preparation_time": "20 mins",
        "cooking_time": "10 mins",
        "servings": 4,
        "process": "Finely chop or slice the vegetables into pieces roughly the same size. Slice the carrots diagonally, slice the baby corn, cut the broccoli into small florets, then slice the stem, and finely slice the peppers, cabbage or pak choi. Heat the oil in a large frying pan or wok, then fry the garlic and ginger for 1 min. Add the veg and toss to coat. Fry for 2-3 mins, then add the soy sauce and chilli sauce, if using, and mix well. Cook for 2-3 mins more until the veg is tender. Stir in the prawns, salmon or chicken and heat through. Serve over the noodles.",
        "date_created": "2022-11-13",
        "user_id": 4,
        "ingredient_lists": [
            {
                "id": 30,
                "measurement": "250 grams",
                "ingredient": {
                    "name": "carrots"
                },
                "recipe": {
                    "recipe_name": "Stir fry"
                }
            },
            {
                "id": 31,
                "measurement": "250 grams",
                "ingredient": {
                    "name": "mushrooms"
                },
                "recipe": {
                    "recipe_name": "Stir fry"
                }
            },
            {
                "id": 32,
                "measurement": "2",
                "ingredient": {
                    "name": "minced garlic cloves"
                },
                "recipe": {
                    "recipe_name": "Stir fry"
                }
            },
            {
                "id": 33,
                "measurement": "1cm",
                "ingredient": {
                    "name": "ginger"
                },
                "recipe": {
                    "recipe_name": "Stir fry"
                }
            }
        ]
    }
]
```

## /recipes/\<int:user_id>/\<int:id>/

- Methods: GET
- Arguments: user_id, id
- Description: Select a single recipe from a single user.
- Authentication: n/a
- Authorization: n/a
- Request Body: n/a
- Response Body:
  - Very similar to the code posted above.

## /recipes/\<int:user_id>/\<int:id>/

- Methods: PUT, PATCH
- Arguments: user_id, id
- Description: Update a single recipe from a user.
- Authentication: JWT bearer token
- Authorization: admin only
- Request Body:
  
```JSON

{
    "recipe_name": "Stir fry",
    "preparation_time": "20 mins",
    "cooking_time": "10 mins",
    "servings": 2,
    "process": "I have removed the process mwahahaha",
}
```

- Response Body:
  
```JSON
{
    "id": 4,
    "recipe_name": "Stir fry",
    "preparation_time": "20 mins",
    "cooking_time": "10 mins",
    "servings": 2,
    "process": "I have removed the process mwahahaha",
    "date_created": "2022-11-13",
    "user_id": 4,
    "ingredient_lists": [
        {
            "id": 30,
            "measurement": "250 grams",
            "ingredient": {
                "name": "carrots"
            },
            "recipe": {
                "recipe_name": "Stir fry"
            }
        },
        {
            "id": 31,
            "measurement": "250 grams",
            "ingredient": {
                "name": "mushrooms"
            },
            "recipe": {
                "recipe_name": "Stir fry"
            }
        },
        {
            "id": 32,
            "measurement": "2",
            "ingredient": {
                "name": "minced garlic cloves"
            },
            "recipe": {
                "recipe_name": "Stir fry"
            }
        },
        {
            "id": 33,
            "measurement": "1cm",
            "ingredient": {
                "name": "ginger"
            },
            "recipe": {
                "recipe_name": "Stir fry"
            }
        },
        {
            "id": 34,
            "measurement": "200 grams",
            "ingredient": {
                "name": "chicken"
            },
            "recipe": {
                "recipe_name": "Stir fry"
            }
        }
    ]
}
```


## /recipes/

- Methods: POST
- Arguments: n/a
- Description: Create a new recipe, the user_id is assigned based on who is signed in with the bearer token.
- Authentication: JWT bearer token
- Authorization: any registered user
- Request Body:
  
```JSON
{
    "recipe_name": "Cheese Sandwich",
    "preparation_time": "1 mins",
    "cooking_time": "2 mins",
    "servings": 1,
    "process": "Get the cheese, get the bread, place cheese within bread. Wallah!"
}
```

- Response Body:
  
  ```JSON
  {
    "id": 5,
    "recipe_name": "Cheese Sandwich",
    "preparation_time": "1 mins",
    "cooking_time": "2 mins",
    "servings": 1,
    "process": "Get the cheese, get the bread, place cheese within bread. Wallah!",
    "date_created": "2022-11-13",
    "user_id": 1,
    "ingredient_lists": []
    }
    ```

## /recipes/\<int:user_id>/\<int:id>/

- Methods: DELETE
- Arguments: user_id, id
- Description: Update a single recipe from a user.
- Authentication: JWT bearer token
- Authorization: admin only
- Request Body: n/a
- Response Body:

```JSON
{
    "message": "Recipe 4 has been deleted"
}
```

## /ingredients/

- Methods: GET
- Arguments: n/a
- Description: Get a list of all ingredients and their associated id.
- Authentication: n/a
- Authorization: n/a
- Request Body: n/a
- Response Body:
  
```JSON
[
    {
        "name": "ground beef",
        "id": 1
    },
    {
        "name": "italian sausage",
        "id": 2
    },
    {
        "name": "brown onion",
        "id": 3
    },
    {
        "name": "canned diced tomatoes",
        "id": 4
    },
    {
        "name": "tomato paste",
        "id": 5
    }
]
```

## /ingredients/

- Methods: POST
- Arguments: n/a
- Description: Register a new ingredient.
- Authentication: JWT bearer token
- Authorization: any logged in user can create a new ingredient
- Request Body:

```JSON
{
    "name": "Cheese"
}
```

- Response Body:
  
```JSON
{
    "name": "Cheese",
    "id": 38
}
```


## /ingredient_lists/

- Methods: GET
- Arguments: n/a
- Description: Get a list of all the assoicated ingredients and recipes.
- Authentication: n/a
- Authorization: n/a
- Request Body: n/a
- Response Body:
  
```JSON
[
    {
        "id": 1,
        "measurement": "500 grams",
        "ingredient": {
            "name": "ground beef"
        },
        "recipe": {
            "recipe_name": "Hells Kitchen Secret Sphaghetti"
        }
    },
    {
        "id": 2,
        "measurement": "5",
        "ingredient": {
            "name": "italian sausage"
        },
        "recipe": {
            "recipe_name": "Hells Kitchen Secret Sphaghetti"
        }
    },
    {
        "id": 3,
        "measurement": "4 medium",
        "ingredient": {
            "name": "brown onion"
        },
        "recipe": {
            "recipe_name": "Hells Kitchen Secret Sphaghetti"
        }
    }
]
```

## /ingredient_lists/

- Methods: POST
- Arguments: n/a
- Description: Add an existing ingredient to the list with its associated recipe and measurement.
- Authentication: JWT bearer token
- Authorization: Registered users
- Request Body:

```JSON
{
    "ingredient_id": 38,
    "measurement": "2 slices",
    "recipe_id": 5
}
```

- Response Body:
  
```JSON
{
    "message": "Successfully added ingredient to the list"
}
```

--

## **ERD(R6)**

![erd](docs/erd.png)

--

## **Detail any thrid-party services/packages the app uses (R7)**

The third-party services/packages used in my app are:

- Flask
  - Python web framework, provides tools and libraries to assist with building a web framework.
- SQLAlchemy
  - A Python SQL toolkit and ORM. Generates SQL statements to interact with the RDBMS.
- psycopg2
  - A PostgresSQL database adapter for Python. Allows generated SQL statements from SQLAlchemy to be sent to the database.
- Marshmallow
  - A Python library that converts complex data types to native Python data types and vice versa.
- Bcrypt
  - A password-hashing function, used to secure passwords.
- JWT
  - imported via flask-jwt-extended. JWT (JSON Web Tokens) allow user to be authorised and identified by the server.
- DateTime
  - Used to generate the current date when requested.

--

## **Describe your projects models in terms of the relationships they have with each other (R8)**

### Users

- The users model has id, username, first_name, password, is_admin and recipes columns.
- The recipes column has a relationship with users, and thus, when a user is queried any recipes that they have contributed will be displayed. If a user was to be deleted any recipes that they have contributed will be deleted as well.

### Recipes

- The recipes model has id, recipe_name, preparation_time, cooking_time, servings, process, date_created, user_id and ingredient_lists columns.
- The user_id column is a foreign key from associated with the id from the users table.
- The ingredient_lists column references a relationship with the ingredient_lists table. When a recipe is queried, the related entries in the ingredient_lists table will be displayed too. If a recipe was to be deleted it would also delete any associated data in the ingredient_lists table.

### Ingredients

- The ingredients model has id, name, and ingredient_lists columns.
- The ingredients_list column is a relationship with the ingredients table. 

### Ingredient Lists

- The ingredient_lists model has id, measurement, ingredient_id, and recipe_id columns.
- The ingredient_id column is a foreign key from associated with the id from the ingredients.
- The recipe_id column is a foreign key from associated with the recipe.

--

## **Discuss the database relations to be implemented in your application (R9)**

The first relationship is between the users table and the recipes table. The users table has a one-to-many relationship with the recipes table. This means that a user can have many recipes, but a recipe can only have one user. The user_id is a foreign key value in the recipes table. Users are also not required to contribute a recipe, so there may not necessarily be a corresponding recipe value for each user.

The second relationship is between the recipes table the ingredient_lists table. The recipes table has a one-to-many relationship with the ingredient_lists table. This means that recipe can have many ingredient_lists values associated with it, but a value in the ingredient_lists table will only direct to one recipe.

The third relationship is between the ingredients table and the ingredient_lists table. The ingredients table has a one-to-many relationship with the ingredient_lists table. This means that an ingredient can have many ingredient_lists values associated with it, however, an entry in the ingredient_lists table will only direct to one ingredient.

The last two relationships were both one-to-many (with both directing to the ingredients_list table), however this designed in order to satisfy a many-to-many relationship that exists between recipes and ingredients. As you cannot have a direct relationship with a many-to-many relationship, it is necessary to have a join table. The join table has two forieng keys from each of the other two tables, allowing for the ingredient to direct to recipes and vice versa.


---

## **Describe the way tasks are allocated and tracked in your project(R10)**

To manage the development of the project, I created a trello board which outlined:

- The tasks to be done.
- Which tasks were currenlty being completed.
- Which tasks had been finished.
  
I have to be honest and admit my board was managed quite chaotically, in that my original planning wasn't sufficient to develop an app with and required a mid-assignment makeover. There were several archives/deletes of cards, and ultimately the board reflects a slightly disorganised and chaotic approach to the assignment. I still developed checklists to help determine what the crucial elements of the project were, and checked them off as they were completed. Reflecting on my management of tasks, I think I needed to be more organised and have a more concrete plan when planning out future tasks.

### [Trello Link](https://trello.com/invite/b/umepIf8e/ATTI0a8954c8da0605a8e3c74d3f66225f1c48BE9CBE/api-assignment)

### [GitHub](https://github.com/ZacharyHLong/api_assignment)
---
