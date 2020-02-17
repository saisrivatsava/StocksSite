
from flask               import Flask, render_template, request, url_for, redirect, send_from_directory

from models import get_stock_data


app = Flask(__name__)



# App main route + generic routing
@app.route('/', defaults={'path': 'consolidated.html'})
@app.route('/<path>')
def index(path):
    try:
        data = get_stock_data.get_stock_info("TCS.NS")
        print(data)
        # try to match the pages defined in -> pages/<input file>
        return render_template( 'pages/'+path , stock_summary = data)

    except Exception  as e:
        print(e)

        return render_template( 'pages/error-404.html')

if __name__ == '__main__':
    app.run(debug=True)