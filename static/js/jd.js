// $(function () {
// 	$('#header-container').load('header.html');
// });

var loginName = null;

// $('#bt-login').click(function(){
// 	$.ajax({
// 		type: 'POST',
// 		url:'data/1_login.php',
// 		data:$('#login-form').serialize(),
// 		success:function(obj){
// 			if(obj.code===1000){
// 				$('.modal').fadeOut();
// 				loginName = $('[name="uname"]').val();
// 				$('#welcome').html('欢迎回来：'+loginName);
// 			}else{
// 				$('.modal .alert').html(obj.msg);
// 			}
// 		}
// 	});
// });

// 实现弹出登录或注册的模态框
$(function () {
	$('#top').on('click','#putDn',function(e){
		e.preventDefault();
		 var modalId = $(this).data('modal');
        $('#' + modalId).show();
	});
	        $('#top').on('click', '#registerLink', function(e){
            e.preventDefault();
            var modalId = $(this).data('modal');
            $('#' + modalId).show();
        });
});

// 确保在使用之前加载 jQuery
$(document).ready(function() {

    // 定义 loadProduct 函数
    function loadProduct() {
        // 这里放置加载产品的代码
        console.log('产品已加载！');
    }

    // 调用 loadProduct 函数
    loadProduct();
    
    // 其他 JavaScript 代码...

});

// function loginUser() {
//     // 获取用户名和密码输入框的值
//     var username = document.getElementById("login-form").elements["uname"].value;
//     var password = document.getElementById("login-form").elements["upwd"].value;

//     // 构建登录请求的数据
//     var data = {
//         username: username,
//         password: password
//     };
// 	// data.append("csrfmiddlewaretoken",'{{ csrf_token }}');
//     // 发送登录请求
//     fetch('login_user', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data)
//     })
//     .then(response => response.json())
//     .then(result => {
//         // 处理登录结果
//         if (result.success) {
//             // 登录成功，可以在这里执行一些操作，例如关闭模态框、更新页面等
//             closeModal('modal-login');
//             alert('登录成功！');
//         } else {
//             // 登录失败，可以在这里给用户一些反馈
//             document.getElementById('Result').innerHTML = '登录失败，请检查用户名和密码。';
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

// $(function(){
// 	loadProduct(1);
// });
// $('.pager').on('click','a',function(e){
// 	e.preventDefault();
// 	var pno=$(this).attr('href');
// 	loadProduct(pno);
// 	$(this).parent().addClass('active');
// 	$(this).parent().siblings('.active').removeClass('active');
// });




// function loadProduct(pno){
// 	$.getJSON('data/1_product_select.php',{'pno':pno},function(pager){
// 		var html='';
// 		$.each(pager.data,function(i,product){
// 			html+=`
// 				<li>
// 					<a href=""><img src="${product.pic}" alt=""/></a>
// 					<p>￥${product.price}</p>
// 					<h1><a href="">${product.pname}</a></h1>
// 					<div>
// 						<a href="" class="contrast"><i></i>对比</a>
// 						<a href="" class="p-operate"><i></i>关注</a>
// 						<a href="${product.pid}" class="addcart"><i></i>加入购物车</a>
// 					</div>
// 				</li>	
// 			`;
// 		});
// 		$('#plist>ul').html(html);
// 		var pagerHtml='';
// 		if(pager.pno-2>0){
// 			pagerHtml+=`<li><a href="${pager.pno-2}">${pager.pno-2}</a></li>`;
// 		}
// 		if(pager.pno-1>0){
// 			pagerHtml+=`<li><a href="${pager.pno-1}">${pager.pno-1}</a></li>`;
// 		}
// 		pagerHtml+=`<li class="active"><a href="${pager.pno}">${pager.pno}</a></li>`;
// 		if(pager.pno+1<=pager.pageCount){
// 			pagerHtml+=`<li><a href="${pager.pno+1}">${pager.pno+1}</a></li>`;
// 		}
// 		if(pager.pno+2<=pager.pageCount){
// 			pagerHtml+=`<li><a href="${pager.pno+2}">${pager.pno+2}</a></li>`;
// 		}
// 		$('.pager').html(pagerHtml);
// 	});
// }
// $(function(){
// 	$('#plist').on('click','.addcart',function(e){
// 		e.preventDefault();
// 		var pid=$(this).attr('href');
// 		$.post('data/1_cart_detail_add.php',{'pid':pid,'uname':loginName})
// 	})
// });
// $('#header').on('click','#settle_up',function(){
// 	location.href='shoppingcart.html?loginName='+loginName;
// });

