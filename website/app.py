from __init__ import create_app


app = create_app()

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)