from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    # Ensure the application context is available
    with app.app_context():
        app.run(host="0.0.0.0", debug=True)
