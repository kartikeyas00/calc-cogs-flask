from flask import Flask, render_template, request, url_for, send_file
from werkzeug import secure_filename
from classes.cogs import calc_cogs

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/help')
def help():
   return render_template('help.html')

@app.route('/download_java_costing')
def download_java_costing():
   return send_file('files/Java_Costing.csv',
                     mimetype='text/csv',
                     attachment_filename='Java_Costing.csv',
                     as_attachment=True)

@app.route('/download_item_summary_csv')
def download_item_summary_csv():
   return send_file('files/item summary.csv',
                     mimetype='text/csv',
                     attachment_filename='item summary.csv',
                     as_attachment=True)

@app.route('/', methods = ['GET', 'POST'])
def upload_file_calculate():
   if request.method == 'POST':
      if ('goodsold' not in request.files) or ('costingsheet' not in request.files) :
         return render_template('upload.html')
      good_sold = request.files['goodsold']
      costing_sheet = request.files['costingsheet']
      if good_sold and costing_sheet:
         calc=calc_cogs(good_sold,costing_sheet)
         return render_template('upload.html',COGS=calc.calculate()[0],Profit=calc.calculate()[1],items=calc.calculate()[2])
		
if __name__ == '__main__':
   app.run(debug = True) 