from datetime import time
from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class HydrationPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    glasses_per_day = db.Column(db.Integer, nullable=False)
    schedules = db.relationship('GlassSchedule', backref='plan', lazy=True)

class GlassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('hydration_plan.id'), nullable=False)
    time_of_day = db.Column(db.String, nullable=False)
