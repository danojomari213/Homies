'use strict';

/** FOR CAROUSEL */

const CAROUSEL_INTERVAL_SECONDS = 3;

$('#homeCarousel').carousel({
    interval: CAROUSEL_INTERVAL_SECONDS * 1000
});

// Pause the carousel from cycling if document is hidden
// To reduce lag and other reasons
document.addEventListener('visibilitychange', () => {
    document.hidden 
        ? $('#homeCarousel').carousel('pause') 
        : $('#homeCarousel').carousel('cycle')
});