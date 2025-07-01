def health_check():
    from flask import jsonify

    response = {
        "status": "healthy"
    }
    return jsonify(response), 200