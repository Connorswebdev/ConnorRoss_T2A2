from __init__ import create_app, DevelopmentConfig

app = create_app(config_class=DevelopmentConfig)

if __name__ == '__main__':
    app.run(debug=True)