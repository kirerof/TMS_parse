from parse import ForChild, Books, Films, Games


def main():
    for_child = ForChild('https://play.google.com/store/apps/category/FAMILY?hl=ru&gl=US')
    for_child.get_html()
    for_child.parsing()
    for_child.save('for_child.json')

    books = Books('https://play.google.com/store/books?hl=ru&gl=US')
    books.get_html()
    books.parsing()
    books.save('books.json')

    films = Films('https://play.google.com/store/movies?hl=ru&gl=US')
    films.get_html()
    films.parsing()
    films.save('films.json')

    games = Games('https://play.google.com/store/games?hl=ru&gl=US')
    games.get_html()
    games.parsing()
    games.save('games.json')


if __name__ == '__main__':
    main()
