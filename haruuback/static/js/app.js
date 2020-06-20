import '../css/app.css'
import * as common from './common/common.js';

console.log(common)
console.log(common.Messages.const)
console.log(common.Messages.const().EM001)

var vm = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        email: 'a',
        after_change_email: '',
        confirm_after_change_email: '',
        password: '',
        todos: []
        },
    methods: {
        updateDB: function(e) {
        },
    }
})