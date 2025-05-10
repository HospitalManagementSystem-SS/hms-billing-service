from app.models import BillingEvent, Invoice
from app.database import SessionLocal

def store_event_and_generate_invoice(event):
    db = SessionLocal()
    try:
        billing_event = BillingEvent(
            appointment_id=event["appointment_id"],
            patient_id=event["patient_id"],
            payload=str(event)
        )
        db.add(billing_event)

        invoice = Invoice(
            appointment_id=event["appointment_id"],
            patient_id=event["patient_id"],
            amount=event.get("amount", 1000.0)  # simple fixed logic
        )
        db.add(invoice)
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error storing event:", e)
    finally:
        db.close()
