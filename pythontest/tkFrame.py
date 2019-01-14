# coding=utf-8
'''交互的窗体，支持开始，暂停，关闭
'''
import json
import _thread

import tkinter as tk
from bs4 import BeautifulSoup as bs

import httptool as ht
import utilty as ut
import readjs


class tkFrame:
    # 建立窗体
    def __init__(self):

        self.window = tk.Tk()
        self.window.title('谁还不是一个小可爱呢')
        self.window.geometry('350x260')
        self.window.resizable(width=False, height=False)

        # user information
        tk.Label(self.window, text='①学号 : ').place(x=50, y=10)
        tk.Label(self.window, text='①密码 : ').place(x=50, y=40)
        tk.Label(self.window, text='②学号 : ').place(x=50, y=130)
        tk.Label(self.window, text='②密码 : ').place(x=50, y=160)

        # 配置基本的参数
        #刷时间的
        var_user = tk.StringVar()
        var_user.set('1510040209')
        self.entry_user = tk.Entry(self.window, textvariable=var_user, width=25)
        self.entry_user.place(x=100, y=10)
        var_pass = tk.StringVar()
        var_pass.set('abc123')
        self.entry_pass = tk.Entry(self.window, textvariable=var_pass, width=25)
        self.entry_pass.place(x=100, y=40)

        # 刷题目的
        var_user2 = tk.StringVar()
        var_user2.set('1510040102')
        self.entry_user2 = tk.Entry(self.window, textvariable=var_user2, width=25)
        self.entry_user2.place(x=100, y=130)
        var_pass2 = tk.StringVar()
        var_pass2.set('abc123')
        self.entry_pass2 = tk.Entry(self.window, textvariable=var_pass2, width=25)
        self.entry_pass2.place(x=100, y=160)

        # 基本状态栏1
        self.var_status = tk.StringVar()
        self.var_status.set('大概：课程未处理')
        self.entry_status = tk.Label(self.window, textvariable=self.var_status)
        self.entry_status.place(x=50, y=70)

        self.var_status_re = tk.StringVar()
        self.var_status_re.set('大概：未处理')
        self.entry_status_re=tk.Label(self.window, textvariable=self.var_status_re)
        self.entry_status_re.place(x=50,y=100)

        # 基本状态栏2
        self.var_status2 = tk.StringVar()
        self.var_status2.set('大概：作业未处理')
        self.entry_status2 = tk.Label(self.window, textvariable=self.var_status2)
        self.entry_status2.place(x=50, y=190)

        self.var_status_re2 = tk.StringVar()
        self.var_status_re2.set('大概：未处理')
        self.entry_status_re2 = tk.Label(self.window, textvariable=self.var_status_re2)
        self.entry_status_re2.place(x=50, y=220)

        self.processDo=processDo()

        # 按钮1
        self.btn_Start = tk.Button(self.window, text='①开始', command=self.startF)
        self.btn_Start.place(x=300, y=10)
        self.btn_End = tk.Button(self.window, text='①清空', command=self.endF)
        self.btn_End.place(x=300, y=45)
        # 按钮2
        self.btn_Start2 = tk.Button(self.window, text='②开始', command=self.startF2)
        self.btn_Start2.place(x=300, y=130)
        self.btn_End2 = tk.Button(self.window, text='②清空', command=self.endF2)
        self.btn_End2.place(x=300, y=165)
        # 这里是窗口的内容

        self.window.mainloop()
        # 建立窗体结束

        print('初始化完成')

    # 点击事件
    # 按钮的函数
    # 处理,先获取到学号和密码，然后调用domain
    def startF(self):
        if self.processDo is None:
            self.processDo = processDo()
        self.var_status.set('开始处理')
        username=self.entry_user.get()
        password=self.entry_pass.get()
        _thread.start_new_thread(self.processDo.mMain,(username,password,self))


    #刷题目
    def startF2(self):
        if self.processDo is None:
            self.processDo = processDo()
        self.var_status2.set('开始处理')
        username=self.entry_user2.get()
        password=self.entry_pass2.get()
        _thread.start_new_thread(self.processDo.mHomeWork,(username,password,self))


    # 退出
    def endF(self):
        self.processDo=None
        self.var_status.set('大概：课程未处理')
        self.var_status_re.set('详细：未处理')

    #刷题目退出
    def endF2(self):
        self.processDo=None
        self.var_status2.set('大概：作业未处理')
        self.var_status_re2.set('详细：未处理')

    # 大致信息提示
    def sendMessage2status(self,message):
        self.var_status.set(message)


    def sendMessage2status_re(self,message):
        self.var_status_re.set(message)

    def sendMessage2status2(self,message):
        self.var_status2.set(message)


    def sendMessage2status_re2(self,message):
        self.var_status_re2.set(message)


