from wtforms import Form, StringField, SelectField

class ProductSearchForm(Form):
    choices = [('Brand', 'Brand'),
               ('Product', 'Product'),]
    select = SelectField('Tìm kiếm điện thoại:', choices=choices)
    search = StringField('')
