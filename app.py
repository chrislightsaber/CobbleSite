from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Get the absolute path to the directory containing the script
base_dir = os.path.abspath(os.path.dirname(__file__))

# Construct the file path to data.xlsxC:\Users\Christopher_Muniz1\Desktop\CobbleWebsite
excel_file = os.path.join(base_dir, 'C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\CobbleDex.xlsx')

# Construct the file path to the templates
template_dir = os.path.join(base_dir, 'C:\\Users\\Christopher_Muniz1\\Desktop\\CobbleWebsite\\CobbleSite\\templates')

df = pd.read_excel(excel_file)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list')
def list():
    # Create a list to store the entries
    entries = []

    # Iterate over the DataFrame rows
    for _, row in df.iterrows():
        entry = {
            'Dex Entry': row['Dex Entry'],
            'Name': row['Name']
        }
        entries.append(entry)

    # Pass the data to the HTML template for the list page
    return render_template('list.html', entries=entries)


@app.route('/detail/<name>')
def detail(name):
    # Query the DataFrame for the selected entry
    entry = df[df['Name'] == name]

    # Pass the data to the HTML template for the detail page
    return render_template('detail.html', entry=entry)


if __name__ == '__main__':
    app.run()
