from fastapi import APIRouter
from services.attendance_service import get_dashboard_stats

router = APIRouter()

@router.get("/")
def get_dashboard():
    """Returns key statistics for the dashboard."""
    stats = get_dashboard_stats()
    return {"status": "success", "data": stats}
