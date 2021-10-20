from snakeeyes.extensions import mail
from snakeeyes.blueprints.feedback.tasks import deliver_feedback_email


class TestTasks(object):
    def test_deliver_support_email(self):
        """ Deliver a feedback email. """
        form = {
          'email': 'foo@bar.com',
          'message': 'Test message from Snake Eyes.'
        }

        with mail.record_messages() as outbox:
            deliver_feedback_email(form.get('email'), form.get('message'))

            assert len(outbox) == 1
            assert form.get('email') in outbox[0].body
