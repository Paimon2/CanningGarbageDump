from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import send_file
from flask import make_response
from flask import request
from fpdf import FPDF
import random
import sqlite3

app = Flask("main")


conn = sqlite3.connect("garbagedump.db", check_same_thread=False)
c = conn.cursor()

def safe_get_cookies(cookiename):
    val = request.cookies.get(cookiename)
    if val == None:
        return 0
    return int(val)


sql_create_projects_table =  "CREATE TABLE IF NOT EXISTS orders (id integer PRIMARY KEY, email text, qty1 int, qty2 int, qty3 int, qty4 int);"
c.execute(sql_create_projects_table)

@app.route('/checkout', methods=['POST'])
def do_login():
   email = request.form['email']
   qty1 = safe_get_cookies("qty1")
   qty2 = safe_get_cookies("qty2")
   qty3 = safe_get_cookies("qty3")
   qty4 = safe_get_cookies("qty4")
   e = "ee"
   # add to db
   no = str(random.randint(1, 99999))
   params = (no, email, qty1, qty2, qty3, qty4)
   c.execute("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)", params)

   # Gen PDF

   pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
   pdf.add_page()
   pdf.set_font('Arial', 'B', 24)
   pdf.cell(0, ln=1, h=20, txt='Receipt from Canning Garbage Dump')
   pdf.set_font('Arial', 'BI', 20)
   pdf.cell(w=20, ln=1, h=20, txt='Thank you for your purchase, we will be in contact shortly.')
   pdf.set_font('Arial', '', 18)
   pdf.cell(w=20, ln=1, h=20, txt='Email: ' + email)
   pdf.cell(w=20, ln=1, h=20, txt='1-5kg: Quantity: ' + str(qty1))
   pdf.cell(w=20, ln=1, h=20, txt='5-10kg: Quantity: ' + str(qty2))
   pdf.cell(w=20, ln=1, h=20, txt='10-15kg: Quantity: ' + str(qty3))
   pdf.cell(w=20, ln=1, h=20, txt='15+kg: Quantity: ' + str(qty4))
   pdf.output('PDF-1.pdf')
   return send_file("PDF-1.pdf")
   

@app.route('/')
def serve_index():
    return render_template('/index.html', msg=None)

@app.route('/cart')
def serve_cart():
    return render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    )

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory("work", path)

@app.route('/add_cart_1')
def add_cart_1():
    resp = make_response(render_template('/index.html', msg="1-5kg of rubbish added to cart!"))
    resp.set_cookie('qty1', str(safe_get_cookies('qty1') + 1))
    return resp

@app.route('/rem_cart_1')
def rem_cart_1():
    resp = make_response(render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    ))
    resp.set_cookie('qty1', str(max(safe_get_cookies('qty1') - 1, 0)))
    return resp
	
@app.route('/addd_cart_1')
def addd_cart_1():
    resp = make_response(render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    ))
    resp.set_cookie('qty1', str(safe_get_cookies('qty1') + 1))
    return resp

@app.route('/addd_cart_2')
def addd_cart_2():
    resp = make_response(render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    ))
    resp.set_cookie('qty2', str(safe_get_cookies('qty2') + 1))
    return resp

@app.route('/addd_cart_3')
def addd_cart_3():
    resp = make_response(render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    ))
    resp.set_cookie('qty3', str(safe_get_cookies('qty3') + 1))
    return resp

@app.route('/addd_cart_1')
def addd_cart_4():
    resp = make_response(render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    ))
    resp.set_cookie('qty4', str(safe_get_cookies('qty4') + 1))
    return resp

@app.route('/add_cart_2')
def add_cart_2():
    resp = make_response(render_template('/index.html', msg="5-10kg of rubbish added to cart!"))
    resp.set_cookie('qty1', str(safe_get_cookies('qty1')))
    return resp

@app.route('/rem_cart_2')
def rem_cart_2():
    resp = make_response(render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    ))
    resp.set_cookie('qty2', str(max(safe_get_cookies('qty2') - 1, 0)))
    return resp

@app.route('/add_cart_3')
def add_cart_3():
    resp = make_response(render_template('/index.html', msg="10-15kg of rubbish added to cart!"))
    resp.set_cookie('qty3', str(safe_get_cookies('qty3') + 1))
    return resp

@app.route('/rem_cart_3')
def rem_cart_3():
    resp = make_response(render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    ))
    resp.set_cookie('qty3', str(max(safe_get_cookies('qty3') - 1, 0)))
    return resp

@app.route('/add_cart_4')
def add_cart_4():
    resp = make_response(render_template('/index.html', msg="15+kg of rubbish added to cart!"))
    resp.set_cookie('qty4', str(safe_get_cookies('qty4') + 1))
    return resp

@app.route('/rem_cart_4')
def rem_cart_4():
    resp = make_response(render_template('/cart.html',
    qty1=safe_get_cookies('qty1'),
    qty2=safe_get_cookies('qty2'),
    qty3=safe_get_cookies('qty3'),
    qty4=safe_get_cookies('qty4'),
    ))
    resp.set_cookie('qty4', str(max(safe_get_cookies('qty4') - 1, 0)))
    return resp

app.run(host='0.0.0.0', port=8000, debug=True)
