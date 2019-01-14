/***
 * 部分特定 url 混淆处理
 */
function getUrl(index,param){
	var url = "";
	if(index==1){//教师课程修改
		url = "/teacourse-edit/1"+getParamNumber(param);
	}else if(index==11){//教务员课程更新
		url = "/teacourse-updmodel/11"+getParamNumber(param);
	}else if(index==2){//教师课程预览
		url = "/teacourse-view/2"+getParamNumber(param);
	}else if(index==3){//教师我的课程管理详情--课前准备
		url = "/teacourse-detail/3"+getParamNumber(param);
	}else if(index==31){//教师我的课程管理详情--在线互动
		url = "/teacourse-onlineactive/31"+getParamNumber(param);
	}else if(index==32){//教师我的课程管理详情--课后批阅
		url = "/teacourse-afterread/32"+getParamNumber(param);
	}else if(index==33){//教师我的课程管理详情--学生管理
		url = "/teacourse-studentmanager/33"+getParamNumber(param);
	}else if(index==34){//教师我的课程管理详情--证书管理
		url = "/teacourse-certificate/34"+getParamNumber(param);
	}else if(index==35){//教师我的课程管理详情--公告栏
		url = "/teacourse-announcement/35"+getParamNumber(param);
	}else if(index==36){//教师我的课程管理详情--课程统计
		url = "/teacourse-statistics/36"+getParamNumber(param);
	}else if(index==37){//教师我的课程管理详情--班级管理
		url = "/teacourse-classmanager/37"+getParamNumber(param);
	}else if(index==4){//教师我的评审详情
		url = "/teacourse-review/4"+getParamNumber(param);
	}else if(index==5){//学生课程详情
		url = "/student-detail/5"+getParamNumber(param);
	}else if(index==6){//学生看视频
		url = "/student-video/6"+getParamNumber(param);
	}else if(index==7){//学生学习，考试
		url = "/student-learn/7"+getParamNumber(param);
	}else if(index==8){//学生学习，考试
		url = "/student-exam/8"+getParamNumber(param.split("_")[0])
			    +"/"+param.split("_")[1]+"68"
				+"/4"+param.split("_")[2]+"X"
			    +"/6"+param.split("_")[3]+"S/"+randomString(16);
	}else if(index==9){//mng/course/detail
		url = "/course-view/9"+getParamNumber(param);
	}else if(index==10){//web/school/detail
		url = "/course-view/10"+getParamNumber(param);
	}
	return url;
}
function getParamNumber(param){
	var para_str = param+"";
	if(para_str.length==1){
		para_str = "00"+para_str;
	}else if(para_str.length==2){
		para_str = "0"+para_str;
	}
	var param_arr = para_str.split("");
	var param_2 = "";
	if(param_arr.length>3){//如果是1位
		for(var i = 2;i<param_arr.length;i++){
			param_2 += param_arr[i];
		}
		param_arr [2] = param_2;
	}
	var parameter = randomString(3)+"/6"+param_arr[0]+"0/"+randomString(8)+"/1"+param_arr[1]+"9/"+randomString(4)+"/5"+param_arr[2]+"8/"+randomString(16);
	//默认字母小写，手动转大写
	return parameter.toUpperCase();//另toLowerCase()转小写
}

function randomString(len){
	len = len || 32;
	var chars = "0123456789ABCDEF_=/";
	var maxpos = chars.length;
	var res = "";
	for(i=0 ; i<len; i++){
		res += chars.charAt(Math.floor(Math.random() * maxpos));
	}
	return res;
}

function blankHref(url) {
		var a = document.createElement('a');
		document.body.appendChild(a);
		a.setAttribute("type", "hidden");
    a.setAttribute('href', url);
		a.setAttribute('target', '_blank');
    a.click();
}

function localtionHref(url){
	window.location.href=url;
}
