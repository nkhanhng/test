from flask import *
import mlab
from models.phone import Phone
from models.evaluate import Evaluate
from models.average import Average
from forms.forms import ProductSearchForm
from models.brand import Brand

mlab.connect()
app = Flask(__name__)

def brandname():
    phone = Phone.objects()
    brand_name_list = []
    brand_name =""
    for item in phone:
        if brand_name != item.phone_brand_name:
            brand_name = item.phone_brand_name
            brand_name_list.append(brand_name)
    return(brand_name_list)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # phone_list = Phone.objects()
        SP_ordered = Average.objects().order_by("-averagePoint")
        top4 = []
        brand_name_list = brandname()
        for i in SP_ordered[0:4]:
            phone_dict = {}
            phone_dict["phone"] = Phone.objects.get(id=i.phone.id)
            phone_dict["averagePoint"] = round(i.averagePoint, 1)
            top4.append(phone_dict)
        return render_template('index.html', top4=top4,brand_name_list = brand_name_list)

    elif request.method == "POST":


        return redirect("/result")

@app.route('/compare', methods = ["GET", "POST"])
def compare():
    if request.method == "GET":

        return render_template('compare.html')
    elif request.method == "POST":
        return redirect("/result")

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "GET":
        SP_ordered = Phone.objects()
        phone_li1 = SP_ordered[0:3]
        phone_li2 = SP_ordered[4:7]
        print(phone_li1[0].product_name)
        print(phone_li2[0].product_name)
        return render_template('result.html', phone_li1=phone_li1, phone_li2=phone_li2)
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        return "a"

@app.route('/hang-dien-thoai')
def cac_hang_dien_thoai():
    brand = Brand.objects()
    brand_name_list = brandname()
    return render_template('hang-dien-thoai.html', brand_name_list = brand_name_list, brand = brand)

@app.route('/hang-dien-thoai/<brand_name>')
def chi_tiet_hang_dien_thoai(brand_name):
    brand_name_list = brandname()
    phone = Phone.objects()
    phone_list = []
    phone_data = []
    for item in phone:
        if item.phone_brand_name == brand_name:
            phone_data.append(item)
    return render_template('dien-thoai-cua-hang.html',phone = phone_data, brand_name = brand_name, brand_name_list = brand_name_list)

@app.route('/danhgiasanpham/<proid>',methods = ['GET','POST'])
def evaluate(proid):
    if request.method == 'GET':
        phone = Phone.objects.with_id(proid)
        for evaluated in Average.objects():
            if evaluated.phone.id == phone.id:
                n = round(evaluated['averagePoint'])
                R = round((255 * (5 - n)) / 5)
                G = round((255 * n) / 5)
                B = 0
                return render_template('Detail/product_detail.html',product = phone,red = R, green = G, blue = B, score = n)
    elif request.method == 'POST':
        designlist = []
        screenlist = []
        funclist = []
        explist = []
        camlist = []
        pinlist = []

        form = request.form
        phone = Phone.objects.get(id = proid)
        design = int(form['design'])
        print(design)
        screen = int(form['screen'])
        func = int(form['func'])
        exp = int(form['exp'])
        cam = int(form['cam'])
        pin = int(form['pin'])

        new_eva = Evaluate(phone = phone,
                           design = design,
                           screen = screen,
                           func = func,
                           exp = exp,
                           cam = cam,
                           pin = pin)


        new_eva.save()

        totalEva = Evaluate.objects(phone = phone)
        new_averagePoint = Average.objects.get(phone = phone)

        for object in totalEva:
            designlist.append(object['design'])
            screenlist.append(object['screen'])
            funclist.append(object['func'])
            explist.append(object['exp'])
            camlist.append(object['cam'])
            pinlist.append(object['pin'])


        designsum = sum(designlist)
        avgdesign = designsum / len(designlist)
        screensum = sum(screenlist)
        avgscreen = screensum/ len(designlist)
        funcsum = sum(funclist)
        avgfunc = funcsum / len(designlist)
        expsum = sum(explist)
        avgexp = expsum / len(designlist)
        camsum = sum(camlist)
        avgcam = camsum / len(designlist)
        pinsum = sum(pinlist)
        avgpin = pinsum / len(designlist)

        total = avgdesign + avgscreen + avgfunc + avgexp + avgcam + avgpin

        average = total / 6

        new_averagePoint.update(set__averagePoint = average)

        n = round(average)
        R = round((255 * (5 - n)) / 5)
        G = round((255 * n) / 5)
        B = 0

        return render_template("Detail/product_detail.html", score = "{0:.1f}".format(average), product = phone,red = R, green = G, blue = B)

if __name__ == '__main__':
  app.run(debug=True)
