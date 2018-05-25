/*
    Fullscreen background
*/
$.backstretch("static/img/backgrounds/background.jpg");

/*
    Form validation
*/
// $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
//     $(this).removeClass('input-error');
// });

// $('.login-form').on('submit', function(e) {
//     if (document.getElementById("denglu").isclick == 1) {
//         $(this).find('input[type="text"], input[type="password"], textarea').each(function() {
//             if ($(this).val() == "") {
//                 e.preventDefault();
//                 $(this).addClass('input-error');
//             } else {
//                 $(this).removeClass('input-error');
//             }
//         });
//     }
// });

function login() {
    alert('已进入login');
    form1.username.style.borderColor = '#dddddd';
    form1.password.style.borderColor = '#dddddd';
    // if (document.getElementById("denglu").isclick == 1) {
    //     $(this).find('input[type="text"], input[type="password"], textarea').each(function() {
    //         if ($(this).val() == "") {
    //             e.preventDefault();
    //             $(this).addClass('input-error');
    //         } else {
    //             $(this).removeClass('input-error');
    //         }
    //     });
    // }
    var flag = 'y';
    if (form1.username.value == "") {
        form1.username.style.borderColor = '#4aaf51';
        form1.username.focus();
        flag = 'n';
    }
    if (form1.password.value == "") {
        form1.password.style.borderColor = '#4aaf51';
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
            'username': $("username").val(),
            'password': $("password").val(),
            'identify': $('input:radio:checked').val() //身份 管理员：1 教师：2 学生：3
        },
        type: "post", //提交方式
        dataType: "json", //数据类型
        url: "/login/", //请求url
        success: function(data) {
            if (data.status == 'success') {
                swal({
                    icon: "success",
                    text: data.msg,
                });
                vm_checkin.checkinDays++;
            } else if (data.status == 'fail') {
                swal({
                    icon: "error",
                    text: data.msg,
                });
            }
        }
    });
}
