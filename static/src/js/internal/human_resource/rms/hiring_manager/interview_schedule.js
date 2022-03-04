"use strict";

/**
 * ==============================================================================
 * CONSTANTS
 * ==============================================================================
*/

// Get Job Post ID from the URL
const jobPostID = getPathnamePart(2);


/**
 * ==============================================================================
 * JOB POST SUMMARY
 * ==============================================================================
*/

/** Set Job Post Summary */
ifSelectorExist('#jobPostSummary', () => {
    GET_ajax(`${ ROUTE.API.H }job-posts/${ jobPostID }`, {
        success: result => {

            const manpowerRequest = result.manpower_request

            // Set Job Post Position
            setContent('#position', manpowerRequest.vacant_position.name);

            // Set Job Post Status
            setContent('#jobPostStatus', () => {
                const expiresAt = result.expiration_date;
                if(isEmptyOrNull(expiresAt) || isAfterToday(expiresAt))
                    return TEMPLATE.DT.BADGE('info', 'On Going');
                else if(isBeforeToday(expiresAt))
                    return TEMPLATE.DT.BADGE('danger', 'Ended');
                else
                    return TEMPLATE.DT.BADGE('warning', 'Last day today');
            });

            //  Set Job Posted At
            setContent('#jobPostedAt',`Posted ${ formatDateTime(result.created_at, 'Date') }`);

            // Set Staff needed
            setContent('#staffsNeeded', () => {
                const staffsNeeded = manpowerRequest.staffs_needed;
                return `${ staffsNeeded } new ${ pluralize('staff', staffsNeeded) }`;
            });
            
            // Set Employment Type
            setContent('#employmentType', manpowerRequest.employment_type.name);

            // Set Deadline
            setContent('#deadline', () => {
                const deadline = manpowerRequest.deadline;
                return isEmptyOrNull(deadline) ? 'No deadline' : `Until ${ formatDateTime(deadline, "Date") }`
            });

            $('#jobPostSummaryLoader').remove();
            showElement('#jobPostSummary');
        },
        error: () => toastr.error('There was an error in getting job post details')
    });

});



/**
 * ==============================================================================
 * CREATE SCHEDULE
 * ==============================================================================
*/

let selectApplicant = $('#selectApplicant'), selectedApplicants = [];

/** If Create Interview Schedule Form is loaded */
ifSelectorExist('#createInterviewScheduleForm', () => {
    GET_ajax(`${ ROUTE.API.H }job-posts/${ jobPostID }/applicants/for-interview`, {
        success: result => {
            selectApplicant.empty();
            selectApplicant.append(`<option></option>`);

            if(result.length > 0) {
                result.forEach(i => {
                    const intervieweeInfo = i.interviewee_info;

                    if(isEmptyOrNull(intervieweeInfo)) {
                        const applicantName = formatName('F M. L, S', {
                            firstName  : i.first_name,
                            middleName : i.middle_name,
                            lastName   : i.last_name,
                            suffixName : i.suffix_name
                        });
                        selectApplicant.append(`<option value="${ i.applicant_id }">${ applicantName }</option>`);
                    }
                });
            } else selectApplicant.append(`<option disabled>No applicants were found</option>`);
            
            $('#selectApplicant').select2({
                placeholder: "Please select applicant here and add",
            });
        },
        error: () => toastr.error('There was an error in getting applicants')
    });

    selectApplicant.on('change', () => isEmptyOrNull(selectApplicant.val()) ? disableElement('#addApplicantBtn') : enableElement('#addApplicantBtn'));

    $('#addApplicantBtn').on('click', () => {
        btnToLoadingState('#addApplicantBtn');
        disableElement('#selectApplicant');

        const selectedApplicant = selectApplicant.val();

        GET_ajax(`${ ROUTE.API.H }applicants/${ selectedApplicant }/interviewee-info`, {
            success: result => {
                const intervieweeFullName = formatName('F M. L, S', {
                    firstName  : result.first_name,
                    middleName : result.middle_name,
                    lastName   : result.last_name,
                    suffixName : result.suffix_name
                });

                const dtBody = $('#selectedApplicantsDTBody');

                if(selectedApplicants.length == 0) dtBody.empty();

                dtBody.append(`
                    <tr id="interviewee-${ result.applicant_id }">
                        <td class="w-100">
                            <div>${ intervieweeFullName }</div>
                            ${ TEMPLATE.SUBTEXT(result.email) }
                            ${ TEMPLATE.SUBTEXT(result.contact_number) }
                        </td>
                        <td class="text-center">
                            <a 
                                href="${ BASE_URL_WEB }static/app/files/resumes/${ result.resume }" 
                                class="btn btn-sm btn-secondary text-nowrap"
                                target="_blank"
                            >
                                <span class="d-none d-md-inline-block">View Resume</span>
                                <i class="fas fa-file-alt ml-md-1"></i>
                            </a>
                        </td>
                        <td class="text-center">
                            <button 
                                type="button" 
                                class="btn btn-sm btn-danger" 
                                onclick="removeApplicant('${ result.applicant_id }')"
                            >
                                <i class="fas fa-trash-alt"></i>
                            </button>
                        </td>
                    </tr>
                `);

                selectedApplicants.push(`${ result.applicant_id }`);

                if(selectedApplicants.length > 0) enableElement('#saveBtn');

                $(`#selectApplicant option[value='${ result.applicant_id }']`).prop('disabled', true).trigger('change');

                selectApplicant.val('').trigger('change');

                setContent('#addApplicantBtn', TEMPLATE.LABEL_ICON('Add', 'plus'));
                enableElement('#selectApplicant');
            },
            error: () => {
                toastr.error('There was na error in getting applicant details');
                btnToUnloadState('#addApplicantBtn', TEMPLATE.LABEL_ICON('Add', 'plus'));
            }
        });
    });
});

