from sqlalchemy import Column, Enum, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from salesapp import db
from datetime import datetime
from salesapp import app
from enum import Enum as UserEnum

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)




class Category(BaseModel):
    __tablename__ = 'category'

    products = relationship('Product', backref='category', lazy=True)


    def __str__(self):
        return self.name

product_tag = db.Table('product_tag',
                       Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
                       Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True))


class Product(BaseModel):
    __tablename__ = 'product'

    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    tags = relationship('Tag', secondary='product_tag', lazy='subquery',
                        backref=backref('product', lazy=True))

    def __str__(self):
        return self.name

class UserRole(UserEnum):
    ADMIN = 1
    USER = 2

class User(BaseModel):
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    email = Column(String(50))
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name

class Tag(db.Model):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Dien thoai')
        # c2 = Category(name='May tinh bang')
        # c3 = Category(name='Dong ho thong minh')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        #
        # t1 = Tag(name='promotion')
        # t2 = Tag(name='new')
        # db.session.add(t1)
        # db.session.add(t2)
        # db.session.commit()
        # pt = product_tag(product_id=1, tag_id=1)
        # pt2 = product_tag(product_id=2, tag_id=2)
        # pt3 = product_tag(product_id=3, tag_id=1)
        # pt4 = product_tag(product_id=4, tag_id=2)
        # pt5 = product_tag(product_id=5, tag_id=1)
        # pt6 = product_tag(product_id=6, tag_id=2)
        # pt7 = product_tag(id=1, product_id=7, tag_id=1)
        # pt8 = product_tag(id=1, product_id=8, tag_id=2)
        # pt9 = product_tag(id=1, product_id=9, tag_id=1)
        # db.session.add(pt)
        # db.session.add(pt2)
        # db.session.add(pt3)
        # db.session.add(pt4)
        # db.session.add(pt5)
        # db.session.add(pt6)
        # db.session.add(pt7)
        # db.session.add(pt8)
        # db.session.add(pt9)
        # db.session.commit()
        # db.session.commit()
        # products = [{
        #  "id": 7,
        #  "name": "iPhone 6 Plus",
        #  "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #  "price": 15000000,
        #  "image":
        # "image/Black_3.jpg",
        #  "category_id": 3
        # }, {
        #  "id": 8,
        #  "name": "Tablet Pro 2020",
        #  "description": "Apple, 128GB, RAM: 6GB",
        #  "price": 27000000,
        #  "image":
        # "image/Blue_3.jpg",
        #  "category_id": 1
        # }, {
        #  "id": 9,
        #  "name": "Galaxy Z-Fold 2",
        # "description": "Samsung, 64GB, RAML: 6GB",
        #  "price": 34000000,
        #  "image":
        # "image/Gold_3.jpg",
        #  "category_id": 2
        # }, {
        #  "id": 1,
        #  "name": "iPhone 7 Plus",
        #  "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #  "price": 17000000,
        #  "image":
        # "image/Black_1.jpg",
        #  "category_id": 1
        # }, {
        #  "id": 2,
        #  "name": "iPad Pro 2020",
        #  "description": "Apple, 128GB, RAM: 6GB",
        #  "price": 37000000,
        #  "image":
        # "image/Blue_1.jpg",
        #  "category_id": 2
        # }, {
        #  "id": 3,
        #  "name": "Galaxy Note 10 Plus",
        # "description": "Samsung, 64GB, RAML: 6GB",
        #  "price": 24000000,
        #  "image":
        # "image/Gold_1.jpg",
        #  "category_id": 1
        # }, {
        #  "id": 4,
        #  "name": "iPhone 8 Plus",
        #  "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #  "price": 17000000,
        #  "image":
        # "image/Black_2.jpg",
        #  "category_id": 2
        # }, {
        #  "id": 5,
        #  "name": "Ipad 8 2020",
        #  "description": "Apple, 128GB, RAM: 6GB",
        #  "price": 25000000,
        #  "image":
        # "image/Blue_2.jpg",
        #  "category_id": 3
        # }, {
        #  "id": 6,
        #  "name": "Galaxy Z-Fold",
        # "description": "Samsung, 64GB, RAML: 6GB",
        #  "price": 14000000,
        #  "image":
        # "image/Gold_2.jpg",
        #  "category_id": 3
        # }]
        #
        # for p in products:
        #     pro = Product(name=p['name'], price=p['price'], image=p['image'],
        #                   description=p['description'], category_id=p['category_id'])
        #     db.session.add(pro)
        #
        # db.session.commit()