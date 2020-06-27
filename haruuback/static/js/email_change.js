//import "../css/email_change.css";
import * as common from "./common/common.js";

//console.log(common)
//console.log(common.Messages.const)
//console.log(common.Messages.const().EM001)

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
  method: {
    toError: function (message) {
      this.message = message;
      this.processing = false;
      window.scrollTo(0, 0);
    },
    validateRequired: function () {
      if (
        !this.application.contractorEmail ||
        String(this.application.contractorEmail).trim() == ""
      ) {
        this.isContractorEmailError = true;
        this.contractorEmailErrorMsg = "必須入力項目です。";
      }
    },
    validate: function () {
      pass;
    },
    click: function () {
      pass;
    },
  },
});
