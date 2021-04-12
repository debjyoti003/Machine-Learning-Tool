from flask import Flask, flash, redirect, render_template, request, session, abort
import pandas as pd
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = r'C:\Users\DEBJYOTI BANERJEE\Documents\My Machine Learning Tool\uploaded files'

# @app.route("/")
# def hello():
#     return render_template('Home_page.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        data = pd.read_csv(request.files.get('file'))
        df = pd.DataFrame(data)
        df2 = pd.DataFrame(df.describe(include = 'all'))
        df3 = pd.DataFrame(df.dtypes)
        
        # df3.columns = ['Column names', 'data_types']
        return render_template('upload.html', shape=df.shape, tables = [df.to_html(classes = 'data', header = "true")], titles = df.columns.values,
        describe_table = [df2.to_html(classes = 'data', header = "true")], titles2 = df2.columns.values, dtypes_table = [df3.to_html(classes = 'data', header = "true")],
        title3 = ['Column names', 'data_types'])
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug = True)