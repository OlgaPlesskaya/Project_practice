# Импортируем необходимые пакеты
from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd
import requests
import plotly.express as px

# Инициализируем приложение
app = Dash()

# Определяем макет приложения
app.layout = html.Div(children=[
    html.H1(children='Список наборов данных'),
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # Обновление каждые 10 секунд
        n_intervals=0  # Начальное значение
    ),
    dash_table.DataTable(
        id='data-table',
        page_size=10,
        columns=[],
        data=[]
    ),
    dcc.Graph(
        id='supplier-graph'
    )
])

# Функция для получения данных из API
def fetch_data():
    response = requests.get('http://localhost:8000/datasets/?format=json')  # Замените на ваш URL API
    data = response.json()
    return pd.DataFrame(data)

# Callback для обновления таблицы и графика
@app.callback(
    Output('data-table', 'data'),
    Output('data-table', 'columns'),
    Output('supplier-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_content(n):
    df = fetch_data()
    
    # Обновление таблицы
    columns = [{"name": i, "id": i} for i in df.columns]
    
    # Подготовка данных для графика по поставщикам
    supplier_counts = df['supplier'].value_counts().reset_index()
    supplier_counts.columns = ['Supplier', 'Count']
    
    # Создание графика
    fig = px.bar(supplier_counts, x='Supplier', y='Count', title='Количество поставок по поставщикам')

    return df.to_dict('records'), columns, fig

# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)
