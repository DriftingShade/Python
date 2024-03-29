from flask import flash
from datetime import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User


class Company:
    DB = "companies_db"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.information = data["information"]
        self.create_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None

    @staticmethod
    def form_is_valid(form_data):
        is_valid = True

        # Text Validator
        if len(form_data["name"]) == 0:
            flash("Please enter name.")
            is_valid = False
        elif len(form_data["name"]) < 3:
            flash("Name must be at least three characters.")
            is_valid = False

        if len(form_data["information"]) == 0:
            flash("Please enter information.")
            is_valid = False
        elif len(form_data["information"]) < 3:
            flash("Information must be at least three characters.")
            is_valid = False

        return is_valid

    @classmethod
    def find_all(cls):
        query = """SELECT * FROM companies JOIN users ON companies.user_id = users.id"""
        list_of_dicts = connectToMySQL(Company.DB).query_db(query)

        companies = []
        for each_dict in list_of_dicts:
            company = Company(each_dict)
            companies.append(company)
        return companies
    
    @classmethod
    def find_all_with_users(cls):
        query = """SELECT * FROM companies JOIN users ON companies.user_id = users.id"""

        list_of_dicts = connectToMySQL(Company.DB).query_db(query)

        companies = []
        for each_dict in list_of_dicts:
            company = Company(each_dict)
            user_data = {
                "id": each_dict["id"],
                "first_name": each_dict["first_name"],
                "last_name": each_dict["last_name"],
                "email": each_dict["email"],
                "password": each_dict["password"],
                "created_at": each_dict["created_at"],
                "updated_at": each_dict["updated_at"],
            }
            user = User(user_data)
            company.user = user
            companies.append(company)
        return companies
    
    @classmethod
    def find_by_id(cls, company_id):
        query = """SELECT * FROM companies WHERE id = %(company_id)s"""
        data = {"company_id": company_id}
        list_of_dicts = connectToMySQL(Company.DB).query_db(query, data)

        if len(list_of_dicts) == 0:
            return None
        
        company = Company(list_of_dicts[0])
        return company
    
    @classmethod
    def find_by_id_with_user(cls, company_id):
        query = """SELECT * FROM companies JOIN users ON companies.user_id = users.id 
        WHERE companies.id = %(company_id)s"""

        data = {"company_id": company_id}
        list_of_dicts = connectToMySQL(Company.DB).query_db(query, data)

        if len(list_of_dicts) == 0:
            return None
        
        company = Company(list_of_dicts[0])
        user_data = {
            "id": list_of_dicts[0]["users.id"],
            "first_name": list_of_dicts[0]["first_name"],
            "last_name": list_of_dicts[0]["last_name"],
            "email": list_of_dicts[0]["email"],
            "password": list_of_dicts[0]["password"],
            "created_at": list_of_dicts[0]["users.created_at"],
            "updated_at": list_of_dicts[0]["users.updated_at"],
        }
        company.user = User(user_data)
        return company
    
    @classmethod
    def create(cls, form_data):
        query = """INSERT INTO companies
        (name, information, user_id)
        VALUES
        (%(name)s, %(information)s, %(user_id)s)"""
        company_id = connectToMySQL(Company.DB).query_db(query, form_data)
        return company_id
    
    @classmethod
    def update(cls, form_data):
        query = """UPDATE companies
        SET
        name=%(name)s,
        information=%(information)s
        WHERE id = %(company_id)s;"""
        connectToMySQL(Company.DB).query_db(query, form_data)
        return
    
    @classmethod
    def delete_by_id(cls, company_id):
        query = """DELETE FROM companies WHERE id = %(company_id)s;"""
        data = {"company_id": company_id}
        connectToMySQL(Company.DB).query_db(query, data)
        return