/** Remove Applicant */
const removeApplicant = (applicantID) => {
    showModal('#confirmRemoveApplicantModal');
    setValue('#applicantID', applicantID);
}

/** Validate Confirm Remove Applicant Form */
validateForm('#confirmRemoveApplicantForm', {
    rules: {
        applicantID: { required: true }
    },
    messages: {
        applicantID: { required: 'This must have a value' }
    },
    submitHandler: () => {
        const applicantID = generateFormData('#confirmRemoveApplicantForm').get('applicantID');

        selectedApplicants = jQuery.grep(selectedApplicants, value => { return value != applicantID });
        $(`#interviewee-${ applicantID }`).remove();
        $(`#selectApplicant option[value='${ applicantID }']`).prop('disabled', false).trigger('change');

        if(selectedApplicants.length == 0) {
            setContent('#selectedApplicantsDTBody', `
                <tr>
                    <td colspan="3">
                        <div class="py-5 text-center">
                            <h3>No applicants has been added</h3>
                            <div class="text-secondary">Applicants that you are going to add will display here</div>
                        </div>
                    </td>
                </tr>
            `);
            disableElement('#saveBtn');
        }

        hideModal('#confirmRemoveApplicantModal');
        toastr.info('An applicant has been removed from the list');
        return false;
    }
});

/** When Confirm Remove Applicant Modal is hidden */
onHideModal('#confirmRemoveApplicantModal', () => resetForm('#confirmRemoveApplicantForm'));

/** Validate Create Schedule Form */
validateForm('#createInterviewScheduleForm', {
    rules: {
        scheduledDate: {
            required: true,
            afterToday: true
        },
        startSession: {
            required: true,
            beforeTime: '#endSession'
        },
        endSession: {
            required: true,
            afterTime: '#startSession'
        }
    },
    messages: {
        scheduledDate: {
            required: 'Please select the date for your schedule',
            afterToday: 'This must be in the future'
        },
        startSession: {
            required: 'Please select the time where session starts',
            beforeTime: 'Start session must be before the set end session'
        },
        endSession: {
            required: 'Please select the time where session end',
            afterTime: 'End session must be after the set start session'
        }
    },
    submitHandler: () => {
        showModal('#confirmCreateInterviewScheduleModal');
        return false;
    }
});

/** Create Schedule Button */
onClick('#createScheduleBtn', () => {
    btnToLoadingState('#createScheduleBtn');
    disableElement('#cancelConfirmCreateInterviewScheduleBtn');

    const formData = generateFormData('#createInterviewScheduleForm');
    const get = (n) => { return formData.get(n) }

    let interviewees = [];
    selectedApplicants.forEach(a => interviewees.push({applicant_id: a}));

    const data = {
        job_post_id: jobPostID,
        scheduled_date: get('scheduledDate'),
        start_session: get('startSession'),
        end_session: get('endSession'),
        interviewees: interviewees
    }

    POST_ajax(`${ ROUTE.API.H }interview-schedule`, data, {
        success: result => {
            if(result) {
                setSessionedAlertAndRedirect({
                    theme: "success",
                    message: "A new schedule is successfully created",
                    redirectURL: `${ ROUTE.WEB.H }job-posts/${ jobPostID }/applicants/for-interview`
                });
            }
        },
        error: () => {
            hideModal('#confirmCreateInterviewScheduleModal');
            btnToUnloadState('#createScheduleBtn', TEMPLATE.LABEL_ICON('Yes, create it!', 'check'));
            enableElement('#cancelConfirmCreateInterviewScheduleBtn');
            toastr.error('There was an error in creating an interview schedule');
        }
    });
});
