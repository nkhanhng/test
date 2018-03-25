from flask import *
import mlab
from models.phone import Phone
from models.evaluate import Evaluate
from models.average import Average


mlab.connect()
app = Flask(__name__)

@app.route('/')
def index():
    phone_list = Phone.objects()
    return render_template('index.html', phone_list= phone_list)

@app.route('/phone')
def phone():
    phone = Phone.objects
    return render_template('Detail/phone.html', all_phones = phone)

@app.route('/danhgiasanpham/<proid>',methods = ['GET','POST'])
def evaluate(proid):

    if request.method == 'GET':
        phone = Phone.objects.with_id(proid)
        return render_template('Detail/detail.html',product = phone)
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

        return render_template("Detail/detail.html", average = "{0:.1f}".format(average), product = phone)

if __name__ == '__main__':
  app.run(debug=True)
