from flask import Blueprint, render_template, request, redirect

from app.models import (
    Book,
    Member,
    books,
    members,
    find_book,
    find_member,
    next_member_id,
)

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html", books=books, members=members)

@bp.route("/members")
def show_members():
    return render_template("members.html", members=members)

@bp.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        books.append(Book(
            request.form["title"],
            request.form["author"],
            request.form["isbn"],
        ))
        return redirect("/")
    return render_template("add_book.html")

@bp.route("/add_member", methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        members.append(Member(request.form["name"], next_member_id()))
        return redirect("/members")
    return render_template("add_member.html")

@bp.route("/delete_member/<int:member_id>")
def delete_member(member_id):
    member = find_member(member_id)
    if member:
        for book in list(member.borrowed_books):
            member.return_book(book)
        members.remove(member)
    return redirect("/members")

@bp.route("/delete_book/<title>")
def delete_book(title):
    book = find_book(title)
    if book:
        for member in members:
            if book in member.borrowed_books:
                member.return_book(book)
        books.remove(book)
    return redirect("/")

@bp.route("/borrow", methods=["GET", "POST"])
def borrow_book():
    if request.method == "POST":
        member_id = int(request.form["member_id"])
        title = request.form["title"]

        member = find_member(member_id)
        book = find_book(title)

        if member and book and not book.is_borrowed:
            member.borrow(book)
        return redirect("/")

    return render_template("borrow.html", books=books, members=members)

@bp.route("/return", methods=["GET", "POST"])
def return_book():
    if request.method == "POST":
        member_id_text, _, title = request.form.get("loan", "").partition("|")
        if member_id_text.isdigit() and title:
            member = find_member(int(member_id_text))
            book = find_book(title)
            if member and book:
                member.return_book(book)
        return redirect("/")

    return render_template("return.html", members=members)
