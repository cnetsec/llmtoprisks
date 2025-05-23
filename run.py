from app import app

if __name__ == '__main__':
    # Running in debug mode (not recommended for production, can expose internals)
    app.run(host='0.0.0.0', port=5000, debug=True)
