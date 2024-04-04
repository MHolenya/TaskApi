from flask import Blueprint, jsonify, request
from task_api.models.database import db_session
from task_api.models.category import Category
from sqlalchemy.exc import SQLAlchemyError

# Create a Blueprint called 'tasks' to organize routes related to tasks
category_bp = Blueprint('category', __name__)


# Route to display all categories
@category_bp.route('/categories', methods=['GET'])
def get_all_categories():
    try:
        # Retrieve all categories from the database
        categories = Category.query.all()
        # Use a list comprehension to create the list of category data
        categories_list: list = [{'category_id': category.category_id,
                                  'name': category.name}
                                 for category in categories]

        # Return JSON response with list of categories
        return jsonify({'categories': categories_list})
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': f'Error retrieving categories: {e}'}), 500


# Route to get category by name
@category_bp.route('/category/name/<name>', methods=['GET'])
def get_category_by_name(name):
    try:
        category = Category.query.filter_by(name=name).first()
        category_id = category.category_id
        category_name = category.name
        category_res = {'id': category_id, 'name': category_name}
        # Return JSON response with a category
        return jsonify(category_res), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': f'Error retrieving category: {e}'}), 500


# Route to get category by id
@category_bp.route('/category/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    try:
        category = Category.query.filter_by(category_id=category_id).first()
        category_id = category.category_id
        category_name = category.name
        category_res = {'id': category_id, 'name': category_name}
        # Return JSON response with a category
        return jsonify(category_res), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': f'Error retrieving category: {e}'}), 500


# Route to add a new category
@category_bp.route('/category', methods=['POST'])
def post_category():
    try:
        request_body = request.json()
        name = request_body.get('name')
        # Check the name is valid
        if not name or name is not str:
            return jsonify({'message': 'Missing valid name field'}), 400

        # Add new category to the database
        new_category = Category(name=name)
        db_session.add(new_category)
        db_session.commit()

        # Return successful creation message with category
        return jsonify({'message': 'Category added succesfully'}), 201

    except SQLAlchemyError as e:
        db_session.rollback()
        return jsonify({'error': str(e)}), 500


# Route to delete a new category
@category_bp.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        category = Category.query.get(category_id)

        if category:

            db_session.delete(category)
            db_session.commit()

            return jsonify({'message': 'Category deleted successfully'})

        else:
            return jsonify({'message': 'Category not found'}), 404

    except SQLAlchemyError as e:
        # Rollback in case of any database error
        db_session.rollback()
        return jsonify({'error': str(e)}), 500
