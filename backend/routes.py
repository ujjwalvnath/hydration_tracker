from flask import Blueprint, request, jsonify
from models import HydrationPlan, GlassSchedule, db

routes = Blueprint('routes', __name__)

@routes.route('/plans', methods=['POST'])
def create_plan():
    data = request.json
    plan = HydrationPlan(
        user_id=data['user_id'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        glasses_per_day=data['glasses_per_day']
    )
    db.session.add(plan)
    db.session.commit()

    for t in data['glass_times']:
        schedule = GlassSchedule(plan_id=plan.id, time_of_day=t)
        db.session.add(schedule)

    db.session.commit()
    return jsonify({'message': 'Plan created'}), 201

@routes.route('/plans/<date>', methods=['GET'])
def get_plan(date):
    plans = HydrationPlan.query.filter(HydrationPlan.start_date <= date, HydrationPlan.end_date >= date).all()
    result = []
    for plan in plans:
        result.append({
            'id': plan.id,
            'user_id': plan.user_id,
            'start_date': plan.start_date,
            'end_date': plan.end_date,
            'glasses_per_day': plan.glasses_per_day,
            'glass_times': [s.time_of_day for s in plan.schedules]
        })
    return jsonify(result)

@routes.route('/plans/<int:plan_id>', methods=['PUT'])
def update_plan(plan_id):
    data = request.json
    plan = HydrationPlan.query.get(plan_id)
    if plan:
        plan.start_date = data['start_date']
        plan.end_date = data['end_date']
        plan.glasses_per_day = data['glasses_per_day']
        GlassSchedule.query.filter_by(plan_id=plan_id).delete()
        for t in data['glass_times']:
            schedule = GlassSchedule(plan_id=plan.id, time_of_day=t)
            db.session.add(schedule)
        db.session.commit()
        return jsonify({'message': 'Plan updated'})
    return jsonify({'error': 'Plan not found'}), 404

@routes.route('/plans/<int:plan_id>', methods=['DELETE'])
def delete_plan(plan_id):
    plan = HydrationPlan.query.get(plan_id)
    if plan:
        db.session.delete(plan)
        db.session.commit()
        return jsonify({'message': 'Plan deleted'})
    return jsonify({'error': 'Plan not found'}), 404
