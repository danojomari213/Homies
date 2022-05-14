# Import Packages
from database import Base
from sqlalchemy import text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime, Float, Text, Boolean, Date, Time
from sqlalchemy.orm import relationship


# * PUBLIC USER
class PublicUser(Base):
    __tablename__ = 'public_users'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))
    is_blacklist = Column(Boolean, default=text('0'))

    profile = relationship('PublicProfile', back_populates='public_user', uselist=False)


class PublicProfile(Base):
    __tablename__ = 'public_profiles'

    id = Column(String(36), primary_key=True, nullable=False, default=text('UUID()'))
    user_id = Column(String(36), ForeignKey('public_users.id'), nullable=True)
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=False)
    suffix_name = Column(String(255), nullable=True)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(255), nullable=False)
    house_street = Column(String(255), nullable=False)
    barangay = Column(String(255), nullable=False)
    municipality = Column(String(255), nullable=False)
    province = Column(String(255), nullable=False)
    region = Column(String(255), nullable=False)
    contact_number = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    full_address = Column(String(255), nullable=False)

    public_user = relationship('PublicUser', back_populates='profile')


# * INTERNAL USER
class InternalUser(Base):
    __tablename__ = 'internal_users'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    employee_id = Column(
        String(36),
        ForeignKey('employees.employee_id'),
        nullable = False
    )
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    roles = relationship('UserRole', back_populates='user')
    employee_info = relationship('Employee', back_populates = 'user_credentials')


class Role(Base):
    __tablename__ = 'roles'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    subsystem = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    redirect_url = Column(String(255), nullable=False)

    users = relationship('UserRole', back_populates='role')


class UserRole(Base):
    __tablename__ = 'user_roles'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    user_id = Column(String(36), ForeignKey('internal_users.id'), default=text('UUID()'))
    role_id = Column(String(36), ForeignKey('roles.id'), default=text('UUID()'))

    user = relationship('InternalUser', back_populates='roles')
    role = relationship('Role', back_populates='users')


#** INTERNAL USER PROFILE? di ko alam kung pano ginawa nyo dito, external ako
#? Employees na yung magsisilbing User Profile for Internal Users


# ! CORE HOSPITAL

# ???


# ! HUMAN RESOURCE

# ? RECRUITMENT MANAGEMENT

