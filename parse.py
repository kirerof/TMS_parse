from base import Parsing


class ForChild(Parsing):
    def parsing(self):
        result = {}
        blocks = self.html.select('section')

        for block in blocks:
            categories = block.select('.kcen6d')
            names = block.select('.Epkrse')

            if not names:
                names = block.select('.sT93pb.DdYX5.OnEJge')

            all_category_name = [name.text for name in names]
            result.update({category.text: all_category_name for category in categories})

        return result


class Books(Parsing):
    def parsing(self):
        result = {}
        blocks = self.html.select('section')

        for block in blocks:
            categories = block.select('.kcen6d')
            names = block.select('div[title]')
            all_category_name = [name.text for name in names]
            result.update({category.text: all_category_name for category in categories if category and names})

        return result


class Films(Parsing):
    def parsing(self):
        result = {}
        blocks = self.html.select('section')

        for block in blocks:
            categories = block.select('.kcen6d')
            names = block.select('div[title]')
            all_category_name = [name.text for name in names]
            result.update({category.text: all_category_name for category in categories if category and names})

        return result


class Games(Parsing):
    def parsing(self):
        result = {}
        blocks = self.html.select('section')

        for block in blocks:
            categories = block.select('.kcen6d')
            names = block.select('.sT93pb.DdYX5.OnEJge ')
            all_category_name = [name.text for name in names]
            result.update({category.text: all_category_name for category in categories if category and names})

        return result
