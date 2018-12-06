from flask import Flask, request, render_template, session, redirect, send_file
import csv
import pygal
from pygal.maps.world import World
df = 'dataset/joined_w_countries.csv'

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/map/<path>')
def map_page(path = None):
    map = generate_map(str(path))
    return render_template("index.html", data=map.render_data_uri())

@app.route('/data')
def data_page():
    data = line_chart()
    return render_template("index.html", data=data.render_data_uri())    

@app.route('/bar')
def bar_page():    
    bar = bar_chart()
    return render_template("index.html", data=bar.render_data_uri())   

@app.route('/pie/<path>')
def pie_page(path = None):   
    pie = pie_chart(int(path))
    return render_template("index.html", data=pie.render_data_uri())      

def generate_map(year):
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'Production vs Consumption - Year ' + year
    with open(df) as f:
        reader = csv.reader(f)
        for row in reader:
            if(row[3] == year):
                worldmap_chart.add(row[2], {
                str(row[6].lower()): [row[4], row[5]]
            })
        return worldmap_chart

def total_production(year):
    total_production = 0.0
    sum = 0
    firstline = True
    with open(df) as f:
        reader = csv.reader(f)
        for row in reader:
            if firstline:
                firstline = False
                continue
            if(int(row[3]) == year):
                total_production += float(row[4])
                sum = sum + 1
    return total_production / sum

def total_consumption(year):
    total_consumption = 0.0
    sum = 0
    firstline = True
    with open(df) as f:
        reader = csv.reader(f)
        for row in reader:
            if firstline:
                firstline = False
                continue
            if(int(row[3]) == year):
                total_consumption += float(row[5])
                sum = sum + 1
    return total_consumption / sum

def line_chart():
    line_chart = pygal.Line()
    line_chart.title = 'Prodcution and Consumption over the years'
    line_chart.x_labels = map(str, range(1991, 2014))
    line_chart.add('Consumption', [total_consumption(1991), total_consumption(1992), total_consumption(1993), total_consumption(1994), total_consumption(1995), total_consumption(1996), total_consumption(1997), total_consumption(1998), total_consumption(1999), total_consumption(2000), total_consumption(2001), total_consumption(2002), total_consumption(2003), total_consumption(2004), total_consumption(2005), total_consumption(2006), total_consumption(2007), total_consumption(2008), total_consumption(2009), total_consumption(2010), total_consumption(2011), total_consumption(2012), total_consumption(2013)])
    line_chart.add('Production',  [total_production(1991), total_production(1992), total_production(1993), total_production(1994), total_production(1995), total_production(1996), total_production(1997), total_production(1998), total_production(1999), total_production(2000), total_production(2001), total_production(2002), total_production(2003), total_production(2004), total_production(2005), total_production(2006), total_production(2007), total_production(2008), total_production(2009), total_production(2010), total_production(2011), total_production(2012), total_production(2013)])
    return line_chart

def bar_chart():
    line_chart = pygal.Bar()
    line_chart.title = 'Prodcution and Consumption over the years'
    line_chart.x_labels = map(str, range(1991, 2014))
    line_chart.add('Consumption', [total_consumption(1991), total_consumption(1992), total_consumption(1993), total_consumption(1994), total_consumption(1995), total_consumption(1996), total_consumption(1997), total_consumption(1998), total_consumption(1999), total_consumption(2000), total_consumption(2001), total_consumption(2002), total_consumption(2003), total_consumption(2004), total_consumption(2005), total_consumption(2006), total_consumption(2007), total_consumption(2008), total_consumption(2009), total_consumption(2010), total_consumption(2011), total_consumption(2012), total_consumption(2013)])
    line_chart.add('Production', [total_production(1991), total_production(1992), total_production(1993), total_production(1994), total_production(1995), total_production(1996), total_production(1997), total_production(1998), total_production(1999), total_production(2000), total_production(2001), total_production(2002), total_production(2003), total_production(2004), total_production(2005), total_production(2006), total_production(2007), total_production(2008), total_production(2009), total_production(2010), total_production(2011), total_production(2012), total_production(2013)])
    return line_chart

def pie_chart(year):
    pie_chart = pygal.Pie()
    pie_chart.title = 'Production vs Consumption ' + str(year)
    pie_chart.add('Production', total_production(year))
    pie_chart.add('Consumption', total_consumption(year))
    return pie_chart

if __name__ == "__main__":
    app.run(host='0.0.0.0')
