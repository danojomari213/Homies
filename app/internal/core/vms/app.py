from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
template = Jinja2Templates('templates')
# from templates import template
# from routes import authRoutes, blacklistRoutes, inpatientRoutes, mailerRoutes, stationRoutes, healthFormRoutes, receptionistRoutes, passRoutes, appointmentRoutes, smsRoutes, userRoutes, visitRoutes, visitorRoutes

VMS = FastAPI()
PMS = FastAPI()
#? Mount static folder
# VMS.mount('/static', StaticFiles(directory='static'), name='static')
# VMS.mount('/storage', StaticFiles(directory='storage'), name='storage')

#? Register Routes
# VMS.include_router(authRoutes.router)
# VMS.include_router(receptionistRoutes.router)
# VMS.include_router(visitorRoutes.router)
# VMS.include_router(appointmentRoutes.router)
# VMS.include_router(passRoutes.router)
# VMS.include_router(stationRoutes.router)
# VMS.include_router(visitRoutes.router)
# VMS.include_router(userRoutes.router)
# VMS.include_router(healthFormRoutes.router)
# VMS.include_router(blacklistRoutes.router)
# VMS.include_router(mailerRoutes.router)
# VMS.include_router(smsRoutes.router)
# VMS.include_router(inpatientRoutes.router)

#Patient Management System
# Register Routes
# PMS.include_router(adminauthRoutes.router)
# PMS.include_router(register_userRoutes.router)
# PMS.include_router(doctorauthRoutes.router)
# PMS.include_router(inpatientRoutes.router)
# PMS.include_router(outpatientRoutes.router)
# PMS.include_router(dischargeRoutes.router)
# PMS.include_router(roomRoutes.router)
# PMS.include_router(prevhosdocRoutes.router)
# PMS.include_router(medicine_preRoutes.router)
# PMS.include_router(prescriptionRoutes.router)
# PMS.include_router(medical_suppliesRoutes.router)
# PMS.include_router(userintegRoutes.router)
# PMS.include_router(recordRoutes.router)


# TODO: CREATE HANDLERS
@VMS.exception_handler(StarletteException)
def http_exception_handler(request, exc):
    if exc.status_code == 401:
        return RedirectResponse('/')
    else:
        return PlainTextResponse(content=str(exc.detail),status_code=exc.status_code)


@VMS.get('/visiting_schedule')
def visiting_schedule(request: Request):
    return 'visiting schedule'
#     return template.TemplateResponse('/contents/public/visiting_schedule.html',{
#     'request': request,
#     'page': 'visiting_schedule',
#     'title': 'Visiting Schedule'
# })

@VMS.get('/visiting_procedures')
def visiting_procedures(request: Request):
    return 'visiting procedures'
#     return template.TemplateResponse('/contents/public/visiting_procedures.html',{
#     'request': request,
#     'page': 'visiting_procedures',
#     'title': 'Visiting Procedures'
# })

@VMS.get('/visiting_policies_requirements')
def visiting_policies_requirements(request: Request):
    return 'visiting policies'
#     return template.TemplateResponse('/contents/public/visiting_policies_requirements.html',{
#     'request': request,
#     'page': 'visiting_policies_requirements',
#     'title': 'Visiting Policies and Requirements'
# })

@VMS.get('/visitor')
def index(request: Request):
    return "fake visitor login page"

# Patient Management System

@PMS.get('/home', response_class=HTMLResponse)
def login(request: Request):
    return template.TemplateResponse('home.html', {
        'request': request,
    })

@PMS.get('/login', response_class=HTMLResponse)
def login(request: Request):
    return template.TemplateResponse('login/plugins_scripts.html', {
        'request': request,
    })

# Patient Management Admin User
@PMS.get('/admin/home', response_class=HTMLResponse)
def dashboard(request: Request):
    return template.TemplateResponse('admin/homeindex.html', {
        'request': request,
        'home' : 'active'
    })

@PMS.get('/admin/dashboard', response_class=HTMLResponse)
def dashboard(request: Request):
    return template.TemplateResponse('admin/index.html', {
        'request': request,
        'dashboard': 'admin/dashboard',
        'patienysys': 'active'
    })

