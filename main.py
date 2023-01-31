from website import create_app

app = create_app()

# only run the web server if this file is invoked
if __name__ == '__main__':
    app.run(debug=True) 