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
    alert('测试');
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
