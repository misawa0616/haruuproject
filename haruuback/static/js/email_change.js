//import "../css/email_change.css";

var app = new Vue({
  delimiters: ["[[", "]]"],
  el: "#app",
  data: {
    after_change_email_error: initial_after_change_email_error,
    after_change_email_confirm_error: initial_after_change_email_confirm_error,
    password_error: initial_password_error,
    after_change_email: initial_after_change_email,
    after_change_email_confirm: initial_after_change_email_confirm,
    password: initial_password,
    message: initial_message,
  },
  beforeCreate: function () {
    window.onpageshow = function () {
      document.f1.reset();
    };
    history.replaceState(null, document.getElementsByTagName('title')[0].innerHTML, null);
    window.addEventListener('popstate', function (e) {
      window.location.reload();
    });
  }
});
