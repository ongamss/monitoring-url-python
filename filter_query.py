from distutils.log import error
from dash import Dash, dash_table, html, dcc
import pandas as pd
from collections import OrderedDict
import requests
from dash.dependencies import Input, Output
import mysql.connector
from mysql.connector import Error

# funcao conexao com banco
def get_connection():
    connection = mysql.connector.connect(host='hostaddress',
                                         port='3306',
                                         database='databasename',
                                         user='user',
                                         password='password')
    return connection

# funcao endrecos das aplicacoes web
def get_enderecos():
    try:
        urls = []
        connection1 = get_connection()
        cursor1 = connection1.cursor()
        select_query1 = """select url from tabela1"""
        cursor1.execute(select_query1)
        records1 = cursor1.fetchall()
        for row1 in records1:
            urls.extend(row1)
        return urls

    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

    finally:
        connection1.close()

# funcao para pegar os nomes das aplicacoes
def get_aplicativos():
    try:
        aplicacoes = []
        connection2 = get_connection()
        cursor2 = connection2.cursor()
        select_query2 = """select app from tabela1"""
        cursor2.execute(select_query2)
        records2 = cursor2.fetchall()
        for row2 in records2:
            aplicacoes.extend(row2)
        return aplicacoes

    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
    finally:
        connection2.close()

# funcao para pegar local de implementacao
def get_implementado():
    try:
        implementadoem = []
        connection3 = get_connection()
        cursor3 = connection3.cursor()
        select_query = """select local from tabela1"""
        cursor3.execute(select_query)
        records3 = cursor3.fetchall()
        for row3 in records3:
            implementadoem.extend(row3)
        return implementadoem

    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
    finally:
        connection3.close()


# funcao verifica o codigo de status da url
def url_status(u):
    try:
        req = requests.get(u)
        return(f" status_code: {req.status_code}")

    except requests.exceptions.RequestException as e:
        return(f" is Not reachable")

# funcao para listar ON ou OFF para url testada
def url_checker(url):
    try:
        # Get Url
        get = requests.get(url)
        if get.status_code == 200:
            return("ON")
        else:
            return("OFF")
    # Exception
    except requests.exceptions.RequestException as e:
        # print URL with Errs
        #raise SystemExit(f"{url}: is Not reachable \nErr: {e}")
        return("ERROR")


# fucao para criar array com resultado dos testes
def monitoramento():
    stat1 = []
    # armazena status
    for x in (get_enderecos()):
        stat1.append(url_checker(x))
    return stat1

# funcao para criar array com resultados dos codigos
def codreturn():
    codstatus = []
    # armazena status
    for y in (get_enderecos()):
        codstatus.append(url_status(y))
    return codstatus

# Carregando os arrays
aplicativos = get_aplicativos()
on_ou_off = monitoramento()
sites = get_enderecos()
implementado = get_implementado()
error_code = codreturn()

# cria vetor de dados
data = OrderedDict(
    [
        ("APP", aplicativos),
        ("Status", on_ou_off),
        ("URL", sites),
        ("Local", implementado),
        ("Error_Code", error_code),
    ]
)

df = pd.DataFrame(data)

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df['id'] = df.index

app.layout = html.Div(children=[
    html.H1(
        children='Status URLs App Caema',
    ),
    dash_table.DataTable(
        id='table1',
        data=df.to_dict('records'),
        sort_action='native',
        columns=[
                    {'name': 'APP', 'id': 'APP', 'type': 'text', 'editable': False},
                    {'name': 'Status', 'id': 'Status','type': 'any', 'editable': False},
                    {'name': 'URL', 'id': 'URL', 'type': 'text', 'editable': False},
                    {'name': 'Local', 'id': 'Local','type': 'text', 'editable': False},
                    {'name': 'Error_Code', 'id': 'Error_Code','type': 'text', 'editable': False},
        ],
        editable=False,
        style_cell_conditional=[
            {
                'if': {
                    'column_id': 'Status',
                },
                'width': '6%',
                'text-align': 'center',
            }
        ],
        style_data_conditional=[
            {
                'if': {
                    'column_id': 'Status',
                },
                'backgroundColor': 'green',
                'color': 'white'
            },
            {
                'if': {
                    'filter_query': '{Local} > 19 && {Local} < 41',
                    'column_id': 'Local'
                },
                'backgroundColor': 'tomato',
                'color': 'white'
            },
            {
                'if': {
                    # comparing columns to each other
                    'filter_query': '{Status} = OFF',
                    'column_id': 'Status'
                },
                'backgroundColor': 'red',
                'color': 'white'
            },
            {
                'if': {
                    # comparing columns to each other
                    'filter_query': '{Status} = ERROR',
                    'column_id': 'Status'
                },
                'backgroundColor': 'red',
                'color': 'white'
            },
            {
                'if': {
                    # comparing columns to each other
                    'filter_query': '{Delivery} > {APP}',
                    'column_id': 'Delivery'
                },
                'backgroundColor': '#3D9970'
            },
            {
                'if': {
                    'column_type': 'text'  # 'text' | 'any' | 'datetime' | 'numeric'
                },
                'textAlign': 'left'
            },

            {
                'if': {
                    'state': 'active'  # 'active' | 'selected'
                },
                'backgroundColor': 'rgba(0, 116, 217, 0.3)',
                'border': '1px solid rgb(0, 116, 217)'
            }

        ]
    ),
    dcc.Interval(
        id='interval-component',
        interval=10000,  # in milliseconds
        n_intervals=0
    ),

])

@app.callback(Output('table1', 'data'),
              Input('interval-component', 'n_intervals'))

def tableupdate(value):

    data = OrderedDict(
        [
            ("APP", get_aplicativos()),
            ("Status", monitoramento()),
            ("URL", get_enderecos()),
            ("Local", get_implementado()),
            ("Error_Code", codreturn()),
        ]
)
    df = pd.DataFrame(data)
    data=df.to_dict('records')  
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