@PMS.get('/admin/patient', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('admin/pages/patient.html', {
        'request': request,
        'patient': 'admin/patient',
        'patienysys': 'active'
    })

@PMS.get('/admin/prescription', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('admin/pages/patient_reg.html', {
        'request': request,
        'prescription': 'admin/prescription',
        'patienysys': 'active'
    })

@PMS.get('/admin/inpatient', response_class=HTMLResponse)
def inpatient(request: Request):
    return template.TemplateResponse('admin/pages/inpatient.html', {
        'request': request,
        'inpatient': 'admin/inpatient',
        'patienysys': 'active'
    })

@PMS.get('/admin/outpatient', response_class=HTMLResponse)
def outpatient(request: Request):
    return template.TemplateResponse('admin/pages/outpatient.html', {
        'request': request,
        'outpatient': 'admin/outpatient',
        'patienysys': 'active'
    })

@PMS.get('/admin/discharge', response_class=HTMLResponse)
def discharge(request: Request):
    return template.TemplateResponse('admin/pages/discharge.html', {
        'request': request,
        'discharge': 'admin/discharge',
        'patienysys': 'active'
    })

@PMS.get('/admin/room', response_class=HTMLResponse)
def room(request: Request):
    return template.TemplateResponse('admin/pages/room.html', {
        'request': request,
        'room': 'admin/room',
        'patienysys': 'active'
    })

@PMS.get('/admin/staff/doctor', response_class=HTMLResponse)
def doctor(request: Request):
    return template.TemplateResponse('admin/pages/doctor.html', {
        'request': request,
        'active': 'active',
        'doctor': 'admin/staff/doctor',
        'patienysys': 'active'
    })

@PMS.get('/admin/staff/publicuser', response_class=HTMLResponse)
def publicuser(request: Request):
    return template.TemplateResponse('admin/pages/publicuser.html', {
        'request': request,
        'active': 'active',
        'doctor': 'admin/staff/publicuser',
        'patienysys': 'active'
    })

@PMS.get('/admin/staff/internaluser', response_class=HTMLResponse)
def nurse(request: Request):
    return template.TemplateResponse('admin/pages/internaluser.html', {
        'request': request,
        'active': 'active',
        'doctor': 'admin/staff/internaluser',
        'patienysys': 'active'
    })

@PMS.get('/admin/staff/patientregistrar', response_class=HTMLResponse)
def patientregistrar(request: Request):
    return template.TemplateResponse('admin/pages/patient_registrar.html', {
        'request': request,
        'active': 'active',
        'doctor': 'admin/staff/patientregistrar',
        'patienysys': 'active'
    })

@PMS.get('/admin/user_settings', response_class=HTMLResponse)
def patientregistrar(request: Request):
    return template.TemplateResponse('admin/pages/user_settings.html', {
        'request': request,
    })


@PMS.get('/admin/sysadmin', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('admin/pages/sysadmin.html', {
        'request': request,
        'dashboard': 'admin/dashboard',
        'sysadmin': 'active'
    })

# Patient Management System Patient Registrar

@PMS.get('/patient_registrar/dashboard', response_class=HTMLResponse)
def dashboard(request: Request):
    return template.TemplateResponse('patient_registrar/index.html', {
        'request': request,
        'dashboard': 'patient_registrar/dashboard',
        'patienysys': 'active'
    })

@PMS.get('/patient_registrar/patient', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('patient_registrar/pages/patient.html', {
        'request': request,
        'patient': 'patient_registrar/patient',
        'patienysys': 'active'
    })

@PMS.get('/patient_registrar/inpatient', response_class=HTMLResponse)
def inpatient(request: Request):
    return template.TemplateResponse('patient_registrar/pages/inpatient.html', {
        'request': request,
        'inpatient': 'patient_registrar/inpatient',
        'patienysys': 'active'
    })

@PMS.get('/patient_registrar/outpatient', response_class=HTMLResponse)
def outpatient(request: Request):
    return template.TemplateResponse('patient_registrar/pages/outpatient.html', {
        'request': request,
        'outpatient': 'patient_registrar/outpatient',
        'patienysys': 'active'
    })

@PMS.get('/patient_registrar/discharge', response_class=HTMLResponse)
def discharge(request: Request):
    return template.TemplateResponse('patient_registrar/pages/discharge.html', {
        'request': request,
        'discharge': 'patient_registrar/discharge',
        'patienysys': 'active'
    })

@PMS.get('/patient_registrar/room', response_class=HTMLResponse)
def room(request: Request):
    return template.TemplateResponse('patient_registrar/pages/room.html', {
        'request': request,
        'room': 'patient_registrar/room',
        'patienysys': 'active'
    })

@PMS.get('/patient_registrar/user_settings', response_class=HTMLResponse)
def patientregistrar(request: Request):
    return template.TemplateResponse('patient_registrar/pages/user_settings.html', {
        'request': request,
    })

@PMS.get('/patient_registrar/user_settings', response_class=HTMLResponse)
def patientregistrar(request: Request):
    return template.TemplateResponse('patient_registrar/pages/user_settings.html', {
        'request': request,
    })

@PMS.get('/patient_registrar/prescription', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('patient_registrar/pages/prescription.html', {
        'request': request,
        'prescription': 'patient_registrar/prescription',
        'patienysys': 'active'
    })


# Patient Management System Management User

@PMS.get('/management/dashboard', response_class=HTMLResponse)
def dashboard(request: Request):
    return template.TemplateResponse('management/index.html', {
        'request': request,
        'dashboard': 'management/dashboard',
        'patienysys': 'active'
    })

@PMS.get('/management/patient', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('management/pages/patient.html', {
        'request': request,
        'patient': 'management/patient',
        'patienysys': 'active'
    })

@PMS.get('/management/inpatient', response_class=HTMLResponse)
def inpatient(request: Request):
    return template.TemplateResponse('management/pages/inpatient.html', {
        'request': request,
        'inpatient': 'management/inpatient',
        'patienysys': 'active'
    })

@PMS.get('/management/outpatient', response_class=HTMLResponse)
def outpatient(request: Request):
    return template.TemplateResponse('management/pages/outpatient.html', {
        'request': request,
        'outpatient': 'management/outpatient',
        'patienysys': 'active'
    })

@PMS.get('/management/discharge', response_class=HTMLResponse)
def discharge(request: Request):
    return template.TemplateResponse('management/pages/discharge.html', {
        'request': request,
        'discharge': 'management/discharge',
        'patienysys': 'active'
    })

@PMS.get('/management/user_settings', response_class=HTMLResponse)
def patientregistrar(request: Request):
    return template.TemplateResponse('management/pages/user_settings.html', {
        'request': request,
    })


# Patient Management System Doctor User


@PMS.get('/doctors/dashboard', response_class=HTMLResponse)
def dashboard(request: Request):
    return template.TemplateResponse('doctors/index.html', {
        'request': request,
        'dashboard': 'doctors/dashboard',
        'patienysys': 'active'
    })

@PMS.get('/doctors/patient', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('doctors/pages/patient.html', {
        'request': request,
        'patient': 'doctors/patient',
        'patienysys': 'active'
    })

@PMS.get('/doctors/inpatient', response_class=HTMLResponse)
def inpatient(request: Request):
    return template.TemplateResponse('doctors/pages/inpatient.html', {
        'request': request,
        'inpatient': 'doctors/inpatient',
        'patienysys': 'active'
    })

@PMS.get('/doctors/outpatient', response_class=HTMLResponse)
def outpatient(request: Request):
    return template.TemplateResponse('doctors/pages/outpatient.html', {
        'request': request,
        'outpatient': 'doctors/outpatient',
        'patienysys': 'active'
    })

@PMS.get('/doctors/discharge', response_class=HTMLResponse)
def discharge(request: Request):
    return template.TemplateResponse('doctors/pages/discharge.html', {
        'request': request,
        'discharge': 'doctors/discharge',
        'patienysys': 'active'
    })

@PMS.get('/doctors/room', response_class=HTMLResponse)
def room(request: Request):
    return template.TemplateResponse('doctors/pages/room.html', {
        'request': request,
        'room': 'doctors/room'
    })

@PMS.get('/doctors/user_settings', response_class=HTMLResponse)
def patientregistrar(request: Request):
    return template.TemplateResponse('doctors/pages/user_settings.html', {
        'request': request,
    })

@PMS.get('/doctors/prescription', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('doctors/pages/prescription.html', {
        'request': request,
        'prescription': 'doctors/prescription',
        'patienysys': 'active'
    })


# Patient Management System Nurse User

@PMS.get('/nurses/dashboard', response_class=HTMLResponse)
def dashboard(request: Request):
    return template.TemplateResponse('nurses/index.html', {
        'request': request,
        'dashboard': 'nurses/dashboard'
    })

@PMS.get('/nurses/patient', response_class=HTMLResponse)
def patient(request: Request):
    return template.TemplateResponse('nurses/pages/patient.html', {
        'request': request,
        'patient': 'nurses/patient'
    })

@PMS.get('/nurses/inpatient', response_class=HTMLResponse)
def inpatient(request: Request):
    return template.TemplateResponse('nurses/pages/inpatient.html', {
        'request': request,
        'inpatient': 'nurses/inpatient'
    })

@PMS.get('/nurses/outpatient', response_class=HTMLResponse)
def outpatient(request: Request):
    return template.TemplateResponse('nurses/pages/outpatient.html', {
        'request': request,
        'outpatient': 'nurses/outpatient'
    })

@PMS.get('/nurses/discharge', response_class=HTMLResponse)
def discharge(request: Request):
    return template.TemplateResponse('nurses/pages/discharge.html', {
        'request': request,
        'discharge': 'nurses/discharge'
    })

@PMS.get('/nurses/room', response_class=HTMLResponse)
def room(request: Request):
    return template.TemplateResponse('nurses/pages/room.html', {
        'request': request,
        'room': 'nurses/room'
    })

@PMS.get('/nurses/user_settings', response_class=HTMLResponse)
def patientregistrar(request: Request):
    return template.TemplateResponse('nurses/pages/user_settings.html', {
        'request': request,
    })




