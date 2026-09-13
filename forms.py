from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, DateField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Length

class TaskForm(FlaskForm):
    title = StringField('Task Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[Length(max=500)])
    deadline = DateField('Deadline (YYYY-MM-DD)', validators=[DataRequired()], format='%Y-%m-%d')
    urgency = IntegerField('Urgency (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    business_impact = IntegerField('Business Impact (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    estimated_effort = FloatField('Estimated Effort (Hours)', validators=[DataRequired(), NumberRange(min=0.1)])
    dependencies = IntegerField('Dependencies (Count)', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Save Task')

class OverrideForm(FlaskForm):
    new_priority = StringField('New Priority (Low, Medium, High, Critical)', validators=[DataRequired()])
    reason = TextAreaField('Reason for Override', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Override Priority')

class EditProfileForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email Address', validators=[DataRequired(), Length(max=150)])
    submit = SubmitField('Save Changes')

class ChangePasswordForm(FlaskForm):
    current_password = StringField('Current Password', validators=[DataRequired()])
    new_password = StringField('New Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Update Password')
