from market import app
from flask import render_template, redirect, url_for, flash, request
from market import db
from market.modules import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseForm, SellItemForm, ChangePasswordForm
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market', methods=['GET','POST'])
@login_required
def market_page():
    purchase_form = PurchaseForm()
    selling_form = SellItemForm()
    if request.method == 'POST':
        #Purchase Item
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name = purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f'Item: {p_item_object.name} Purchase Successfully!', category='Success')
            else:
                flash(f'Oops! Not enough balance to purchase item: {p_item_object.name}', category='Danger')

        #Sell Item
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Sold {s_item_object.name} back to market successfully!", category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name}", category='danger')

        return redirect (url_for('market_page'))

    if request.method=='GET':
        items = Item.query.filter_by(owner=None)

        owned_items = Item.query.filter_by(owner=current_user.id)
        if not items:
            return render_template('market.html', items=[], owned_items=owned_items, selling_form=selling_form)
        return render_template('market.html', items=items, purchase_form = purchase_form, owned_items=owned_items, selling_form=selling_form)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! you are now logged in as {user_to_create.username}', category='success')
        return redirect(url_for('market_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'error: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.password_check(form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash(f'Username and password are not matched! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out successfully!', category='info')
    return redirect(url_for('home_page'))

@app.route('/profile', methods=['POST','GET'])
@login_required
def profile_page():
    form=ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.password_check(form.old_password.data):
            current_user.password=form.new_password.data
            db.session.commit()
            flash('Password updated successfully', category='Success')
        else:
            flash('Old password is incorrect.', category='danger')
        return redirect(url_for('profile_page'))
    return render_template('profile.html', form=form)