# Applicant Model
class Applicant(Base):
    __tablename__ = "applicants"

    # ==================================================================================
    # Columns
    # ==================================================================================

    applicant_id = Column(
        String(36), 
        primary_key = True, 
        default = text('UUID()')
    )
    job_post_id = Column(
        String(36), 
        ForeignKey("job_posts.job_post_id"), 
        nullable = False
    )
    first_name = Column(
        String(255), 
        nullable = False
    )
    middle_name = Column(
        String(255), 
        nullable = True
    )
    last_name = Column(
        String(255), 
        nullable = False
    )
    suffix_name = Column(
        String(255), 
        nullable = True
    )
    resume = Column(
        String(255), 
        nullable = False,unique = True
    )
    contact_number = Column(
        String(255), 
        nullable = False
    )
    email = Column(
        String(255), 
        nullable = False
    )
    status = Column(
        String(255), 
        nullable = False,
        default = "For evaluation"
    )
    evaluated_by = Column(
        String(36), 
        ForeignKey("employees.employee_id"), 
        nullable = True
    )
    evaluated_at = Column(
        DateTime, 
        nullable = True
    )
    screened_by = Column(
        String(36), 
        ForeignKey("employees.employee_id"), 
        nullable = True
    )
    screened_at = Column(
        DateTime, 
        nullable = True
    )
    hired_by = Column(
        String(36), 
        ForeignKey("employees.employee_id"), 
        nullable = True
    )
    hired_at = Column(
        String(36), 
        nullable = True
    )
    rejected_by = Column(
        String(36), 
        ForeignKey("employees.employee_id"), 
        nullable = True
    )
    rejected_at = Column(
        DateTime, 
        nullable = True
    )
    remarks = Column(
        Text, 
        nullable = True
    )
    created_at = Column(
        DateTime, 
        default = text('NOW()'), 
        nullable = False
    )
    updated_at = Column(
        DateTime, 
        default = text('NOW()'), 
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationships (From other tables/models)
    # ==================================================================================

    # From JobPost
    applied_job = relationship("JobPost", back_populates = "applicants")
    
    # From Employee
    applicant_evaluated_by = relationship(
        "Employee",
        back_populates = "evaluated_applicants",
        foreign_keys = "Applicant.evaluated_by"
    )
    applicant_screened_by = relationship(
        "Employee",
        back_populates = "screened_applicants",
        foreign_keys = "Applicant.screened_by"
    )
    applicant_hired_by = relationship(
        "Employee",
        back_populates = "hired_applicants",
        foreign_keys = "Applicant.hired_by"
    )
    applicant_rejected_by = relationship(
        "Employee",
        back_populates = "rejected_applicants",
        foreign_keys = "Applicant.rejected_by"
    )

    # ==================================================================================
    # Relationships (To other tables/models)
    # ==================================================================================

    # To Interviewee
    interviewee_info = relationship(
        "Interviewee",
        back_populates = "applicant_info",
        uselist = False
    )


# Department Model
# Hiram namin sa core human capital
class Department(Base):
    __tablename__ = "departments"

    # ==================================================================================
    # Columns
    # ==================================================================================

    department_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    name = Column(
        String(255),
        nullable = False
    )
    description = Column(
        String(255),
        nullable = False
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationships (To other tables)
    # ==================================================================================

    # To SubDepartment
    sub_departments = relationship(
        "SubDepartment",
        back_populates = "main_department"
    )


# Employee Model
# Hiram namin sa core human capital
class Employee(Base):
    __tablename__ = "employees"

    # ==================================================================================
    # Columns
    # ==================================================================================

    employee_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    first_name = Column(
        String(255),
        nullable = False
    )
    middle_name = Column(
        String(255),
        nullable =  True
    )
    last_name = Column(
        String(255),
        nullable = False
    )
    extension_name = Column(
        String(255),
        nullable = True
    )
    contact_number = Column(
        String(255),
        nullable = False
    )
    position_id = Column(
        String(36),
        ForeignKey("positions.position_id"),
        nullable = False
    )
    employment_type_id = Column(
        String(255),
        ForeignKey("employment_types.employment_type_id"),
        nullable = False
    )
    status = Column(
        String(255),
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )


    # ==================================================================================
    # Relationships (From other tables)
    # ==================================================================================
    
    # From Position
    position = relationship(
        "Position",
        back_populates = "employees"
    )

    # From EmploymentType
    employment_type = relationship(
        "EmploymentType",
        back_populates = "employees"
    )


    # ==================================================================================
    # Relationships (To other tables)
    # ==================================================================================
    
    # To User
    user_credentials = relationship(
        "InternalUser",
        back_populates = "employee_info"
    )
    
    # To ManpowerRequst
    requested_manpower_requests = relationship(
        "ManpowerRequest", 
        back_populates = "manpower_request_requested_by",
        foreign_keys = "ManpowerRequest.requested_by"
    )
    signed_manpower_requests = relationship(
        "ManpowerRequest",
        back_populates = "manpower_request_signed_by",
        foreign_keys = "ManpowerRequest.signed_by"
    )
    reviewed_manpower_requests = relationship(
        "ManpowerRequest",
        back_populates = "manpower_request_reviewed_by",
        foreign_keys = "ManpowerRequest.reviewed_by"
    )
    rejected_manpower_requests = relationship(
        "ManpowerRequest",
        back_populates = "manpower_request_rejected_by",
        foreign_keys = "ManpowerRequest.rejected_by"
    )

    # To JobPost
    created_job_posts = relationship(
        "JobPost",
        back_populates = "job_post_posted_by"
    )

    # To JobCategory
    created_job_categories = relationship(
        "JobCategory",
        back_populates = "job_category_created_by"
    )

    # To Applicant
    evaluated_applicants = relationship(
        "Applicant",
        back_populates = "applicant_evaluated_by",
        foreign_keys = "Applicant.evaluated_by"
    )
    screened_applicants = relationship(
        "Applicant",
        back_populates = "applicant_screened_by",
        foreign_keys = "Applicant.screened_by"
    )
    hired_applicants = relationship(
        "Applicant",
        back_populates = "applicant_hired_by",
        foreign_keys = "Applicant.hired_by"
    )
    rejected_applicants = relationship(
        "Applicant",
        back_populates = "applicant_rejected_by",
        foreign_keys = "Applicant.rejected_by"
    )

    # To InterviewSchedule
    set_interview_schedules = relationship(
        "InterviewSchedule",
        back_populates = "interview_schedule_set_by" 
    )

    # To Interview Score
    set_interview_scores = relationship(
        "InterviewScore",
        back_populates = "interview_scored_by"
    )

    # To InterviewQuestion
    added_interview_questions = relationship(
        "InterviewQuestion",
        back_populates = "interview_question_added_by",
        foreign_keys = "InterviewQuestion.added_by"
    )
    updated_interview_questions = relationship(
        "InterviewQuestion",
        back_populates = "interview_question_updated_by",
        foreign_keys = "InterviewQuestion.updated_by"
    )

    # To OnboardingEmployee
    signed_onboarding_employees = relationship(
        "OnboardingEmployee",
        back_populates = "onboarding_employee_signed_by",
        foreign_keys = "OnboardingEmployee.signed_by"
    )
    updated_onboarding_employees = relationship(
        "OnboardingEmployee",
        back_populates = "onboarding_employee_updated_by",
        foreign_keys = "OnboardingEmployee.updated_by"
    )

    # To OnboardingTask
    added_onboarding_tasks = relationship(
        "OnboardingTask",
        back_populates = "onboarding_task_added_by",
        foreign_keys = "OnboardingTask.added_by"
    )
    updated_onboarding_tasks = relationship(
        "OnboardingTask",
        back_populates = "onboarding_task_updated_by",
        foreign_keys = "OnboardingTask.updated_by"
    )

    # To OnboardingEmployeeTask
    assigned_onboarding_employee_tasks = relationship(
        "OnboardingEmployeeTask",
        back_populates = "onboarding_employee_task_assigned_by",
        foreign_keys = "OnboardingEmployeeTask.assigned_by"
    )
    completed_onboarding_employee_tasks = relationship(
        "OnboardingEmployeeTask",
        back_populates = "onboarding_employee_task_completed_by",
        foreign_keys = "OnboardingEmployeeTask.completed_by"
    )


# Employment Type Model
# Hiram namin sa core human capital
class EmploymentType(Base):
    __tablename__ = "employment_types"

    # ==================================================================================
    # Column
    # ==================================================================================

    employment_type_id = Column(
        String(36),
        primary_key=True,
        default=text('UUID()')
    )
    name = Column(
        String(255),
        nullable = False
    )
    description = Column(
        Text,
        nullable = False,
    )
    is_active = Column(
        Boolean,
        default = True,
        nullable = False
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationship (To other tables/models)
    # ==================================================================================

    # To ManpoweRequest
    manpower_requests = relationship(
        "ManpowerRequest",
        back_populates = "employment_type"
    )

    # To Employee
    employees = relationship(
        "Employee",
        back_populates = "employment_type"
    )


# Interviewee Model
class Interviewee(Base):
    __tablename__ = "interviewees"

    # ==================================================================================
    # Columns
    # ==================================================================================

    interviewee_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    applicant_id = Column(
        String(36),
        ForeignKey("applicants.applicant_id"),
        nullable = False
    )
    interview_schedule_id = Column(
        String(36),
        ForeignKey("interview_schedules.interview_schedule_id"),
        nullable = True
    )
    is_interviewed = Column(
        Boolean,
        nullable = True
    )
    interviewed_at = Column(
        DateTime,
        nullable = True
    )
    remarks = Column(
        Text,
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationships (From other tables/models)
    # ==================================================================================

    # From Applicant
    applicant_info = relationship(
        "Applicant",
        back_populates = "interviewee_info",
        uselist = False
    )

    # From InterviewSchedule
    interview_schedule = relationship(
        "InterviewSchedule",
        back_populates = "interviewees"
    )
    
    # ==================================================================================
    # Relationships (To other tables/models)
    # ==================================================================================

    # To InterviewScore
    interview_scores = relationship(
        "InterviewScore",
        back_populates = "score_for"
    )


# Interview Question Model
class InterviewQuestion(Base):
    __tablename__ = "interview_questions"

    # ==================================================================================
    # Columns
    # ==================================================================================

    interview_question_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    question = Column(
        String(255),
        nullable = False
    )
    type = Column(
        String(255),
        nullable = False
    )
    added_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = False
    )
    updated_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationships (From other tables/columns)
    # ==================================================================================

    # From Employee
    interview_question_added_by = relationship(
        "Employee",
        back_populates = "added_interview_questions",
        foreign_keys = "InterviewQuestion.added_by"
    )
    interview_question_updated_by = relationship(
        "Employee",
        back_populates = "updated_interview_questions",
        foreign_keys = "InterviewQuestion.updated_by"
    )

    # ==================================================================================
    # Relationships (To other tables/columns)
    # ==================================================================================
    
    # To InterviewScore
    interview_scores = relationship(
        "InterviewScore",
        back_populates = "interview_question"
    )


# Inteview Schedule Model
class InterviewSchedule(Base):
    __tablename__ = "interview_schedules"

    # ==================================================================================
    # Columns
    # ==================================================================================

    interview_schedule_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    job_post_id = Column(
        String(36),
        ForeignKey("job_posts.job_post_id"),
        nullable = False
    )
    scheduled_date = Column(
        Date,
        nullable = False
    )
    start_session = Column(
        Time,
        nullable = False
    )
    end_session = Column(
        Time,
        nullable = False
    )
    set_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationships (From other tables/columns)
    # ==================================================================================

    # From JobPost
    schedule_for = relationship(
        "JobPost",
        back_populates = "interview_schedules"
    )

    # From Employee
    interview_schedule_set_by = relationship(
        "Employee",
        back_populates = "set_interview_schedules"
    )

    # ==================================================================================
    # Relationships (To other tables/columns)
    # ==================================================================================

    # To Interviewees
    interviewees = relationship(
        "Interviewee",
        back_populates = "interview_schedule"
    )


# Interview Score Model
class InterviewScore(Base):
    __tablename__ = "interview_scores"

    # ==================================================================================
    # Columns
    # ==================================================================================

    interview_score_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    interviewee_id = Column(
        String(36),
        ForeignKey("interviewees.interviewee_id"),
        nullable = False
    )
    interview_question_id = Column(
        String(36),
        ForeignKey("interview_questions.interview_question_id")
    )
    score = Column(
        Float,
        nullable = True
    )
    scored_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationships (From other tables/columns)
    # ==================================================================================

    # From InterviewQuestion
    interview_question = relationship(
        "InterviewQuestion",
        back_populates = "interview_scores"
    )

    # From Employee
    interview_scored_by = relationship(
        "Employee",
        back_populates = "set_interview_scores"
    )

    # From Interviewee
    score_for = relationship(
        "Interviewee",
        back_populates = "interview_scores"
    )


# Job Category Model
class JobCategory(Base):
    __tablename__ = "job_categories"

    # ==================================================================================
    # Columns
    # ==================================================================================

    job_category_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    name = Column(
        String(36),
        nullable = False
    )
    description = Column(
        Text,
        nullable = False
    )
    is_removed = Column(
        Boolean,
        nullable = False,
        default = False
    )
    created_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = False
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationships (From other tables/models)
    # ==================================================================================

    # From Employee
    job_category_created_by = relationship(
        "Employee",
        back_populates = "created_job_categories",
    )

    # ==================================================================================
    # Relationships (To other tables/models)
    # ==================================================================================

    job_posts = relationship(
        "JobPost",
        back_populates = "job_category"
    )


# Job Post Model
class JobPost(Base):
    __tablename__ = "job_posts"

    # ==================================================================================
    # Columns
    # ==================================================================================

    job_post_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    manpower_request_id = Column(
        String(36),
        ForeignKey("manpower_requests.manpower_request_id"),
        nullable = False
    )
    is_salary_visible = Column(
        Boolean,
        nullable = False,
        default = False
    )
    content = Column(
        Text,
        nullable = False
    )
    expiration_date = Column(
        DateTime,
        nullable = True
    )
    job_category_id = Column(
        String(36),
        ForeignKey("job_categories.job_category_id"),
        nullable = False
    )
    posted_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = False
    )
    views = Column(
        Integer,
        nullable = False,
        default = 0
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationship (From other tables/models)
    # ==================================================================================

    # From ManpowerRequest
    manpower_request = relationship(
        "ManpowerRequest",
        back_populates = "job_post"
    )

    # From Employee
    job_post_posted_by = relationship(
        "Employee",
        back_populates = "created_job_posts"
    )

    # From JobCategory
    job_category = relationship(
        "JobCategory",
        back_populates = "job_posts",
    )

    # ==================================================================================
    # Relationship (To other tables/models)
    # ==================================================================================

    # To Applicants
    applicants = relationship(
        "Applicant",
        back_populates = "applied_job"
    )

    # To Interview Schedule
    interview_schedules = relationship(
        "InterviewSchedule",
        back_populates = "schedule_for"
    )


# Manpower Request Model
class ManpowerRequest(Base):
    __tablename__ = "manpower_requests"

    # ==================================================================================
    # Columns
    # ==================================================================================

    manpower_request_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    requisition_no = Column(
        String(255),
        unique = True,
        nullable = False
    )
    requested_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = False
    )
    position_id = Column(
        String(36),
        ForeignKey("positions.position_id"),
        nullable = False
    )
    employment_type_id = Column(
        String(255),
        ForeignKey("employment_types.employment_type_id"),
        nullable = False
    )
    request_nature = Column(
        String(255),
        default = "For Review",
        nullable = False
    )
    staffs_needed = Column(
        Integer,
        nullable = False
    )
    min_monthly_salary = Column(
        Float,
        nullable = True
    )
    max_monthly_salary = Column(
        Float,
        nullable = True
    )
    content = Column(
        Text,
        nullable = False
    )
    request_status = Column(
        String(255),
        nullable = False
    )
    deadline = Column(
        DateTime,
        nullable = True
    )
    signed_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    signed_at = Column(
        DateTime,
        nullable = True
    )
    reviewed_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    reviewed_at = Column(
        DateTime,
        nullable = True
    )
    completed_at = Column(
        DateTime,
        nullable = True
    )
    rejected_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    rejected_at = Column(
        DateTime,
        nullable = True
    )
    remarks = Column(
        Text,
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationship (From other tables/models)
    # ==================================================================================

    # From Employee
    manpower_request_requested_by = relationship(
        "Employee",
        back_populates = "requested_manpower_requests",
        foreign_keys = "ManpowerRequest.requested_by"
    )
    manpower_request_reviewed_by = relationship(
        "Employee",
        back_populates = "reviewed_manpower_requests",
        foreign_keys = "ManpowerRequest.reviewed_by"
    )
    manpower_request_signed_by = relationship(
        "Employee",
        back_populates = "signed_manpower_requests",
        foreign_keys = "ManpowerRequest.signed_by"
    )
    manpower_request_rejected_by = relationship(
        "Employee",
        back_populates = "rejected_manpower_requests",
        foreign_keys = "ManpowerRequest.rejected_by"
    )

    # From Employment Type
    employment_type = relationship(
        "EmployeeType",
        back_populates="manpower_requests",
    )

    # From EmploymentType
    employment_type = relationship(
        "EmploymentType",
        back_populates = "manpower_requests"
    )

    # From Position
    vacant_position = relationship(
        "Position",
        back_populates = "manpower_requests"
    )

    # ==================================================================================
    # Relationship (To other tables/models)
    # ==================================================================================

    # To JobPost
    job_post = relationship(
        "JobPost",
        back_populates = "manpower_request",
        uselist = False
    )


# Onboarding Employee Model
class OnboardingEmployee(Base):
    __tablename__ = "onboarding_employees"

    # ==================================================================================
    # Columns
    # ==================================================================================

    onboarding_employee_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    first_name = Column(
        String(255),
        nullable = False
    )
    middle_name = Column(
        String(255),
        nullable = True
    )
    last_name = Column(
        String(255),
        nullable = False
    )
    suffix_name = Column(
        String(255),
        nullable = True
    )
    contact_number = Column(
        String(255),
        nullable = False
    )
    email = Column(
        String(255),
        nullable = False
    )
    position_id = Column(
        String(36),
        ForeignKey("positions.position_id"),
        nullable = False
    )
    employment_start_date = Column(
        Date,
        nullable = True
    )
    employment_contract = Column(
        String(255),
        unique = True,
        nullable = False
    )
    status = Column(
        String(255),
        nullable = False
    )
    signed_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = False
    )
    updated_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationship (From other tables/models)
    # ==================================================================================

    # From Position
    onboarding_employee_position = relationship(
        "Position",
        back_populates = "onboarding_employees"
    )

    # From Employee
    onboarding_employee_signed_by = relationship(
        "Employee",
        back_populates = "signed_onboarding_employees",
        foreign_keys = "OnboardingEmployee.signed_by"
    )
    onboarding_employee_updated_by = relationship(
        "Employee",
        back_populates = "updated_onboarding_employees",
        foreign_keys = "OnboardingEmployee.updated_by"
    )

    # ==================================================================================
    # Relationship (To other tables/models)
    # ==================================================================================

    # To OnboardingEmployeeTask
    onboarding_employee_tasks = relationship(
        "OnboardingEmployeeTask",
        back_populates = "onboarding_employee"
    )


# Onboarding Employye Task Model
class OnboardingEmployeeTask(Base):
    __tablename__ = "onboarding_employee_task"
    
    # ==================================================================================
    # Columns
    # ==================================================================================

    onboarding_employee_task_id = Column(
        String(36),
        primary_key = True,
        default = text("UUID()")
    )
    onboarding_employee_id = Column(
        String(36),
        ForeignKey("onboarding_employees.onboarding_employee_id"),
        nullable = False
    )
    onboarding_task_id = Column(
        String(36),
        ForeignKey("onboarding_tasks.onboarding_task_id"),
        nullable = False
    )
    start_at = Column(
        DateTime,
        nullable = False
    )
    end_at = Column(
        DateTime,
        nullable = False
    )
    assigned_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = False
    )
    status = Column(
        String(255),
        nullable = False
    )
    completed_at = Column(
        DateTime,
        nullable = True
    )
    completed_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationships (From other tables/models)
    # ==================================================================================

    # From OnboardingEmployee
    onboarding_employee = relationship(
        "OnboardingEmployee",
        back_populates = "onboarding_employee_tasks"
    )

    # From OnboardingTask
    onboarding_task = relationship(
        "OnboardingTask",
        back_populates = "assigned_tasks"
    )
    
    # From Employee
    onboarding_employee_task_assigned_by = relationship(
        "Employee",
        back_populates = "assigned_onboarding_employee_tasks",
        foreign_keys = "OnboardingEmployeeTask.assigned_by"
    )
    onboarding_employee_task_completed_by = relationship(
        "Employee",
        back_populates = "completed_onboarding_employee_tasks",
        foreign_keys = "OnboardingEmployeeTask.completed_by"
    )


# Onboarding Tasks Model
class OnboardingTask(Base):
    __tablename__ = "onboarding_tasks"

    # ==================================================================================
    # Columns
    # ==================================================================================

    onboarding_task_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    title = Column(
        String(255),
        nullable = False
    )
    description = Column(
        Text,
        nullable = False
    )
    task_type = Column(
        String(255),
        nullable = False
    )
    is_general = Column(
        Boolean,
        nullable = False,
        default = False
    )
    sub_department_id = Column(
        String(36),
        ForeignKey("sub_departments.sub_department_id"),
        nullable = False
    )
    added_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = False
    )
    updated_by = Column(
        String(36),
        ForeignKey("employees.employee_id"),
        nullable = True
    )
    is_deleted = Column(
        Boolean,
        nullable = False,
        default = False
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationship (From other tables/column)
    # ==================================================================================

    # From SubDepartment
    for_sub_department = relationship(
        "SubDepartment",
        back_populates = "onboarding_tasks"
    )

    # Employee
    onboarding_task_added_by = relationship(
        "Employee",
        back_populates = "added_onboarding_tasks",
        foreign_keys = "OnboardingTask.added_by"
    )
    onboarding_task_updated_by = relationship(
        "Employee",
        back_populates = "updated_onboarding_tasks",
        foreign_keys = "OnboardingTask.updated_by"
    )

    # ==================================================================================
    # Relationship (To other tables/column)
    # ==================================================================================

    # To OnboardingEmployeeTask
    assigned_tasks = relationship(
        "OnboardingEmployeeTask",
        back_populates = "onboarding_task"
    )


# Position Model
# Hiram namin sa core human capital
class Position(Base):
    __tablename__ = "positions"

    # ==================================================================================
    # Columns
    # ==================================================================================

    position_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()'),
    )
    sub_department_id = Column(
        String(36),
        ForeignKey("sub_departments.sub_department_id"),
        nullable = False
    )
    name = Column(
        String(255),
        nullable = False
    )
    description = Column(
        String(255),
        nullable = False
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationship (From other tables/models)
    # ==================================================================================

    # From SubDepartment
    sub_department = relationship(
        "SubDepartment",
        back_populates = "positions"
    )

    # ==================================================================================
    # Relationship (To other tables/models)
    # ==================================================================================

    # To Employee
    employees = relationship(
        "Employee",
        back_populates = "position"
    )

    # To ManpowerRequest
    manpower_requests = relationship(
        "ManpowerRequest",
        back_populates = "vacant_position"
    )

    # To OnboardingEmployee
    onboarding_employees = relationship(
        "OnboardingEmployee",
        back_populates = "onboarding_employee_position"
    )


# Sub Department Model
# Hiram namin sa core human capital
class SubDepartment(Base):
    __tablename__ = "sub_departments"

    # ==================================================================================
    # Columns
    # ==================================================================================

    sub_department_id = Column(
        String(36),
        primary_key = True,
        default = text('UUID()')
    )
    department_id = Column(
        String(36),
        ForeignKey("departments.department_id"),
        nullable = False
    )
    name = Column(
        String(255),
        nullable = False
    )
    description = Column(
        Text,
        nullable = False
    )
    location = Column(
        String(255),
        nullable = False
    )
    created_at = Column(
        DateTime,
        default = text('NOW()'),
        nullable = False
    )
    updated_at = Column(
        DateTime,
        default = text('NOW()'),
        onupdate = text('NOW()')
    )

    # ==================================================================================
    # Relationship (From other tables/models)
    # ==================================================================================

    # From department
    main_department = relationship(
        "Department",
        back_populates = "sub_departments"
    )

    # ==================================================================================
    # Relationship (From other tables/models)
    # ==================================================================================

    # To Position
    positions = relationship(
        "Position", 
        back_populates = "sub_department"
    )

    # To OnboardingTask
    onboarding_tasks = relationship(
        "OnboardingTask",
        back_populates = "for_sub_department"
    )

# ==================================================================================
# Patient Registration
# ==================================================================================
class PatientRegistration(Base):
    __tablename__ = 'patient_registration'

    patient_id = Column(String(36), primary_key=True, default=text('UUID()'))
    first_name = Column(String(255), nullable=False)
    middle_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    sex = Column(String(255), nullable=False)
    birthday = Column(Date, nullable=False)
    weight = Column(String(255), nullable=False)
    height = Column(String(255), nullable=False)
    blood_type = Column(String(255), nullable=False)
    guardian = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    contact_number = Column(String(255), nullable=False)
    hospital_employee = Column(String(255), nullable=False)
    medical_history_number = Column(String(36), ForeignKey('medical_history.medical_history_number'), nullable=True)
    dp_id = Column(String(36), ForeignKey('discount_privillages.dp_id'), nullable=True)
    status = Column(String(255),nullable=True, default="Active")
    patient_type = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    medical_history = relationship('MedicalHistory')
    discount_privillages = relationship('Discount')

# ==================================================================================
# Inpatient Table
# ==================================================================================

class Inpatient(Base):
    __tablename__ = 'inpatients'

    admission_id = Column(String(255), primary_key=True, default=text('UUID()'))
    inpatient_no = Column(String(255), nullable=False)
    patient_id  = Column(String(255), ForeignKey('patient_registration.patient_id'), nullable=True)
    room_number = Column(String(36), ForeignKey('rooms.room_id'), nullable=False)
    # room_type = Column(String(255), nullable=True)
    date_admitted = Column(DateTime, default=text('NOW()'))
    reason_of_admittance = Column(String(255), nullable=True)
    department = Column(String(255), nullable=True)
    diagnosis = Column(String(255), nullable=True)
    tests = Column(String(255), nullable=True)
    treatments = Column(String(255), nullable=True)
    surgery = Column(String(255), nullable=True)
    # medication = Column(String(255), nullable=True)
    # dosage = Column(String(255), nullable=True)
    # frequency = Column(String(255), nullable=True)
    # ending_date = Column(Date, nullable=True)
    status = Column(String(255),nullable=True, default="Active")
    is_accepting_visits = Column(String(255), nullable=True)
    patient_status = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    room = relationship('Room', foreign_keys=[room_number])
    patientFK = relationship('PatientRegistration', foreign_keys=[patient_id])

    #favor na idagdag
    my_prescriptions = relationship("Prescription", primaryjoin="and_(Inpatient.admission_id==Prescription.admission_id)",back_populates="inpatient_FK")

# ==================================================================================
# Outpatient Table
# ==================================================================================
class Outpatient(Base):
    __tablename__ = 'outpatients'

    outpatient_id = Column(String(255), primary_key=True, default=text('UUID()'))
    outpatient_no = Column(String(255), nullable=False)
    patient_id  = Column(String(255), ForeignKey('patient_registration.patient_id'), nullable=True)
    walk_in_date = Column(DateTime, default=text('NOW()'))
    purpose = Column(String(255), nullable=False)
    test = Column(String(255), nullable=True)
    treatment_summary = Column(String(255), nullable=True)
    # medication = Column(String(255), nullable=True)
    # dosage = Column(String(255), nullable=True)
    # frequency = Column(String(255), nullable=True)
    # ending_date = Column(Date, nullable=True)
    diagnosis = Column(String(255), nullable=True)
    status = Column(String(255),nullable=True, default="Active")
    patient_status = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    patientFK = relationship('PatientRegistration')

# ==================================================================================
# Discharge Table
# ==================================================================================
class DischargeManagement(Base):
    __tablename__ = 'discharge_management'

    discharge_id = Column(String(255), primary_key=True, default=text('UUID()'))
    discharge_no = Column(String(255), nullable=False)
    patient_id  = Column(String(255), ForeignKey('patient_registration.patient_id'), nullable=True)
    admission_id = Column(String(255), ForeignKey('inpatients.admission_id'), nullable=True)
    reason_of_admittance = Column(String(255), nullable=False)
    diagnosis_at_admittance = Column(String(255), nullable=False)
    date_admitted = Column(DateTime, default=text('NOW()'))
    treatment_summary = Column(String(255), nullable=False)
    discharge_date = Column(Date, nullable=True)
    physician_approved = Column(String(255), nullable=False)
    discharge_diagnosis = Column(String(255), nullable=False)
    further_treatment_plan = Column(String(255), nullable=False)
    next_check_up_date = Column(Date, nullable=True)
    client_consent_approval = Column(String(255), nullable=False)
    # medication = Column(String(255), nullable=True)
    # dosage = Column(String(255), nullable=True)
    # frequency = Column(String(255), nullable=True)
    # ending_date = Column(Date, nullable=True)
    #check if the patient is paid or not
    status = Column(String(255),nullable=False, default="Unpaid")
    active_status = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    discharge_inpatientFk = relationship('Inpatient', foreign_keys=[admission_id])
    patientFK = relationship('PatientRegistration', foreign_keys=[patient_id])

# ==================================================================================
# Discount Table
# ==================================================================================

class Discount(Base):
    __tablename__ = 'discount_privillages'

    dp_id = Column(String(36), primary_key=True, default=text('UUID()'))
    ph_id = Column(String(255), nullable=True)
    end_of_validity = Column(String(255), nullable=True)
    sc_id = Column(String(255), nullable=True)
    municipality = Column(String(255), nullable=True)
    pwd_id = Column(String(255), nullable=True)
    type_of_disability = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

# ==================================================================================
# Medical Supplies Prescription Table
# ==================================================================================

class MedicalSupplies_PR(Base):
    __tablename__= 'medicalsupplies_pr'

    medicsupp_prid= Column(String(36), primary_key=True,  default=text('UUID()'))
    ms_no = Column(String(36), nullable=False,unique=True, index=True)
    # med_id = Column(String(36), ForeignKey("medicine.med_id"),nullable=True)
    med_sup_id = Column(String(36),nullable=True)
    quantity = Column(Integer,nullable=False)
    cancellation_return = Column(Float, nullable=False, default="0")
    prescription_id = Column(String(36), ForeignKey("prescriptions.prescription_id"),nullable=True)
    created_at = Column(DateTime,nullable=False, default=text('NOW()'))
    updated_at = Column(DateTime,nullable=True, default=text('NOW()'))

    prescription_info = relationship("Prescription", foreign_keys=[prescription_id])
    # med_id_FK = relationship('Medicine', foreign_keys=[med_id])

# ==================================================================================
# Medical History Table
# ==================================================================================

class MedicalHistory(Base):
    __tablename__ = 'medical_history'

    medical_history_number = Column(String(36), primary_key=True, default=text('UUID()'))
    # patient_id = Column(String(255), ForeignKey('patient_registration.patient_id'), nullable=True)
    # prev_hospital = Column(String(255), nullable=True)
    # prev_doctor = Column(String(255), nullable=True)
    prev_diagnosis = Column(String(255), nullable=True)
    prev_treatments = Column(String(255), nullable=True)
    prev_surgeries = Column(String(255), nullable=True)
    prev_medications = Column(String(255), nullable=True)
    allergies = Column(String(255), nullable=True)
    health_conditions = Column(String(255), nullable=True)
    special_privillages = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    # medical_historyFk = relationship('PatientRegistration', back_populates='medical_history')

# ==================================================================================
# Medicine Prescription Table
# ==================================================================================

class Medicine_PR(Base):
    __tablename__= 'medicine_pr'

    medpr_id= Column(String(36), primary_key=True, default=text('UUID()'))
    medicine_no = Column(String(36), nullable=False,unique=True, index=True)
    med_id = Column(String(36), ForeignKey("medicine.med_id"),nullable=True)
    quantity = Column(Integer,nullable=False)
    intake = Column(String(255),nullable=False)
    frequency = Column(String(255),nullable=False)
    dosage = Column(String(255),nullable=False)
    doctor_prescribed = Column(String(255),nullable=False)
    cancellation_return = Column(Float, nullable=False, default="0")
    prescription_id = Column(String(36), ForeignKey("prescriptions.prescription_id"),nullable=True)
    med_pres_status = Column(String(255),nullable=False, default="Unpaid")
    created_at = Column(DateTime,nullable=False, default=text('NOW()'))
    updated_at = Column(DateTime,nullable=True, default=text('NOW()'))

    med_id_FK = relationship('Medicine', foreign_keys=[med_id])
    prescription_FK = relationship('Prescription', foreign_keys=[prescription_id])

# ==================================================================================
# Medicine Table
# ==================================================================================

class Medicine(Base):
    __tablename__= 'medicine'

    med_id= Column(String(36), primary_key=True, default=text('UUID()'))
    medicine_number = Column(Integer, nullable=False,unique=True, index=True)
    medicine_name = Column(String(255), nullable=False)
    created_at = Column(DateTime,nullable=False, default=text('NOW()'))
    updated_at = Column(DateTime,nullable=True, default=text('NOW()'))

# ==================================================================================
# Patient Room Table
# ==================================================================================

class PatientRoom(Base):
    __tablename__ = 'patient_room'

    patient_room_id = Column(String(36), primary_key=True, default=text('UUID()'))
    room_number = Column(String(36), ForeignKey('rooms.room_id'), nullable=False)
    admission_id = Column(String(36), ForeignKey('inpatients.admission_id'), nullable=False)
    status = Column(String(255), nullable=False, server_default="Active")
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))


    patroom_roomFk = relationship('Room', foreign_keys=[room_number])
    patroom_inpatientsFk = relationship('Inpatient', foreign_keys=[admission_id])