class processDo:
    mSession = None
    allCount = 0

    # 根据url username，password 模拟登录 均不能为空,获取到session传递给主能量
    def login(self,mainUrl, yzmUrl, loginUrl, savePath, username, password):
        sessioncurr = ht.getSessionForLogin(mainUrl, yzmUrl, loginUrl, savePath, username, password)
        if sessioncurr is not None:
            global mSession
            mSession = sessioncurr
            data = ht.getHtml('http://hnust.hunbys.com/web/students/getCourse', mSession)
            data = data.decode() #bytes解码为字符串
            count = data.count('href')
            if count is 0:
                return 1
            else:
                return 0
        else:
            return 0

    def getCourseidAndUrl(self):
        global mSession
        data=ht.getHtml('http://hnust.hunbys.com/web/students/getCourse',mSession)
        data = data.decode()
        count=data.count('href')
        if count is 0:
            coursecurr = data.split(',')[1]
            courseId = coursecurr.split(':')[2]

            preurl = 'http://hnust.hunbys.com'

            urlstr=readjs.get_des_psswd(courseId)
            urlperfect = preurl + urlstr
            urlperfect=urlperfect.encode('utf-8')
            arr = []
            arr.append(courseId)
            arr.append(urlperfect)
            return arr
        else:
            return None


    def getAllCourse(self,url):
        global mSession
        html = ht.getHtml(url, mSession)
        soup = bs(html, 'html.parser')  # 采用lxml解析更快，默认为‘html.parser’
        aarr = soup.find_all('a', href='javascript:void(0)')
        idarr = []
        num1 = 0
        num2 = 0
        for i in range(len(aarr)):
            try:
                id = aarr[i]['id']
                num1 = num1 + 1
                # print(id)
                idarr.append(id)
                self.call2Framestatus_re('获取第'+str(num1)+'个课程编号')
            except:
                num2 = num2 + 1
        global allCount
        allCount = num1
        self.call2Framestatus_re('共获取课程' + str(num1) + '个')
        return idarr

    def getVideoLength(self,url, idarr):
        global mSession
        videoLengtharr = []
        for i in range(len(idarr)):
            self.call2Framestatus_re('获取第' + str(i) + '个视频长度')
            data = ht.getHtml(ut.PGPostValusesVideoLebgth(url, self.courseId, idarr[i]), mSession)
            jsondata = json.loads(data)
            videoLengtharr.append(jsondata['videoLength'])

        return videoLengtharr

    # 单独的消耗
    def consumeTime(self,url, idarr, videoLengtharr):
        global mSession
        # url,runTime,courseId,catId
        for i in range(len(idarr)):
            data = ht.getHtml(ut.PGPostValusesXH(url, videoLengtharr[i], self.courseId, idarr[i]), mSession)
            #4954 资安编号  4942 16学院的  4944  11学院的

    # 单独的结束
    def finish(self,url, idarr):
        global mSession, allCount
        # url,runTime,courseId,catId
        successNum = 0
        failedNum = 0
        for i in range(len(idarr)):
            print('处理中...' + str(i) + '/' + str(allCount))
            data = ht.postHtml(ut.PGPostValusesFinish(url, idarr[1]), mSession)
            jsondata = json.loads(data)
            if jsondata is 1:
                successNum = successNum + 1
            else:
                failedNum = failedNum + 1
                print('失败处理:' + idarr[i])
        print('成功结束:' + str(successNum) + '/' + str(allCount))
        print('失败结束:' + str(failedNum) + '/' + str(allCount))

    # 合并消耗和结束
    def connsumeTimeAndFinish(self,url1, url2, idarr, videoLengtharr):
        global mSession, allCount
        successNum = 0
        failedNum = 0
        # 先消耗，后结束range(len(idarr))
        for i in range(len(idarr)):
            self.call2Framestatus_re('详细：处理中...' + str(i) + '/' + str(allCount) + ',正在拉进度条')
            print('详细：处理中...' + str(i) + '/' + str(allCount))
            ht.postHtml(url1, ut.PGPostValusesXH(url1, videoLengtharr[i], self.courseId, idarr[i]), mSession)
            self.call2Framestatus_re('详细：处理中...' + str(i) + '/' + str(allCount) + ',正在通知服务器结束视频')
            data = ht.postHtml(src=ut.PGPostValusesFinish(url2, idarr[i]), data=None, session=mSession)
            jsondata = json.loads(data)
            self.call2Framestatus_re('详细：处理中...' + str(i) + '/' + str(allCount) + ',正在监督服务器工作')
            ht.postHtml(url1, ut.PGPostValusesXH(url1, videoLengtharr[i], self.courseId, idarr[i]), mSession)

            # data = ht.getHtml(ut.PGPostValusesXH(url1, videoLengtharr[i], 4942, idarr[i]), mSession)
            if jsondata['code'] is 1:
                successNum = successNum + 1
            else:
                failedNum = failedNum + 1
                catIdcurr = idarr[i].encode('utf-8')
                print('失败处理:' + catIdcurr)
            self.call2Framestatus_re('详细：处理中...' + str(i) + '/' + str(allCount) + ',服务器统计数据')
        self.call2Framestatus('本次处理结束，请点击清空后开始或退出')
        self.call2Framestatus_re('成功处理:' + str(successNum) + '/' + str(allCount)+'，失败处理:' + str(failedNum) + '/' + str(allCount))
        print('成功处理:' + str(successNum) + '/' + str(allCount))
        print('失败处理:' + str(failedNum) + '/' + str(allCount))

    #课后作业实现,放在处理的外面
    def dohomework(self,subminexamarr):
        global mSession
        self.call2Framestatus2('开始监督做作业')
        self.call2Framestatus_re2('做作业中...')
        print('组装结束')
        #发送答案,这个时候需要重新登录自己的
        successnum=0
        allcount=len(subminexamarr)
        for ajson in subminexamarr:
            if ajson is None:
                break
            html=ht.postHtml('http://hnust.hunbys.com/web/examination/examSubmit', ajson, mSession)
            jd=json.loads(html)
            print(ajson)
            if jd[u'code'] is 1:
                successnum=successnum+1
            prices=''
            try:
                prices=str(jd[u'data'])
            except:
                prices='Nohave'

            self.call2Framestatus_re2('做作业中...成功/总数=》'+str(successnum)+'/'+str(allcount)+',分数：'+prices)
        self.call2Framestatus2('作业结束，部分可能没有题目或不允许做')
        return

    def getreferansAndPG(self):
        values = {"courseId": self.courseId}
        # values=json.dumps(values)
        global mSession
        # 获取全部的exid catalogname（会少一点）  failpath  ，typename，ccid就是对应章节测试的id
        data = ht.postHtml('http://hnust.hunbys.com/web/students/findTestInCourseChange', values, mSession)
        # 测试两种方式，第一种是用字符串解析，第二用途转成jsonn解析，下面的要重新写，这样写的不对，太麻烦了，还是用json
        # #获取exxid
        # dataarr = data.split('"testId":')
        # for a in dataarr:
        #     b=a.split(',"type":')
        #     if len(b) > 1:
        #         exid=b[0]
        #         exidarr.append(exid)
        # #获取cata
        # dataarr=data.split('catalogName":"')
        # for a in dataarr:
        #     b=a.split('","')
        #     if len(b) > 1:
        #         cata=b[0]
        #         cataarr.append(cata)
        # # 获取file
        # dataarr = data.split('filePath":"/')
        # for a in dataarr:
        #     b = a.split('","')
        #     if len(b) > 1:
        #         filep = b[0]
        #         filearr.append(filep)
        # # 获取type
        # dataarr = data.split('typeName":"')
        # for a in dataarr:
        #     b = a.split('"},{')
        #     if len(b) > 1:
        #         typen = b[0]
        #         typenname.append(typen)
        # json
        depenarr = self.getdepenarrwithdata(data=data)

        self.call2Framestatus2('开始尝试获取答案...尝试获取参考答案')
        # 获取到全部的参考答案,根据exid
        referarr = []
        for eid in depenarr[2]:
            values = {'exId': eid}
            datarefer = ht.postHtml('http://hnust.hunbys.com/web/students/findAnswerListByExid', values, mSession)
            jsondata = None
            try:
                jsondata = json.loads(datarefer)
            except:
                self.call2Framestatus_re2(str(eid) + '未考试或不存在答案')
                print(str(eid) + '未考试或不存在答案')

            if jsondata is not None:
                arrcurr = jsondata[u'answer']
                referwithexid = []
                for a in arrcurr:
                    referanswercurr = []
                    qidcurr = a[u'quesId']
                    qtypecurr = a[u'type']
                    acurr = a[u'referAnswer']
                    rcurr = acurr.encode('utf-8')
                    referanswercurr.append(qidcurr)
                    referanswercurr.append(qtypecurr)
                    referanswercurr.append(rcurr)
                    referwithexid.append(referanswercurr)
                refecurr = []
                refecurr.append(eid)
                refecurr.append(referwithexid)
                referarr.append(refecurr)
            else:
                referarr.append(None)
        self.call2Framestatus2('开始尝试获取答案...获取参考答案成功，开始组装答案')
        # 组装答案# 第一个cata，第二个file，第三个exid,第四个type，mulu然后上面的knoid
        subminexamarr = []
        for i in range(len(referarr)):
            dependata = []
            dependata.append(self.courseId)
            dependata.append(depenarr[3][i])
            dependata.append(depenarr[2][i])
            dependata.append(depenarr[4][i])
            dependata.append(depenarr[5][i])

            answerdata = []
            answerdata = referarr[i]
            if answerdata is None:
                subminexamarr.append(None)
                break
            #
            if answerdata[0] is dependata[2]:
                referanswercurr = self.PGanswer(dependata=dependata, answerdata=answerdata)
                subminexamarr.append(referanswercurr)
            else:
                self.call2Framestatus_re2(str(answerdata[0]) + ',' + str(dependata[2]) + '不匹配')
                print(str(answerdata[0]) + ',' + str(dependata[2]) + '不匹配')
        self.call2Framestatus2('成功获取答案...组装答案成功,准备重新模拟登录')
        return subminexamarr

    #获取依据，并重新得到我们需要的
    def getdepenarrwithdata(self,data):
        jsondata = None
        try:
            jsondata = json.loads(data)
        except:
            print('获取不到依据')
            return None
        # 这是个list
        depenarr = []
        if jsondata is not None:
            jsondata = jsondata[u'cata']
            exidarr = []  # exid
            cataarr = []  # name
            filearr = []  # file
            typearr = []  # type
            cataidarr = []  # muluid
            cataidarrcurr = []  # 临时目录集合
            cataorderarrcurr = []  # 临时集合
            knoidarr = []  # knoid
            for jcurr in jsondata:

                ctname = None
                try:
                    ctname = jcurr[u'catalogName']
                    ctname = ctname.encode('utf-8')
                    cataarr.append(ctname)
                except:
                    cataarr.append(ctname)
                filep = jcurr[u'filePath']
                filep = filep.encode('utf-8')
                filearr.append(filep)
                exidcurr = jcurr[u'testId']
                exidarr.append(exidcurr)
                typecurr = jcurr[u'type']
                typearr.append(typecurr)
                catalogIdcurr = jcurr[u'catalogId']
                knoidarr.append(catalogIdcurr)
                catordercurr = jcurr[u'catalogOrder']
                cataorderarrcurr.append(catordercurr)
                # 如果是目录，把内容放到临时目录集合中
                if type(catordercurr) is int:
                    acrcu = []
                    acrcu.append(catordercurr)
                    acrcu.append(catalogIdcurr)
                    cataidarrcurr.append(acrcu)

            for c in cataorderarrcurr:
                for a in cataidarrcurr:
                    b = c - a[0]
                    if b < 1 and b >= 0:
                        cataidarr.append(a[1])
                        break

                # 第一个cata，第二个file，第三个exid,第四个type，mulu然后上面的knoid
            depenarr.append(cataarr)
            depenarr.append(filearr)
            depenarr.append(exidarr)
            depenarr.append(typearr)
            depenarr.append(cataidarr)
            depenarr.append(knoidarr)
            return depenarr
        else:
            return None

    #拼接答案的
    def PGanswer(self,dependata,answerdata):
        if answerdata is None:
            return None

        answers=[]
        blankanswer=[]

        for ans in answerdata[1]:
            if ans[1] is 1:
                qid=str(ans[0])
                vcurr=[ans[2]]
                va={"qid":qid,"value":vcurr}
                answers.append(va)
            if ans[1] is 2:
                qid =str(ans[0])
                vcurr = [ans[2]]
                vcurr=ans[2].decode('utf-8').split(',')
                cvustr=[]
                for i in range(len(vcurr)):
                    cvustr.append(vcurr[i])
                    #cvustr = cvustr + vcurr[i] + ','
                va={"qid":qid,"value":cvustr}
                answers.append(va)
            if ans[1] is 3:
                qid =str(ans[0])
                vcurr = [ans[2]]
                va = {"qid": qid, "value": vcurr}
                answers.append(va)
            if ans[1] is 4:
                qid = str(ans[0])
                st = ans[2].decode('utf-8')
                vcurr = eval(st)
                va = {"qid": qid, "value": vcurr}
                blankanswer.append(va)
            if ans[1] is 5:
                qid =str(ans[0])
                st = ans[2].decode('utf-8')
                vcurr=eval(st)
                # vcurr = []
                # vcurr.append(st["0"])
                va = {"qid": qid, "value": vcurr}
                answers.append(va)

        values = {"courseId": str(dependata[0]), "type": str(dependata[1]), "exId": str(dependata[2]), "ccId": str(dependata[3]), "knoId": str(dependata[4]),"answers": str(answers),"blankAnswers":str(blankanswer),"total": str(len(answerdata[1])),
         "unanswered": '0',
         "examination": ""}
        j=json.dumps(values, ensure_ascii=False)
        #这里注意编码的方式一个重要的ensure_ascii
        #print(json.dumps(values))
        return j

    #处理外部调用的刷时间的方法
    def mMain(self,username,password,mframe):
        self.usernname = username
        self.password = password
        self.mframe = mframe

        # 模拟登录
        # 可能由于网络原因，会失败，尝试5次
        self.call2Framestatus('开始模拟登录')
        b = 0
        for i in range(5):
            b = self.login("http://hnust.hunbys.com/web/tologin#0",
                      "http://hnust.hunbys.com/verifycode/getverifycode.action", 'http://hnust.hunbys.com/web/login',
                      'E:\\Zhou\\zhou.txt',
                      self.usernname, self.password)
            if b is 1:
                break

        global mSession
        if b is 1:
            self.call2Framestatus('模拟登录成功,开始获取基础页面数据')
            print('模拟的登录成功')
        else:
            self.call2Framestatus('模拟的登录尝试失败，线程即将退出。。。')
            print('模拟的登录尝试失败，线程即将退出。。。')
            mSession.close()
            return

        #获取课程的页面url和课程的id
        b = 0
        pageurlAndcoursearr = []
        for i in range(5):
            pageurlAndcoursearr=self.getCourseidAndUrl()
            if pageurlAndcoursearr is not None :
                b=1
                break
        if b is 1:
            self.call2Framestatus('获取基础页面数据成功,开始获取课程数据')
            self.courseId=pageurlAndcoursearr[0]
            self.page2learnurl=pageurlAndcoursearr[1]
            print('获取基础页面数据成功'+str(self.courseId)+','+str(self.page2learnurl))
        else:
            self.call2Framestatus('获取基础页面数据尝试失败，线程即将退出。。。')
            print('获取基础页面数据尝试失败，线程即将退出。。。')
            mSession.close()
            return

        # 获取课程全部
        b = 0
        idarr = []
        for i in range(5):
            idarr = self.getAllCourse(
                self.page2learnurl)
            if len(idarr) is not 0:
                b = 1
                break
        if b is 1:
            self.call2Framestatus('获取课程数据成功,开始获取课程时长')
            print('获取课程数据成功')
        else:
            self.call2Framestatus('获取课程数据尝试失败，线程即将退出。。。')
            print('获取课程数据尝试失败，线程即将退出。。。')
            mSession.close()
            return

        # 获取全部课程时长
        b = 0
        videoarr = []
        for i in range(5):
            videoarr = self.getVideoLength('http://hnust.hunbys.com/web/students/getAjaxVideo', idarr)
            if len(videoarr) is not 0:
                b = 1
                break

        if b is 1:
            self.call2Framestatus('获取课程时长成功,进入最后一步')
            print('获取课程时长成功')
        else:
            self.call2Framestatus('获取课程时长尝试失败，线程即将退出。。。')
            print('获取课程时长尝试失败，线程即将退出。。。')
            mSession.close()
            return

        # 消耗时长并结束
        b = 0
        self.connsumeTimeAndFinish('http://hnust.hunbys.com/web/students/addVideoPercentage',
                              'http://hnust.hunbys.com/web/students/videoFinish', idarr, videoarr)

        # 下面是分开做的消耗时长并结束
        # consumeTime('http://hnust.hunbys.com/web/students/addVideoPercentage', idarr, videoarr)
        # finish('http://hnust.hunbys.com/web/students/videoFinish', idarr)
        # 关闭连接
        #global mSession
        mSession.close()

    def mHomeWork(self,username,password,mframe):
        self.usernname = username
        self.password = password
        self.mframe = mframe
        usernamecurr='1510040102'
        passwordcurr = 'abc123'

        # 模拟登录
        # 可能由于网络原因，会失败，尝试5次
        self.call2Framestatus2('开始尝试获取答案...')
        b = 0
        for i in range(5):
            b = self.login("http://hnust.hunbys.com/web/tologin#0",
                           "http://hnust.hunbys.com/verifycode/getverifycode.action",
                           'http://hnust.hunbys.com/web/login',
                           'E:\\Zhou\\zhou.txt',
                           usernamecurr, passwordcurr)
            if b is 1:
                break

        global mSession
        if b is 1:
            self.call2Framestatus2('开始尝试获取答案...模拟登录成功')
            print('模拟的登录成功')
        else:
            self.call2Framestatus2('获取答案失败')
            print('模拟的登录尝试失败，线程即将退出。。。')
            mSession.close()
            return

        # 获取课程的页面url和课程的id
        self.call2Framestatus2('开始尝试获取答案...尝试解析页面数据')
        b = 0
        pageurlAndcoursearr = []
        for i in range(5):
            pageurlAndcoursearr = self.getCourseidAndUrl()
            if pageurlAndcoursearr is not None:
                b = 1
                break
        if b is 1:
            self.call2Framestatus2('开始尝试获取答案...解析页面数据成功')
            self.courseId = pageurlAndcoursearr[0]
            self.page2learnurl = pageurlAndcoursearr[1]
            print('获取基础页面数据成功' + str(self.courseId) + ',' + str(self.page2learnurl))
        else:
            #self.call2Framestatus('获取基础页面数据尝试失败，线程即将退出。。。')
            self.call2Framestatus2('开始尝试获取答案...解析页面数据失败')
            mSession.close()
            return

        # 获取组装好的作业答案
        submitans=self.getreferansAndPG()
        #重新登录自己的
        # 模拟登录
        # 可能由于网络原因，会失败，尝试5次
        self.call2Framestatus2('开始重新模拟登录...')
        b = 0
        for i in range(5):
            b = self.login("http://hnust.hunbys.com/web/tologin#0",
                           "http://hnust.hunbys.com/verifycode/getverifycode.action",
                           'http://hnust.hunbys.com/web/login',
                           'E:\\Zhou\\zhou.txt',
                           self.usernname, self.password)
            if b is 1:
                break


        if b is 1:
            self.call2Framestatus2('开始重新模拟登录...成功,准备发送作业')
            print('模拟的登录成功')
        else:
            self.call2Framestatus2('开始重新模拟登录...失败，请清空重新尝试')
            print('模拟的登录尝试失败，线程即将退出。。。')
            mSession.close()
            return
        self.dohomework(submitans)
        print('处理完成')
        mSession.close()
    #这里给主状态
    def call2Framestatus(self,message):
        self.mframe.sendMessage2status(message=message)
    # 这里给细节状态
    def call2Framestatus_re(self,message):
        self.mframe.sendMessage2status_re(message=message)

    # 这里给刷题目主状态
    def call2Framestatus2(self, message):
        self.mframe.sendMessage2status2(message=message)

    # 这里给刷题目细节状态
    def call2Framestatus_re2(self, message):
        self.mframe.sendMessage2status_re2(message=message)

mf=tkFrame()









