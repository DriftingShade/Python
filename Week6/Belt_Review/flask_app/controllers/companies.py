from flask_app import app
from flask_app.models.company import Company
from flask_app.models.user import User
from flask import flash, render_template, redirect, request, session


@app.route("/companies/all")
def companies():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    companies = Company.find_all_with_users()
    user = User.find_by_id(session["user_id"])
    return render_template("all_companies.html", companies=companies, user=user)

@app.get("/companies/new")
def new_companies():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    user = User.find_by_id(session["user_id"])
    return render_template("new_companies.html", user=user)

@app.post("/companies/create")
def create_companies():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    if not Company.form_is_valid(request.form):
        return redirect("/companies/new")
    
    Company.create(request.form)
    
    return redirect("/companies/all")

@app.get("/companies/<int:companies_id>")
def companies_details(companies_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    companies = Company.find_by_id_with_user(companies_id)
    user = User.find_by_id(session["user_id"])
    return render_template("companies_details.html", user=user, companies=companies)

@app.get("/companies/<int:companies_id>/edit")
def edit_companies(companies_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    companies = Company.find_by_id(companies_id)
    user = User.find_by_id(session["user_id"])
    return render_template("edit_companies.html", companies=companies, user=user)

@app.post("/companies/update")
def update_companies():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    companies_id = request.form["companies_id"]
    if not Company.form_is_valid(request.form):
        return redirect(f"/companies/{companies_id}/edit")
    
    Company.update(request.form)
    return redirect(f"/companies/{companies_id}")

@app.post("/companies/<int:companies_id>/delete")
def delete_companies(companies_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    Company.delete_by_id(companies_id)
    return redirect("/companies/all")