# ==================================================================================
# Prescription Table
# ==================================================================================

class Prescription(Base):
    __tablename__= 'prescriptions'

    prescription_id= Column(String(36), primary_key=True,  default=text('UUID()'))
    prescription_no = Column(String(255), nullable=False,unique=True, index=True)
    admission_id = Column(String(36),ForeignKey("inpatients.admission_id"),nullable=True)
    outpatient_id = Column(String(255), ForeignKey('outpatients.outpatient_id'), nullable=True)
    date_prescribed = Column(Date,nullable=False, default=text('NOW()'))
    patient_status = Column(String(255), nullable=True)
    status = Column(String(255),nullable=False, default="Unpaid")
    created_at = Column(DateTime,nullable=False, default=text('NOW()'))
    updated_at = Column(DateTime,nullable=True, default=text('NOW()'))

    inpatient_FK = relationship('Inpatient', foreign_keys=[admission_id])
    outpatient_Fk = relationship('Outpatient', foreign_keys=[outpatient_id])

    #favor na ipasok
    medicines_prescription = relationship("Medicine_PR", primaryjoin="and_(Prescription.prescription_id==Medicine_PR.prescription_id)",back_populates="prescription_FK")
    medical_prescription = relationship("MedicalSupplies_PR", primaryjoin="and_(Prescription.prescription_id==MedicalSupplies_PR.prescription_id)",back_populates="prescription_info")

