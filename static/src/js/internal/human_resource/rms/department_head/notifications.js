"use strict";

/**
 * ==============================================================================
 * NOTIFICATIONS
 * ==============================================================================
*/

/** Get all notifications */
getUserNotifications({
    apiRoute: ROUTE.API.DH,
    webRoute: ROUTE.WEB.DH,
    notifTypes: {
        "Manpower Request": {
            icon: "copy",
            subtypes: {
                "Request for Manpower": {
                    getContent: data => {
                        const author = data.notification_created_by;
                        const authorName = formatName('F M. L, S', {
                            firstName: author.first_name,
                            middleName: author.middle_name,
                            lastName: author.last_name,
                            suffixName: author.suffix_name,
                        });
    
                        return `<b>${ authorName }</b> has been requested for manpower.`
                    }
                }
            }
        }
    }
});

/** Unread notifications */
const unreadNotification = (notificationID) => {
    PUT_ajax(`${ ROUTE.API.DH }notifications/${notificationID}/unread`, {
        success: () => {},
        error: () => toastr.error('There was an error in updating recruitment notification')
    });
}
