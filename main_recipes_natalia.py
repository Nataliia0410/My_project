from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from random import randint
import json, requests
import logging
import psycopg2
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name':"Seans-Python-Flask-REST-Boilerplate"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

logging.basicConfig(filename='logs.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
login_list = {}


# Nata_recipes connection
conn = psycopg2.connect(dbname='nata_db', user='nata_u', password='123', host='159.69.151.133', port='5056')
cursor = conn.cursor()




@app.route('/main_page', methods=['GET'])
def main_page():

    main_page_link = 'main_page_link'

    return main_page_link


@app.route('/login_form', methods=['GET'])
def login_form():
    login_form_link = 'login_form_link'


    return login_form_link


@app.route('/registration_form', methods=['GET'])
def registration_form():
    registration_form_link = 'registration_form_link'

    return registration_form_link



@app.route('/login', methods=['POST'])
def login():


    user_login = request.form.get('user_login')
    password = request.form.get('password')

    #todo validation login and password in DB
    #todo if login create token
    #todo if login return recipes_list_page
    #todo if not login return error message


    page_link = 'page_link'

    return page_link


@app.route('/logout', methods=['POST'])
def logout():


    user_id = request.args.get('user_id')
    token = request.args.get('token')
    # todo kill token

    main_page_link = 'main_page_link'

    return main_page_link


@app.route('/registration', methods=['POST'])
def registration():


    user_image = request.form.get('user_image')
    email = request.form.get('email')
    login = request.form.get('login')
    password = request.form.get('password')

    cursor = conn.cursor()

    user = False


    if conn:

        pp_query = """select login from users where login='""" + login + """' """

        cursor.execute(pp_query)

        rows = cursor.fetchall()

        if len(rows):
            user = True
        else:
            user = False

        conn.commit()

        if not user:

            print('CREATE_USER =====')
            base_data = (login, email, password, user_image)

            p_query = """INSERT INTO public.users (login, email, password_users, photo) VALUES (%s,%s,%s,%s)"""
            cursor.execute(p_query, base_data)
            conn.commit()

            cursor.close()



    # todo put image on server FS
    # todo put image link address on DB

    # todo check unique email in DB
    # todo if unique then save user to DB
    # todo if not unique then return error message

    # todo check unique login in DB
    # todo if unique then save user to DB
    # todo if not unique then return error message

    # todo save password hash to DB

    # todo create token, send token to client
    # todo get user_id from DB, send user_id to client
    # todo if Succes registration return recipes list page

    recipes_page_link = 'recipes_page_link'

    return recipes_page_link


@app.route('/undo_change_user', methods=['GET'])
def undo_change_user():
    user_id = request.args.get('user_id')
    token = request.args.get('token')

    recipes_page_link = 'recipes_page_link'
    return recipes_page_link



@app.route('/user_change_form', methods=['GET'])
def user_change_form():

    user_id = request.args.get('user_id')
    token = request.args.get('token')


    # todo get user_image from DB by user_ID, send to client
    # todo get user_email from DB by user_ID, send to client
    # todo get user_login from DB by user_ID, send to client
    # todo send user_id to client

    change_form_link = 'change_form_link'

    return change_form_link



@app.route('/change_user', methods=['POST'])
def change_user():



    user_id = request.args.get('user_id')
    token = request.args.get('token')

    user_image = request.form.get('user_image')
    email = request.form.get('email')
    login = request.form.get('login')
    password = request.form.get('password')


    # todo check the same email and login in other users
    # todo if unique, save to DB
    # todo if not unique, return error message
    # todo send user_id to client
    # todo get user_image from DB by user_id

    recipes_page_link = 'recipes_page_link'

    return recipes_page_link



@app.route('/recipes_list_page', methods=['GET'])
def recipes_list_page():

    #
    # DB
    #
    # selec
    #
    # insert
    #
    # udate

    item_id = request.args.get('item_id')


    # user_id = request.args.get('user_id')
    # sub_item_id = None

    #todo get recipes from DB by user_id. Default recipe_item_id == 0, sub_item == Nome

    recipes_list = []

    if conn:
        print('CONN =====')


        cursor.execute("select * from public.recipe inner join public.category on public.recipe.category_id=public.category.category_id;")
        rows = cursor.fetchall()
        for i in rows:

            recipe_object = {'recipe_id':i[0],
                             'login_id':i[1],
                             'category_id': i[2],
                             'recipe_name': i[3],
                             'photo_address': i[4]}

            recipes_list.append(recipe_object)

            print("SL_rows = ", i)
            print("Row_type = ", type(i))
        cursor.close()



    # recipe_id = None
    # ingridients = None
    # recipe_image = None
    # cooking_time = None
    #
    # recipes_list = {"recipes": [
    #                     {"recipe_id": recipe_id,
    #                      "ingridients": ingridients,
    #                      "recipe_image": recipe_image,
    #                      "cooking_time": cooking_time},
    #                     {"recipe_id": recipe_id,
    #                      "ingridients": ingridients,
    #                      "recipe_image": recipe_image,
    #                      "cooking_time": cooking_time}
    #                     ]
    # }

    # recipes_page_link = 'recipes_page_link'

    return jsonify(recipes_list)


@app.route('/delete_recipe', methods=['GET'])
def delete_recipe():
    recipe_id = request.args.get('recipe_id')
    token = request.args.get('token')
    user_id = request.args.get('user_id')

    #todo check recipe by id
    #todo delete recipes from DB by recipes id list
    #todo get new recipes_list

    recipes_page_link = 'recipes_page_link'

    return recipes_page_link


@app.route('/create_recipe_form', methods=['GET'])
def create_recipe():
    # recipe_id = None (create new)
    # recipe_id = 1 (change exist)

    token = request.form.get('token')
    user_id = request.form.get('user_id')

    create_recipe_form = 'create_recipe_form'

    return create_recipe_form


@app.route('/save_recipe', methods=['POST'])
def save_recipe():

    # #action_id = 0 (create new)
    # #action_id = 1 (change exist)
    #
    # action_id = 0
    #
    # token = request.form.get('token')
    recipe_id = request.form.get('recipe_id')
    user_id = request.form.get('user_id')
    category_id = request.form.get('category_id')

    name_recipe = request.form.get('recipe_title')
    photo = request.form.get('photo')
    ingridients = request.form.get('ingridients')
    cooking_time = request.form.get('cooking_time')
    recipe_description = request.form.get('recipe_description')


    convert_rd_txt = save_txt(recipe_description)


    if conn:

        pp_query = """select recipe_id from recipe where recipe_id='""" + recipe_id + """' """
        print("recipe_id = ", pp_query)

        cursor.execute(pp_query)
        rows = cursor.fetchall()

        print("recipe_id = ", rows)

        if len(rows):
            recipe = True
        else:
            recipe = False

        conn.commit()

        if not recipe:

            print('CREATE_Recipe =====')
            base_data = (user_id, category_id, name_recipe, photo, ingridients, cooking_time, convert_rd_txt)

            p_query = """INSERT INTO public.recipe (login_id, category_id, name_recipe, photo, ingredients, cooking_time, recipe_description) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(p_query, base_data)
            conn.commit()

            # cursor.close()

        else:

            login_id = ' login_id=' + """'""" + user_id + """'"""+ ','
            category_id = 'category_id=' + """'""" + category_id + """'""" + ','
            name_recipe = 'name_recipe=' + """'""" + name_recipe + """'""" + ','
            photo = 'photo=' + """'""" + photo + """'""" + ','
            ingredients = 'ingredients=' + """'""" + ingridients + """'""" + ','
            cooking_time = 'cooking_time=' + """'""" + cooking_time + """'""" + ','
            recipe_description = 'recipe_description=' + """'""" + recipe_description + """'"""


            print('Update_Recipe =====')
            base_data = (user_id, category_id, name_recipe, photo, ingridients, cooking_time, convert_rd_txt)

            update_req = """update recipe""" + login_id + \
                         category_id + \
                         name_recipe + \
                         photo + \
                         ingredients + \
                         cooking_time + \
                         recipe_description + """where login_id=""" + """'""" + recipe_id + """'""" + """;"""


            print(update_req)



            # p_query = """INSERT INTO public.recipe (login_id, category_id, name_recipe, photo, ingredients, cooking_time, recipe_description) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            # cursor.execute(update_req)
            conn.commit()
            # cursor.close()




    #todo if ation 0, insert new recipe to db
    #todo if ation 1, update exist recipe in db
    #todo get new recipes_list

    create_recipe_form = 'create_recipe_form'

    return create_recipe_form





def save_txt(rd):

    rd_txt_name = 'recipes/1.txt'


    return rd_txt_name


