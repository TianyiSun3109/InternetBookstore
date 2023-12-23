 <?php
header('Content-Type:application/json;charset=UTF-8');
$uname=$_POST["uname"];
$upwd=$_POST["upwd"];
$conn=mysqli_connect("localhost", "root", "root","jd");
$sql="SET NAMES UTF8";
mysqli_query($conn,$sql);
if (!$sql) {
    die('Error in SQL query: ' . mysqli_error($conn));
}
$sql="SELECT*FROM jd_user WHERE uname='$uname' AND upwd='$upwd'";
$result=mysqli_query($conn,$sql);
if(!$result){
	echo '{"code":1001,"msg":"SQL语法错误"}';
}else{
	if(($user=mysqli_fetch_assoc($result))===null){
		echo '{"code":1002,"msg":"用户名或密码错误"}';
	}else{
		echo '{"code":1000,"msg":"登陆信息验证正确"}';
	}
} 

