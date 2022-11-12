from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.users import User
from models.recipes import Recipe
from models.ingredients import Ingredient, IngredientList




db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables have been created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables have been dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            id = 0,
            username = "HEADCHEF",
            password = bcrypt.generate_password_hash("password123").decode("utf-8"),
            is_admin = True
        ),
        
        User(
            id = 1,
            username = "JiroDreams",
            password = bcrypt.generate_password_hash("sharpen").decode("utf-8"),
            is_admin = False
        ),

        User(
            id = 2,
            username = "Hells_Kitchen",
            password = bcrypt.generate_password_hash("gordonramsey").decode("utf-8"),
            is_admin = False
        ),

        User(
            id = 3,
            username = "metalfingers",
            password = bcrypt.generate_password_hash("calamusroot").decode("utf-8"),
            is_admin = False
        )
    ]

    db.session.add_all(users)
    db.session.commit()
    print("Users have been seeded")


    recipes = [
        Recipe(
            id = 1000,
            recipe_name = "Hells Kitchen Secret Sphaghetti",
            preparation_time = "30 mins",
            cooking_time = "8 hours",
            servings = 12,
            process = "In a Dutch oven, cook the beef, sausage, onions and garlic over medium heat until meat is no longer pink; drain. Transfer to a 5-qt. slow cooker. Stir in the tomatoes, tomato paste, water, sugar, Worcestershire sauce, oil and seasonings. Cook, covered, on low 8-10 hours. Discard bay leaves. Serve with spaghetti.",
            date_created = date.today(),
            user = users[2],
        ),
        Recipe(
            id = 1001,
            recipe_name = "Pasta Carbonara",
            preparation_time = "10 mins",
            cooking_time = "30 mins",
            servings = 4,
            process = "Put a large pot of salted water on to boil (1 tablespoon salt for every 2 quarts of water). While the water is coming to a boil, heat the olive oil or butter in a large sauté pan over medium heat. Add the bacon or pancetta and cook slowly until crispy. Add the garlic (if using) and cook another minute, then turn off the heat and put the pancetta and garlic into a large bowl. n a small bowl, beat the eggs and mix in about half of the cheese. Once the water has reached a rolling boil, add the dry pasta, and cook, uncovered, at a rolling boil.  When the pasta is al dente (still a little firm, not mushy), use tongs to move it to the bowl with the bacon and garlic. Let it be dripping wet. Reserve some of the pasta water. Move the pasta from the pot to the bowl quickly, as you want the pasta to be hot. It's the heat of the pasta that will heat the eggs sufficiently to create a creamy sauce. Toss everything to combine, allowing the pasta to cool just enough so that it doesn't make the eggs curdle when you mix them in. (That's the tricky part.) Add the beaten eggs with cheese and toss quickly to combine once more. Add salt to taste. Add some pasta water back to the pasta to keep it from drying out. Serve.",
            date_created = date.today(),
            user = users[1],
        ),
        Recipe(
            id = 1002,
            recipe_name = "Classic Bacon and Eggs",
            preparation_time = "10 mins",
            cooking_time = "10 mins",
            servings = 4,
            process = "Fry bacon in a pan on medium-low flame until they are crispy. Transfer them into a plate. Use the same pan to cook eggs. Crack eggs in the pan and cook them as you like; sunny side up. Cover the pan so that the egg cooks properly. Add seasoning and garnish with chopped fresh parsley. Serve bacon and eggs hot.",
            date_created = date.today(),
            user = users[1],
        )
    ]

    db.session.add_all(recipes)
    db.session.commit()
    print("Recipes have been seeded")

    ingredients = [
        # 0-9
        Ingredient(
            name = "ground beef"
        ),
        Ingredient(
            name = "italian sausage"
        ),
        Ingredient(
            name = "brown onion"
        ),
        Ingredient(
            name = "canned diced tomatoes"
        ),
        Ingredient(
            name = "tomato paste"
        ),
        Ingredient(
            name = "minced garlic cloves"
        ),
        Ingredient(
            name = "water"
        ),
        Ingredient(
            name = "sugar"
        ),
        Ingredient(
            name = "worcestershire sauce"
        ),
        Ingredient(
            name = "canola oil"
        ),
        # 10-19
        Ingredient(
            name = "parsley"
        ),
        Ingredient(
            name = "bay leaves"
        ),
        Ingredient(
            name = "salt"
        ),
        Ingredient(
            name = "pepper"
        ),
        Ingredient(
            name = "spaghetti"
        ),
        Ingredient(
            name = "dried basil"
        ),
        Ingredient(
            name = "eggs"
        ),
        Ingredient(
            name = "parmesan cheese"
        ),
        Ingredient(
            name = "bacon"
        ),
        Ingredient(
            name = "olive oil"
        ),
        # 20-29
        Ingredient(
            name = "ginger"
        ),
         Ingredient(
            name = "carrots"
        ),
         Ingredient(
            name = "mushrooms"
        ),
         Ingredient(
            name = "chicken"
        ),
         Ingredient(
            name = "egg noodles"
        ),
         Ingredient(
            name = "soy sauce"
        ),
         Ingredient(
            name = "corn chips"
        ),
         Ingredient(
            name = "smoked paprika"
        ),
         Ingredient(
            name = "canned red kidney beans"
        ),
        Ingredient(
            name = "ground chilli"
        ),
        # 30-36
        Ingredient(
            name = "cheddar"
        ),
         Ingredient(
            name = "tomatoes"
        ),
         Ingredient(
            name = "burrito seasoning mix"
        ),
         Ingredient(
            name = "tortillas"
        ),
         Ingredient(
            name = "iceburg lettuce"
        ),
         Ingredient(
            name = "sour cream"
        ),
         Ingredient(
            name = "avocado"
        )
    ]

    db.session.add_all(ingredients)
    db.session.commit()
    print("Ingredients have been seeded")

    ingredient_lists = [
    # spaghetti
        IngredientList(
            recipe = recipes[0],
            measurement = "500 grams",
            ingredients = ingredients[0]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "5",
            ingredients = ingredients[1]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "4 medium",
            ingredients = ingredients[2]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "4 cans (400ml)",
            ingredients = ingredients[3]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "150 grams",
            ingredients = ingredients[4]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "1/2 cup",
            ingredients = ingredients[6]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "8",
            ingredients = ingredients[5]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "1/4 cup",
            ingredients = ingredients[7]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "1/4 cup",
            ingredients = ingredients[8]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "1 tablespoon",
            ingredients = ingredients[9]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "1/4 cup minced",
            ingredients = ingredients[10]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "4",
            ingredients = ingredients[11]
        ),
        IngredientList(
            recipe = recipes[0],
            measurement = "1 teaspoon",
            ingredients = ingredients[12]
        ),     
        IngredientList(
            recipe = recipes[0],
            measurement = "1 teaspoon",
            ingredients = ingredients[13]
        ),    
        IngredientList(
            recipe = recipes[0],
            measurement = "400 grams",
            ingredients = ingredients[14]
        ),    
        IngredientList(
            recipe = recipes[0],
            measurement = "1 tablespoon",
            ingredients = ingredients[15]
        ),    
        # carbonara
        IngredientList(
            recipe = recipes[1],
            measurement = "1 tablespoon",
            ingredients = ingredients[19]
        ),    
        IngredientList(
            recipe = recipes[1],
            measurement = "200 grams",
            ingredients = ingredients[18]
        ),    
        IngredientList(
            recipe = recipes[1],
            measurement = "2",
            ingredients = ingredients[5]
        ),    
        IngredientList(
            recipe = recipes[1],
            measurement = "3 or 4",
            ingredients = ingredients[16]
        ),    
        IngredientList(
            recipe = recipes[1],
            measurement = "1 cup",
            ingredients = ingredients[17]
        ),    
        IngredientList(
            recipe = recipes[1],
            measurement = "400 grams",
            ingredients = ingredients[14]
        ),
        IngredientList(
            recipe = recipes[1],
            measurement = "1 pinch",
            ingredients = ingredients[12]
        ),
        IngredientList(
            recipe = recipes[1],
            measurement = "8 good cracks",
            ingredients = ingredients[13]
        ),    
    # bacon and eggs
        IngredientList(
            recipe = recipes[2],
            measurement = "8",
            ingredients = ingredients[16]
        ),
        IngredientList(
            recipe = recipes[2],
            measurement = "150 grams",
            ingredients = ingredients[18]
        ),
        IngredientList(
            recipe = recipes[2],
            measurement = "1/4 cup",
            ingredients = ingredients[10]
        ),
        IngredientList(
            recipe = recipes[2],
            measurement = "to taste",
            ingredients = ingredients[12]
        ),  
        IngredientList(
            recipe = recipes[2],
            measurement = "to taste",
            ingredients = ingredients[13]
        )       
    ]
    db.session.add_all(ingredient_lists)
    db.session.commit()
    print("Ingredient lists have been seeded")

    
