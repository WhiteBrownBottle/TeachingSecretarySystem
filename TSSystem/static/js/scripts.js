jQuery(document).ready(function() {

    /*
        Fullscreen background
    */
    $.backstretch("static/img/backgrounds/background.jpg");

    /*
        Form validation
    */
    $('.login-form input[type="text"], .login-form input[type="password"], .login-form textarea').on('focus', function() {
        $(this).removeClass('input-error');
    });

    $('.login-form').on('submit', function(e) {
        if (document.getElementById("denglu").isclick == 1 ){
            $(this).find('input[type="text"], input[type="password"], textarea').each(function() {
                if ($(this).val() == "") {
                    e.preventDefault();
                    $(this).addClass('input-error');
                } else {
                    $(this).removeClass('input-error');
                }
            });
        }
    });


    function toSubmit(frm) {
        var obj = getFormJson(frm);
        var user = $('#wrap input[name="payMethod"]:checked ').val(); //身份 管理员：1 教师：2 学生：3
        $(this).ajaxSubmit({
            data: {'username': $("#Username").val(), 'password': $("#Password").val(),'identify':user},
            type: "post", //提交方式
            dataType: "json", //数据类型
            url: "", //请求url
            clearForm: true,
            resetForm: true,
            success: function(data) { //提交成功的回调函数
                if (data.status == 1) {
                    alert('登录成功');
                } else {
                    alert('帐号或密码错误');
                }
            }
        });
    }

});
