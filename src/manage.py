from smart_shield.app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(port=3030)
