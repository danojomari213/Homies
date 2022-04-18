"use strict";

/**
 * ==============================================================================
 * NOTIFICATIONS
 * ==============================================================================
*/

/** Get notifications */
getUserNotifications({
    apiRoute: ROUTE.API.H,
    webRoute: ROUTE.WEB.H,
    notifTypes: {
        "Manpower Request": {
            icon: "copy",
            subtypes: {
                "Signed Request": {
                    getContent: data => {
                        const author = data.notification_created_by;
                        const authorName = formatName('F M. L, S', {
                            firstName: author.first_name,
                            middleName: author.middle_name,
                            lastName: author.last_name,
                            suffixName: author.suffix_name,
                        });
                        return `A manpower request has been signed by <b>${ authorName }</b>.`
                    }
                },
            }
        }
    }
});

/** Unread notifications */
const unreadNotification = (notificationID) => {
    PUT_ajax(`${ ROUTE.API.H }notifications/${notificationID}/unread`, {
        success: () => {},
        error: () => toastr.error('There was an error in updating recruitment notification')
    });
}