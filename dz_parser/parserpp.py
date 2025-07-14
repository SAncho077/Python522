from ps import Parserss


def main():
    for i in range(1,14):
        pars = Parserss('https://www.sports.ru/news/', "dz_parser.txt")
        pars.run()
        pars.save(i)

if __name__ == '__main__':
    main()