import svgwrite
from datetime import datetime


def generate_svg_chart(data, width, height):
    # Преобразуем даты в метки времени
    data = [(datetime.strptime(date, "%Y-%m-%d"), rate) for date, rate in data]

    # Вычисляем минимальное и максимальное значение engagement_rate
    min_rate = min(data, key=lambda x: x[1])[1]
    max_rate = max(data, key=lambda x: x[1])[1]

    # Создаем объект SVG-файла
    dwg = svgwrite.Drawing('graph.svg', profile='tiny')

    # Рисуем полоску графика
    for i in range(len(data) - 1):
        x1 = (data[i][0] - data[0][0]).days / (data[-1][0] - data[0][0]).days * width
        x2 = (data[i+1][0] - data[0][0]).days / (data[-1][0] - data[0][0]).days * width
        y1 = height - ((data[i][1] - min_rate) / (max_rate - min_rate) * height)
        y2 = height - ((data[i+1][1] - min_rate) / (max_rate - min_rate) * height)

        dwg.add(dwg.line(start=(x1, y1), end=(x2, y2), stroke='black'))

    # Сохраняем SVG-файл
    dwg.save()


data = [
    ("2023-05-28", 0.5),
    ("2023-05-29", 0.3),
    ("2023-05-30", 0.8),
    ("2023-05-31", 0.6),
    ("2023-06-01", 0.9),
]

width = 100
height = 100

generate_svg_chart(data, width, height)
