# coding=UTF-8
'''拼接数据的
'''

def PGPostValues(account,password,code):
    #{'account': '1510040102', 'password': 'abc123', 'code': code, 'setCookie': 'false', }
    code=code.encode('utf-8')
    result={'account': account, 'password':password, 'code': code, 'setCookie': 'true'}
    return result

def PGPostValusesVideoLebgth(url,courseId,catId):
    catId = catId.encode('utf-8')
    #result={'courseId':courseId,'catId':catId}
    result=url+ '?courseId='+str(courseId)+ '&catId='+str(catId,"utf-8")
    return result


def PGPostValusesXH(url,runTime,courseId,catId):
    catId = catId.encode('utf-8')
    #result=url+ '?courseId='+str(courseId)+ '&catId='+catId+'&runTime='+str(runTime)+'&courseHasStartLearn=true'
    result = {'courseId':str(courseId),'catId':catId,'runTime':str(runTime),'courseHasStartLearn':'true'}
    #print(result)
    return result

def PGPostValusesFinish(url,catId):
    catId = catId.encode('utf-8')
    result = url +'/'+ str(catId,"utf-8")
    return result

