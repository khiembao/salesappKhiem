from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from salesapp import db
from datetime import datetime
from salesapp import app


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)




class Category(BaseModel):
    __tablename__ = 'category'

    products = relationship('Product', backref='category', lazy=False)


    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'

    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    column_hide_backrefs = False

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        c1 = Category(name='Dien thoai')
        c2 = Category(name='May tinh bang')
        c3 = Category(name='Dong ho thong minh')

        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)

        db.session.commit()
        products = [{
         "id": 7,
         "name": "iPhone 6 Plus",
         "description": "Apple, 32GB, RAM: 3GB, iOS13",
         "price": 15000000,
         "image":
        "image/Black_3.jpg",
         "category_id": 3
        }, {
         "id": 8,
         "name": "Tablet Pro 2020",
         "description": "Apple, 128GB, RAM: 6GB",
         "price": 27000000,
         "image":
        "image/Blue_3.jpg",
         "category_id": 1
        }, {
         "id": 9,
         "name": "Galaxy Z-Fold 2",
        "description": "Samsung, 64GB, RAML: 6GB",
         "price": 34000000,
         "image":
        "image/Gold_3.jpg",
         "category_id": 2
        }, {
         "id": 1,
         "name": "iPhone 7 Plus",
         "description": "Apple, 32GB, RAM: 3GB, iOS13",
         "price": 17000000,
         "image":
        "image/Black_1.jpg",
         "category_id": 1
        }, {
         "id": 2,
         "name": "iPad Pro 2020",
         "description": "Apple, 128GB, RAM: 6GB",
         "price": 37000000,
         "image":
        "image/Blue_1.jpg",
         "category_id": 2
        }, {
         "id": 3,
         "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
         "price": 24000000,
         "image":
        "image/Gold_1.jpg",
         "category_id": 1
        }, {
         "id": 4,
         "name": "iPhone 8 Plus",
         "description": "Apple, 32GB, RAM: 3GB, iOS13",
         "price": 17000000,
         "image":
        "image/Black_2.jpg",
         "category_id": 2
        }, {
         "id": 5,
         "name": "Ipad 8 2020",
         "description": "Apple, 128GB, RAM: 6GB",
         "price": 25000000,
         "image":
        "image/Blue_2.jpg",
         "category_id": 3
        }, {
         "id": 6,
         "name": "Galaxy Z-Fold",
        "description": "Samsung, 64GB, RAML: 6GB",
         "price": 14000000,
         "image":
        "image/Gold_2.jpg",
         "category_id": 3
        }]

        for p in products:
            pro = Product(name=p['name'], price=p['price'], image=p['image'],
                          description=p['description'], category_id=p['category_id'])
            db.session.add(pro)

        db.session.commit()