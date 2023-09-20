from salesapp import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from salesapp.models import Category, Product

admin = Admin(app=app, name="E-commerce Administration", template_mode="bootstrap4")

class ProductView(ModelView):
    can_view_details = True
    can_export = True
    column_display_all_relations = True
    column_list = ['name', 'description', 'price', 'image', 'active', 'created_date', 'category_id']
    column_searchable_list = ['name', 'description']
    column_filters = ['name', 'price']
    can_create = ['name', 'description', 'price', 'image', 'active', 'created_date', 'category_id']






admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))