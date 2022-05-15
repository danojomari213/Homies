# Import Packages
from typing import Optional
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from database import get_db
from fastapi.templating import Jinja2Templates

# Import Models
from models import *


# Import Submodule files
from app.internal.human_resource.rms.routers.web \
    import errPages_templates as errTemplate


# Template
template = Jinja2Templates(directory = "app/internal/human_resource/rms/views")


# Router
router = APIRouter()


# ===========================================================
# CAREERS/JOB POSTS
# ===========================================================


# Careers
@router.get("/careers")
def careers(
    req: Request, 
    page: Optional[int] = 1
):

    # Check if page is not valid
    if not page or page <= 0:
        return errTemplate.page_not_found(req)

    # If query is not declared
    return template.TemplateResponse("pages/home/careers.html", {
        "request": req,
        "page_title": "Careers",
        "page_subtitle": "Discover job opportunities here",
        "active_navlink": "Careers"
    })


# Available Job Details
@router.get("/careers/{job_post_id}")
def job_details(job_post_id: str, req: Request, db: Session = Depends(get_db)):
    
    # Check if job_post_id is existing in database
    if not db.query(JobPost).filter(JobPost.job_post_id == job_post_id).first():
        return errTemplate.page_not_found(req)
    
    # If no error, return template response
    return template.TemplateResponse("pages/home/job_details.min.html", {
        "request": req,
        "page_title": "Job Details",
        "active_navlink": "Careers"
    })
