from flask import Flask, redirect, url_for, request, render_template, session
from core.oauth import init_oauth
from db.models import User, Transaction, Base
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from db.database import Base, engine
from datetime import datetime, timedelta
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# init database
Base.metadata.create_all(engine)

# init OAuth
google = init_oauth(app)
Session = sessionmaker(bind=engine)
db_session = Session()

# init SQLAlchemy session

@app.route("/")
def home():
    user_data = None
    period = request.args.get('period', 'month')  # default to month
    
    with Session() as db_session:
        if "user_id" in session:
            user = db_session.get(User, session["user_id"])
            if user:
                # คำนวณช่วงเวลา
                today = datetime.now()
                if period == 'week':
                    start_date = today - timedelta(days=7)
                elif period == 'year':
                    start_date = today - timedelta(days=365)
                else:  # month
                    start_date = today - timedelta(days=30)

                # ดึงข้อมูลตามช่วงเวลา
                sum_income = (
                    db_session.query(func.sum(Transaction.amount))
                    .filter(
                        Transaction.user_id == user.id,
                        Transaction.type_ == "income",
                        Transaction.date >= start_date
                    )                   
                    .scalar() or 0
                )
                
                sum_expense = (
                    db_session.query(func.sum(Transaction.amount))
                    .filter(
                        Transaction.user_id == user.id,
                        Transaction.type_ == "expense",
                        Transaction.date >= start_date
                    )
                    .scalar() or 0
                )
                
                user_data = {
                    "username": user.username,
                    "email": user.email,
                    "sum_income": sum_income,
                    "sum_expense": sum_expense
                }
                
    return render_template("index.html", user_data=user_data, period=period)

@app.route("/login")
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route("/login/callback")
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()

    with Session() as db_session:
        user = db_session.query(User).filter_by(provider="google", google_id=str(user_info["sub"])).first()
        if not user:
            user = User(
                google_id=str(user_info["sub"]),
                username=user_info.get("name", f"User{user_info['sub'][-6:]}"),
                email=user_info.get("email"),
                provider="google",
                date_joined=datetime.now(),
                last_active=datetime.now()
            )
            db_session.add(user)
        else:
            user.last_active = datetime.now()
        
        db_session.commit()
        session["user_id"] = user.id
    # return username, email to @app.route("/")
    return f"""
    <script>
        window.opener.postMessage({{'username': '{user.username}', 'email': '{user.email}'}}, "{request.host_url}");  
        window.close();
    </script>
    """
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home")) 

@app.route("/add-income", methods=['POST'])
def add_income():
    if "user_id" not in session:
        return redirect(url_for('home'))
        
    amount = request.form.get('amount')
    category = request.form.get('category')
    
    with Session() as db_session:
        transaction = Transaction(
            user_id=session["user_id"],
            amount=float(amount),
            type_="income",
            category=category
        )
        db_session.add(transaction)
        db_session.commit()
    
    return redirect(url_for('home'))

@app.route("/add-expense", methods=['POST'])
def add_expense():
    if "user_id" not in session:
        return redirect(url_for('home'))
        
    amount = request.form.get('amount')
    category = request.form.get('category')
    
    with Session() as db_session:
        transaction = Transaction(
            user_id=session["user_id"],
            amount=float(amount),
            type_="expense",
            category=category
        )
        db_session.add(transaction)
        db_session.commit()
    
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
