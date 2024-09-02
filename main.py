import csv
from collections import defaultdict
import matplotlib.pyplot as plt


def read_sales_data(file_path):
    sales = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4:
                product_name = row[0]
                quantity = int(row[1])
                price = float(row[2])
                date = row[3]
                sales.append({
                    'product_name': product_name,
                    'quantity': quantity,
                    'price': price,
                    'date': date
                })
    return sales


def total_sales_per_product(sales_data):
    total_sales = defaultdict(float)

    for sale in sales_data:
        total_sales[sale['product_name']] += sale['quantity'] * sale['price']

    return total_sales


def sales_over_time(sales_data):
    sales_by_date = defaultdict(float)

    for sale in sales_data:
        sales_by_date[sale['date']] += sale['quantity'] * sale['price']

    return sales_by_date


def plot_sales_per_product(total_sales):
    products = list(total_sales.keys())
    sales_values = list(total_sales.values())

    plt.figure(figsize=(10, 5))
    plt.bar(products, sales_values, color='skyblue')
    plt.title('Общая сумма продаж по продуктам')
    plt.xlabel('Продукты')
    plt.ylabel('Сумма продаж ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_sales_over_time(sales_by_date):
    dates = list(sales_by_date.keys())
    sales_values = list(sales_by_date.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, sales_values, marker='o', color='orange')
    plt.title('Общая сумма продаж по дням')
    plt.xlabel('Даты')
    plt.ylabel('Сумма продаж ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main(file_path):
    sales_data = read_sales_data(file_path)

    total_sales = total_sales_per_product(sales_data)

    sales_by_date = sales_over_time(sales_data)

    max_product = max(total_sales, key=total_sales.get)
    max_product_sales = total_sales[max_product]

    max_date = max(sales_by_date, key=sales_by_date.get)
    max_date_sales = sales_by_date[max_date]

    print(f'Продукт с наибольшей выручкой: {max_product} (${max_product_sales:.2f})')
    print(f'Дата с наивысшей суммой продаж: {max_date} (${max_date_sales:.2f})')

    plot_sales_per_product(total_sales)
    plot_sales_over_time(sales_by_date)


if __name__ == "__main__":
    main('DataForStepikAss.txt')
