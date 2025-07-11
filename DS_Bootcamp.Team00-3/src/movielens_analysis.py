import sys
import pytest
from collections import OrderedDict

sys.path.append('../code-samples/')
from movies import Movies
from ratings import Ratings
from links import Links
from tags import Tags



class Tests:
    @staticmethod
    def test_dist_by_release():
        movies = Movies("../datasets/movies.csv")
        result = movies.dist_by_release()
        assert isinstance(result, OrderedDict)
        assert all(isinstance(year, str) for year in result.keys())
        assert all(isinstance(count, int) for count in result.values())

    @staticmethod
    def test_dist_by_genres():
        movies = Movies("../datasets/movies.csv")
        result = movies.dist_by_genres()
        assert isinstance(result, OrderedDict)
        assert all(isinstance(genre, str) for genre in result.keys())
        assert all(isinstance(count, int) for count in result.values())

    @staticmethod
    def test_most_genres():
        movies = Movies("../datasets/movies.csv")
        result = movies.most_genres(3)
        assert isinstance(result, OrderedDict)
        assert len(result) == 3
        assert all(isinstance(title, str) for title in result.keys())
        assert all(isinstance(count, int) for count in result.values())

    @staticmethod
    def test_ratings_dist_by_year():
        ratings = Ratings("../datasets/ratings.csv")
        movies = ratings.Movies(ratings.ratings)
        result = movies.dist_by_year()
        assert isinstance(result, dict)
        assert all(isinstance(year, int) for year in result.keys())
        assert all(isinstance(count, int) for count in result.values())

    @staticmethod
    def test_ratings_top_by_num_of_ratings():
        ratings = Ratings("../datasets/ratings.csv")
        movies = ratings.Movies(ratings.ratings)
        result = movies.top_by_num_of_ratings(5)
        assert isinstance(result, dict)
        assert len(result) == 5
        assert all(isinstance(movie_id, int) for movie_id in result.keys())
        assert all(isinstance(count, int) for count in result.values())

    #----------------------------------------------------------------------#
    @pytest.fixture
    def links(self):
        filepath = "../datasets/links_test.csv"
        return Links(filepath)

    @pytest.fixture
    def tags(self):
        filepath = "../datasets/tags.csv"
        return Tags(filepath)

    @staticmethod
    def test_links_types_get_imdb():
        res = Links.get_imdb(["0114709", "0113497"], [
                             'movieId', 'Director', 'Budget', 'Cumulative Worldwide Gross', 'Runtime'])
        assert isinstance(res, list) and all(
            isinstance(field, list) for field in res)

    @staticmethod
    def test_result_get_imdb():
        res = Links.get_imdb(["0114709"], [
                             'movieId', 'Director', 'Budget', 'Cumulative Worldwide Gross', 'Runtime'])
        assert res == [['0114709', 'John Lasseter',
                        '$30,000,000 (estimated)', '$394,436,586', '1 hour 21 minutes']]
        assert res == sorted(res, key=lambda x: int(x[0]), reverse=True)

    def test_links_types_top_directors(self, links):
        assert isinstance(links.top_directors(5), dict)

    def test_links_res_top_directors(self, links):
        res = links.top_directors(5)
        assert res['John Lasseter'] == 2
        assert res == dict(
            sorted(res.items(), key=lambda x: x[1], reverse=True))

    def test_links_types_most_expensive(self, links):
        assert isinstance(links.most_expensive(5), dict)

    def test_links_res_most_expensive(self, links):
        res = links.most_expensive(5)
        assert res['Джуманджи'] == 65000000
        assert res == dict(
            sorted(res.items(), key=lambda x: x[1], reverse=True))

    def test_links_types_most_profitable(self, links):
        assert isinstance(links.most_profitable(5), dict)

    def test_links_res_most_profitable(self, links):
        res = links.most_profitable(5)
        assert res['Джуманджи'] == 197821940
        assert res == dict(
            sorted(res.items(), key=lambda x: x[1], reverse=True))

    def test_links_types_longest(self, links):
        assert isinstance(links.longest(5), dict)

    def test_links_res_longest(self, links):
        res = links.longest(5)
        assert res['Джуманджи'] == 104
        assert res == dict(
            sorted(res.items(), key=lambda x: x[1], reverse=True))

    def test_links_types_cost_min(self, links):
        assert isinstance(links.top_cost_per_minute(5), dict)

    def test_links_res_cost_min(self, links):
        res = links.top_cost_per_minute(5)
        assert res['Джуманджи'] == 625000.00
        assert res == dict(
            sorted(res.items(), key=lambda x: x[1], reverse=True))

    def test_tags_types_most_words(self, tags):
        assert isinstance(tags.most_words(5), dict)

    def test_tags_res_most_words(self, tags):
        res = tags.most_words(10)
        assert res['heroine in tight suit'] == 4
        assert res == dict(
            sorted(res.items(), key=lambda x: x[1], reverse=True))

    def test_tags_types_longest(self, tags):
        assert isinstance(tags.longest(5), list)

    def test_tags_res_longest(self, tags):
        res = tags.longest(15)
        assert res[5] == 'Everything you want is here'

    def test_tags_types_most_words_and_longest(self, tags):
        assert isinstance(tags.most_words_and_longest(5), list)

    def test_tags_types_most_popular(self, tags):
        assert isinstance(tags.most_popular(5), dict)

    def test_tags_res_most_popular(self, tags):
        res = tags.most_popular(5)
        assert res == {'funny': 15, 'sci-fi': 14,
                       'twist ending': 12, 'dark comedy': 12, 'atmospheric': 10}

    def test_tags_types_tags_with_word(self, tags):
        assert isinstance(tags.tags_with_word('comedy'), list)

    def test_tags_res_tags_with_word(self, tags):
        res = tags.tags_with_word('comedy')
        assert res == ['black comedy', 'british comedy',
                       'comedy', 'dark comedy', 'romantic comedy']

if __name__ == "__main__":
    pytest.main()