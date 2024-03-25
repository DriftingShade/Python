from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    DB = "test_db"
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def create_post(cls, data):
        query = """INSERT INTO posts (content, created_at, updated_at, user_id)
        VALUES (%(content)s, NOW(), NOW(), %(user_id)s)"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        print(results)
        return results
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts;"
        print(query)
        results = connectToMySQL(cls.DB).query_db(query)
        print(results)
        posts = []
        for post in results:
            posts.append(cls(post))
        return posts