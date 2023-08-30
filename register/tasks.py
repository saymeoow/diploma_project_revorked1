from config.celery import app


@app.task
def profile_created(username):
    return print(username)
