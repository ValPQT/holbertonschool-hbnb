from app import create_app
"""The Entry Point file that will serve as the entry point
for running the application"""
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
