from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from salesapp import db
from datetime import datetime
from salesapp import app


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)



class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Dien thoai')
        # c2 = Category(name='May tinh bang')
        # c3 = Category(name='Dong ho thong minh')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        #
        # db.session.commit()
        products = [{
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
        }]

        for p in products:
            pro = Product(name=p['name'], price=p['price'], image=p['image'],
                          description=p['description'], category_id=p['category_id'])
            db.session.add(pro)

        db.session.commit()