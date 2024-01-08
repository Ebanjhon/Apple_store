from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from apple_app import db, admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_admin import BaseView, expose
# admin login
class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __str__(self):
        return self.name

#loai san pham
class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name

class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    describe = Column(String(255), nullable=True, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100),
                   default='https://img.freepik.com/free-vector/glitch-error-404-page_23-2148105404.jpg')
    category_id = Column(Integer, ForeignKey(Category.id), nullable=True)

    def __str__(self):
        return self.name

class CategoryModelView(ModelView):
    form_columns = ('name',)
    can_edit = True
    can_export = True


class CustomProductView(ModelView):
    can_edit = True
    can_export = True

    form_columns = ('name', 'describe', 'price', 'image', 'category_id',)

    form_overrides = {
        'category_id': QuerySelectField
    }
    #
    # # Thiết lập options cho trường category
    form_args = {
        'category_id': {
            'query_factory': lambda: Category.query.all(),
            'allow_blank': False,
            'get_label': 'name',
        }
    }

    def on_model_change(self, form, model, is_created):
        model.category_id = form.category_id.data.id
        super().on_model_change(form, model, is_created)


class AboutMeView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/about-me.html')

admin.add_view(CategoryModelView(Category, db.session))
admin.add_view(CustomProductView(Product, db.session))
admin.add_view(AboutMeView(name="About me"))


# if __name__ == "__main__":
#     from apple_app import app
#     with app.app_context():
#         db.create_all()
#
#         c1 = Category(name='Macbook')
#         c2 = Category(name='iPad')
#         db.session.add(c1)
#         db.session.add(c2)
#         db.session.commit()
#
#         p1 = Product(name='MacBook Air 2020', price=22000000, category_id=1,describe='Cấu hình Macbook Pro M2 2022 rất mạnh mẽ với chip Apple M2',
#                      image="static/image/macbookair1.png")
#         p2 = Product(name='MacBook Air M2', price=50000000, category_id=1,
#                      describe='Về thiết kế phải nói là MacBook Air M2 khá tuyệt vời',
#                      image="static/image/macbookairm2.png")
#         p3 = Product(name='iPad gen9', price=10000000, category_id=2,
#                      describe='iPad Gen 9 sở hữu thiết kế hình chữ nhật quen thuộc với lớp vỏ ngoài aluminum sáng bóng',
#                      image="static/image/ipadgen9.png")
#
#         db.session.add_all([p1, p2, p3])
#         db.session.commit()
