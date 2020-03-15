from flask import Flask, Markup, render_template, request,jsonify
import time
from sort_algorithm.sort_algorithm import SortAlgorithm
from threading import Thread

app = Flask(__name__)

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

sort_arr = SortAlgorithm(50, 50)
sort_arr.dict_arr['selection'] = sort_arr.random_array()
sort_arr.sleep = 0.01


@app.route('/_stuff', methods=['GET'])
def stuff():
    return jsonify(array=sort_arr.dict_arr['selection'],
                   sorted=sort_arr.dic_sorted['selection'],
                   detail=sort_arr.dict_gra_infor['selection'])


@app.route('/')
def hello():

    thr = Thread(target=sort_arr.selection_sort)
    thr.start()
    return render_template("index.html", arr_before=sort_arr.dict_arr['selection'])


@app.route('/response', methods=['POST'])
def response():
    fname = request.form.get("fname")
    note = request.form.get("note")
    return render_template("index.html", name=fname, note=note)


@app.route('/bar')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('bar_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=bar_labels, values=bar_values)


@app.route('/line')
def line():
    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=line_labels, values=line_values)


@app.route('/pie')
def pie():
    pie_labels = labels
    pie_values = values
    return render_template('pie_chart.html', title='Bitcoin Monthly Price in USD', max=17000, set=zip(values, labels, colors))


if __name__ == '__main__':
    app.run()
# arr2 = sort_arr.selection_sort()
# print(arr2)