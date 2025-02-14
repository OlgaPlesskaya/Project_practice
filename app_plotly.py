import dash
from dash import dcc, html, dash_table
from dash.dependencies import Output, Input
import requests

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Макет приложения
app.layout = html.Div([
    html.H1("Таблица данных"),
    dash_table.DataTable(
        id="table",
        columns=[
            {"name": "ID", "id": "identifier"},
            {"name": "Название", "id": "name"},
            {"name": "Дата", "id": "date"},
            {"name": "Поставщик", "id": "supplier"}
        ],
        style_cell={
            'textAlign': 'left'
        },
        style_header={
            'backgroundColor': '#4CAF50',
            'color': 'white',
            'fontWeight': 'bold'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#f2f2f2'
            }
        ],
        style_as_list_view=True
    ),
    dcc.Interval(
        id='interval-component',
        interval=5000,  # Обновление каждые 5 секунд (в миллисекундах)
        n_intervals=0
    )
])

# Функция обратного вызова для обновления таблицы
@app.callback(
    Output("table", "data"),
    Input("interval-component", "n_intervals")
)
def update_table(n):
    # Получение данных из API
    response = requests.get('http://localhost:8000/datasets/?format=json')
    data = response.json()
    
    return data

if __name__ == "__main__":
    app.run_server(debug=True)