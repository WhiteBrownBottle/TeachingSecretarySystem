/*
    Fullscreen background
*/
$.backstretch("static/img/backgrounds/background.jpg");

function login() {
    // alert('已进入login');
    form1.username.style.borderColor = '#dddddd';
    form1.password.style.borderColor = '#dddddd';
    var flag = 'y';
    if (form1.password.value == "") {
        form1.password.style.borderColor = 'red';
        form1.password.focus();
        flag = 'n';
    }
    if (form1.username.value == "") {
        form1.username.style.borderColor = 'red';
        form1.username.focus();
        flag = 'n';
    }

    if (document.getElementById("radio1").checked == false && document.getElementById("radio2").checked == false && document.getElementById("radio3").checked == false) {
        swal("请选择身份", "", "error");
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
                if(data.msg=="1") window.location.href="/xadmin";
                if(data.msg=="2") window.location.href="/teacher";
                if(data.msg=="3") window.location.href="/student";
            } else if (data.status == 'fail') {
                swal(data.msg, "", "error");
            }
        }
    });
}

function forgetPassword() {
    form1.username.style.borderColor = '#dddddd';
    var flag = 'y';

    if (form1.username.value == "" && document.getElementById("radio1").checked == false && document.getElementById("radio2").checked == false && document.getElementById("radio3").checked == false) {
        form1.username.style.borderColor = 'red';
        swal("请填写您的用户名和选择身份!", "", "error");
        form1.username.focus();
        return false;
    }

    if (form1.username.value == "") {
        form1.username.style.borderColor = 'red';
        swal("请填写您的用户名!", "", "error");
        form1.username.focus();
        flag = 'n';
    }

    if (document.getElementById("radio1").checked == false && document.getElementById("radio2").checked == false && document.getElementById("radio3").checked == false) {
        swal("请选择身份", "", "error");
        flag = 'n';
    }
    if (flag == 'n') return false;

    $.ajax({
        data: {
            'username': document.getElementById("username").value,
            'identify': $('input:radio:checked').val() //身份 管理员：1 教师：2 学生：3
        },
        type: "post", //提交方式
        dataType: "json", //数据类型
        url: "/forgetpwd/", //请求url
        success: function(data) {
            if (data.status == 'success') {
            swal("已向您的邮箱发送初始密码，请查看并及时修改！","","success");
            } else if (data.status == 'fail') {
                swal(data.msg, "", "error");
            }
        }
    });
}
