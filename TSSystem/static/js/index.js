/*
    Fullscreen background
*/
$.backstretch("static/img/backgrounds/background.jpg");

function login() {
    // alert('已进入login');
    form1.username.style.borderColor = '#dddddd';
    form1.password.style.borderColor = '#dddddd';
    var flag = 'y';
    if (form1.username.value == "") {
        form1.username.style.borderColor = 'red';
        form1.username.focus();
        flag = 'n';
    }
    if (form1.password.value == "") {
        form1.password.style.borderColor = 'red';
        form1.password.focus();
        flag = 'n';
    }

    if (form2.radio1.checked == false && form2.radio2.checked == false && form2.radio3.checked == false) {
        alert('请选择身份');
        flag = 'n';
    }
    if (flag == 'n') return false;

    $.ajax({
        data: {
            'username': document.getElementById("username").value,
            'password': document.getElementById("password").value,
            'identify': $('input:radio:checked').val() //身份 管理员：1 教师：2 学生：3
        },
        type: "post", //提交方式
        dataType: "json", //数据类型
        url: "/login/", //请求url
        success: function(data) {
            if (data.status == 'success') {
                if(msg=="1") window.location.href="/xadmin";
                if(msg=="2") window.location.href="/student";
                if(msg=="3") window.location.href="/teacher";
            } else if (data.status == 'fail') {
                swal({
                    icon: "error",
                    text: data.msg,
                });
            }
        }
    });
}