# ==================================================================================
# Previous Doctor Table
# ==================================================================================

class PrevDoctor(Base):
    __tablename__= 'prev_doctor'

    prev_did= Column(String(36), primary_key=True, default=text('UUID()'))
    medical_history_number = Column(String(255), ForeignKey('medical_history.medical_history_number'), nullable=True)
    doctor_name = Column(String(255), nullable=True) 
    created_at = Column(DateTime,nullable=False, default=text('NOW()'))
    updated_at = Column(DateTime,nullable=True, default=text('NOW()'))

    medical_history_fk = relationship("MedicalHistory", foreign_keys=[medical_history_number])

# ==================================================================================
# Previous Hospital Table
# ==================================================================================

class PrevHospital(Base):
    __tablename__= 'prev_hospital'

    prev_hid= Column(String(36), primary_key=True, default=text('UUID()'))
    medical_history_number = Column(String(255), ForeignKey('medical_history.medical_history_number'), nullable=True)
    hospital_name = Column(String(255), nullable=True) 
    created_at = Column(DateTime,nullable=False, default=text('NOW()'))
    updated_at = Column(DateTime,nullable=True, default=text('NOW()'))

    medical_history_fk = relationship("MedicalHistory", foreign_keys=[medical_history_number])

# ==================================================================================
# Room Table
# ==================================================================================

class Room(Base):
    __tablename__ = 'rooms'

    room_id = Column(String(36), primary_key=True, default=text('UUID()'))
    room_number = Column(String(255), nullable=False)
    date_admitted = Column(DateTime, default=text('NOW()'))
    admission_id = Column(String(255), ForeignKey('inpatients.admission_id'), nullable=True)
    outpatient_id = Column(String(255), ForeignKey('outpatients.outpatient_id'), nullable=True)
    room_type_id = Column(String(36), nullable=True)
    location = Column(String(36), nullable=True)
    room_count = Column(Integer, nullable=True)
    room_status = Column(String(36), nullable=True, default="0")
    active_status = Column(String(36), nullable=False)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    # rooms_inpatientFk = relationship('Inpatient')
    room_inpatientFk = relationship('Inpatient', foreign_keys=[admission_id])
    room_outpatientFk = relationship('Outpatient', foreign_keys=[outpatient_id])

