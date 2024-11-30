from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime
import logging

# Set up logging for scheduler
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def reminder_job():
    # This function can send reminders or notifications
    logger.info(f"Reminder sent at {datetime.now()}")

def job_listener(event):
    if event.exception:
        logger.error(f"Job failed: {event.job_id}")
    else:
        logger.info(f"Job {event.job_id} executed successfully.")

def start_scheduler():
    # Initialize the scheduler
    scheduler = BackgroundScheduler()
    
    # Add job to send reminders every day at 9 AM (for example)
    scheduler.add_job(reminder_job, 'interval', hours=24, start_date='2024-11-30 09:00:00')
    
    # Add a listener for job events (e.g., job execution or error)
    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    
    # Start the scheduler
    scheduler.start()

    logger.info("Scheduler started.")
