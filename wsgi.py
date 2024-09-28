import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

# wsgi.py

from App.controllers.competition import create_competition, get_competitions, get_competition_results
from App.controllers.result import import_results
from flask.cli import AppGroup
import click

competition_cli = AppGroup('competition')

@competition_cli.command('create')
@click.argument('name')
@click.argument('description')
@click.argument('date')
def create_new_competition(name, description, date):
    competition = create_competition(name, description, date)
    click.echo(f"Competition '{competition.name}' created successfully.")

@competition_cli.command('list')
def list_competitions():
    competitions = get_competitions()
    for competition in competitions:
        click.echo(f"ID: {competition.id}, Name: {competition.name}, Date: {competition.date}")

@competition_cli.command('results')
@click.argument('competition_id')
def view_competition_results(competition_id):
    results = get_competition_results(competition_id)
    if results:
        for result in results:
            click.echo(f"User ID: {result.user_id}, Score: {result.score}, Rank: {result.ranking}")
    else:
        click.echo(f"No results found for competition ID {competition_id}")

@competition_cli.command('import_results')
@click.argument('file_path')
@click.argument('competition_id')
def import_competition_results(file_path, competition_id):
    import_results(file_path, competition_id)
    click.echo(f"Results imported for competition ID {competition_id}")

# Register the CLI group with Flask's command line interface
app.cli.add_command(competition_cli)
