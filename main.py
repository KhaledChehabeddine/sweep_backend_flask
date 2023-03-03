from flask import Flask, render_template, request, redirect, url_for, jsonify
# from bson.json_util import dumps
# from bson.objectid import ObjectId
import pymongo
from pymongo.server_api import ServerApi
import os
# from werkzeug.security import generate_password_hash, check_password_hash
# import urllib
from flask_marshmallow import Marshmallow

app = Flask(__name__, template_folder='templates')

client = pymongo.MongoClient("mongodb+srv://admin:<c32C219F332>@cluster0.zahtuza.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
mongo = PyMongo(app)

# Initialize the Marshmallow serializer
ma = Marshmallow(app)


# Define the PromotionMainItem schema
class PromotionMainItemSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'image_url')

# Initialize the PromotionMainItem schema
promotion_main_item_schema = PromotionMainItemSchema()
promotion_main_items_schema = PromotionMainItemSchema(many=True)


# Define the PromotionCategory schema
class PromotionCategorySchema(ma.Schema):
    class Meta:
        fields = ('_id', 'title', 'subtitle')

# Initialize the PromotionCategory schema
promotion_category_schema = PromotionCategorySchema()
promotion_categories_schema = PromotionCategorySchema(many=True)


# Define the PromotionRestaurant schema
class PromotionRestaurantSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'image_url', 'title', 'subtitle', 'rating', 'promotion_category_id')

# Initialize the PromotionRestaurant schema
promotion_restaurant_schema = PromotionRestaurantSchema()
promotion_restaurants_schema = PromotionRestaurantSchema(many=True)


# Define the API endpoints for the PromotionMainItem model
@app.route('/promotion_main_item', methods=['GET'])
def get_promotion_main_items():
    promotion_main_items = mongo.db.promotion_main_item.find()
    return promotion_main_items_schema.jsonify(promotion_main_items)

@app.route('/promotion_main_item', methods=['POST'])
def add_promotion_main_item():
    image_url = request.json['image_url']
    promotion_main_item = {'image_url': image_url}
    result = mongo.db.promotion_main_item.insert_one(promotion_main_item)
    new_promotion_main_item = mongo.db.promotion_main_item.find_one({'_id': result.inserted_id})
    return promotion_main_item_schema.jsonify(new_promotion_main_item)


# Define the API endpoints for the PromotionCategory model
@app.route('/promotion_category', methods=['GET'])
def get_promotion_categories():
    promotion_categories = mongo.db.promotion_category.find()
    return promotion_categories_schema.jsonify(promotion_categories)

@app.route('/promotion_category', methods=['POST'])
def add_promotion_category():
    title = request.json['title']
    subtitle = request.json['subtitle']
    promotion_category = {'title': title, 'subtitle': subtitle}
    result = mongo.db.promotion_category.insert_one(promotion_category)
    new_promotion_category = mongo.db.promotion_category.find_one({'_id': result.inserted_id})
    return promotion_category_schema.jsonify(new_promotion_category)


# Define the API endpoints for the PromotionRestaurant model
@app.route('/promotion_restaurant', methods=['GET'])
def get_promotion_restaurants():
    promotion_restaurants = mongo.db.promotion_restaurant.find()
    return promotion_restaurants_schema.jsonify(promotion_restaurants)

@app.route('/promotion_restaurant', methods=['POST'])
def add_promotion_restaurant():
    image_url = request.json['image_url']
    title = request.json['title']
    subtitle = request.json['subtitle']
    rating = request.json['rating']
    promotion_category_id = request.json['promotion_category_id']
    promotion_restaurant = {'image_url': image_url, 'title': title, 'subtitle': subtitle, 'rating': rating,'promotion_category_id': promotion_category_id}
        # create an instance of the PromotionRestaurant model using the provided data
    new_promotion_restaurant = PromotionRestaurant(**promotion_restaurant)
    # save the new promotion restaurant to the database
    new_promotion_restaurant.save()
    # return a response indicating success
    return jsonify({'message': 'Promotion restaurant added successfully.'}), 201

    
if __name__ == '__main__':
    app.debug = True
    app.run()
    