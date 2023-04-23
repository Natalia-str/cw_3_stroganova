from functions import get_data, filter_data, sort_data, formate_data

json_file = 'operations.json'
def main():
    data = get_data(json_file)
    data = filter_data(data)
    data = sort_data(data)
    data = formate_data(data)

    for row in data:
        print(row)


if __name__ == '__main__':
    main()
