import os
import unittest
import json

from flaskr import create_app
from models import setup_db, Book

class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres', 'eazye5000', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
                'title': 'Anansi Boys',
                'author': 'Neil Gaiman',
                'rating': 5
                } 

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_paginated_books(self):
        res = self.client().get('/books')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_books'])
        self.assertTrue(len(data['books']))

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/books?page=1000', json={'rating': 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_update_book_rating(self):
        res = start.client().patch('/books/5', json={'rating': 1})
        data - json.loads(res.data)
        book = Book.query.filter(Book.id == 5).one_ornone()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(book.format()['rating'], 1)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
