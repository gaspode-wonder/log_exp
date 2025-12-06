from datetime import datetime
from app import db

class GeigerReading(db.Model):
    __tablename__ = "geiger_readings"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    counts_per_second = db.Column(db.Integer, nullable=False)
    counts_per_minute = db.Column(db.Integer, nullable=False)
    microsieverts_per_hour = db.Column(db.Float, nullable=False)
    mode = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return (
            f"<GeigerReading id={self.id} cps={self.counts_per_second} "
            f"cpm={self.counts_per_minute} µSv/h={self.microsieverts_per_hour} "
            f"mode={self.mode} timestamp={self.timestamp}>"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "counts_per_second": self.counts_per_second,
            "counts_per_minute": self.counts_per_minute,
            "microsieverts_per_hour": self.microsieverts_per_hour,
            "mode": self.mode,
        }
