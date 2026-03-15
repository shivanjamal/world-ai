// script.js

document.addEventListener('DOMContentLoaded', function() {
  // ئەڤە ناڤێ کوکی (Cookie)ـێ یە کو دێ دوماهی دەمێ سەردانکرنێ پارێزیت
  const lastVisitCookie = 'lastVisit';

  // خواندنا دوماهی دەمێ سەردانکرنێ ژ کوکی
  let lastVisit = localStorage.getItem(lastVisitCookie) || new Date(0).toUTCString();

  // پشکنینا نویبوونان (Updates)
  checkForUpdates(lastVisit);

  // پاراستنا دەمێ نوکە وەک دوماهی دەمێ سەردانکرنێ
  localStorage.setItem(lastVisitCookie, new Date().toUTCString());

  function checkForUpdates(lastVisit) {
    // گرێدانا لێرە دێ هێتە گوهۆڕین لسەر ئادرەسەکێ ڕاستەقینە یێ API یا تە
    fetch('/api/updates?lastVisit=' + encodeURIComponent(lastVisit))
      .then(response => response.json())
      .then(data => {
        if (data.hasNewUpdates) {
          document.title = '(*) گەردۆنێ AI'; // نیشانا ستێرکێ
        }
      })
      .catch(error => console.error('Error checking for updates:', error));
  }
});