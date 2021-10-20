from lib.flask_mailplus import send_template_message
from snakeeyes.app import create_celery_app

celery = create_celery_app()


@celery.task()
def deliver_feedback_email(email, message):
    """
    Send a feedback e-mail.

    :param email: E-mail address of the visitor
    :type user_id: str
    :param message: E-mail message
    :type user_id: str
    :return: None
    """
    ctx = {'email': email, 'message': message}

    send_template_message(subject='[Snake Eyes] Feedback',
                          sender=email,
                          recipients=[celery.conf.get('MAIL_USERNAME')],
                          reply_to=email,
                          template='feedback/mail/index', ctx=ctx)

    return None
