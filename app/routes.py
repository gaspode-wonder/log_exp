from flask import Blueprint, jsonify
from app.models import GeigerReading

bp = Blueprint("routes", __name__)

@bp.route("/readings")
def get_readings():
    readings = GeigerReading.query.order_by(GeigerReading.timestamp.desc()).limit(50).all()
    return jsonify([r.to_dict() for r in readings])
