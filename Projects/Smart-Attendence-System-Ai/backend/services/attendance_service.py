import pandas as pd
from datetime import datetime
import os
from config import ATTENDANCE_FILE

def get_all_attendance():
    """Reads all attendance records from CSV."""
    if not os.path.exists(ATTENDANCE_FILE):
        return []
    try:
        df = pd.read_csv(ATTENDANCE_FILE)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Error reading attendance: {e}")
        return []

def get_today_attendance():
    """Returns only today's attendance records."""
    all_records = get_all_attendance()
    today_str = datetime.now().strftime("%Y-%m-%d")
    return [record for record in all_records if record.get("Date") == today_str]

def get_student_attendance(student_name: str):
    """Returns records for a specific student."""
    all_records = get_all_attendance()
    return [record for record in all_records if record.get("Name") == student_name]

def check_duplicate_attendance(student_name: str, date_str: str) -> bool:
    """Checks if a student already has attendance for a specific date."""
    records = get_student_attendance(student_name)
    for record in records:
        if record.get("Date") == date_str and record.get("Status") == "Present":
            return True
    return False

def mark_attendance(student_name: str) -> dict:
    """Marks attendance for a student. Returns status dictionary."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    # Check for duplicate
    if check_duplicate_attendance(student_name, date_str):
        return {
            "status": "duplicate",
            "message": f"{student_name} is already marked present today."
        }

    # Prepare new record
    new_record = pd.DataFrame([{
        "Name": student_name,
        "Date": date_str,
        "Time": time_str,
        "Status": "Present"
    }])

    # Write to CSV
    try:
        if not os.path.exists(ATTENDANCE_FILE):
            # Create with header if it doesn't exist
            new_record.to_csv(ATTENDANCE_FILE, index=False)
        else:
            # Append if it exists
            new_record.to_csv(ATTENDANCE_FILE, mode='a', header=False, index=False)
        
        return {
            "status": "success",
            "message": f"Attendance marked for {student_name}."
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Could not save attendance: {str(e)}"
        }

def get_dashboard_stats():
    """Calculates statistics for the dashboard."""
    all_records = get_all_attendance()
    today_records = get_today_attendance()
    
    unique_students = set(r.get("Name") for r in all_records)
    total_registered = len(unique_students)
    # If we have a list of all registered students from model, we could use that.
    # For now, we base it on history.
    if total_registered == 0: total_registered = 1 # avoid div by zero if empty

    return {
        "total_attendance_records": len(all_records),
        "present_today": len(today_records),
        "registered_students_estimate": total_registered,
        "today_percentage": round((len(today_records) / total_registered) * 100, 1)
    }
