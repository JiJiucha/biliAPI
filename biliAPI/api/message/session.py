from biliAPI.tools.mRequests import mrequests
from biliAPI.tools.url import get_session_list_by_type,get_new_session_list,session_detail,get_session_limit_stat,get_session_push_setting,set_session_to_read,remove_session_on_list,set_session_on_top,get_session_dnd_stat,set_session_dnd_stat,set_session_push_setting,set_session_intercept_stat,set_intercept_to_read,remove_all_intercept
class session_type:
    user_or_sys=1#用户与系统
    unfollow=2#未关注人
    group=3#粉丝团
    all_session=4#所有
    dustbin=5#被拦截
    huahuo=6#花火商单
    all_sys=7#所有系统消息
    stranger=8#陌生人（与 “未关注人” 不同，不包含官方消息）
    follow_or_sys=9#关注的人与系统
    
#只有这个session_type与上面的类一样，下面都是 1指用户，2指粉丝团
'''session_type不为4,7时有用 1,2:按会话时间逆向排序 3:按已读时间逆向排序 其他:正常排序'''
def get_session_list(cookie,session_type=0,size=20,group_fold=0,unfollow_fold=0,sort_rule=0,begin_ts='',end_ts=''):
    return mrequests.get(get_session_list_by_type,cookie=cookie,params={'session_type':session_type,'size':size,'group_fold':group_fold,'unfollow_fold':unfollow_fold,'sort_rule':sort_rule,'begin_ts':begin_ts,'end_ts':end_ts})

def get_new_session(cookie,size=20,begin_ts=''):
    return mrequests.get(get_new_session_list,cookie=cookie,params={'size':size,'begin_ts':begin_ts})

def get_session_dnd(cookie,uid):
    return mrequests.get(get_session_dnd,cookie=cookie,params={'uid':uid,'type':1})

def get_session_detail(cookie,session_type,talker_id):
    return mrequests.get(get_session_detail,cookie=cookie,params={'session_type':session_type,'talker_id':talker_id})

def get_session_limit(cookie,uid='',group_id=''):
    return mrequests.get(get_session_limit_stat,cookie=cookie,params={'own_uid':cookie.get('DedeUserID'),'uids':uid,'group_ids':group_id})

def get_session_push(cookie,talker_uid):
    return mrequests.get(get_session_limit_stat,cookie=cookie,params={'talker_uid':talker_uid})

def set_session_read(cookie,session_type,talker_id,ack_seqno=''):
    return mrequests.post(set_session_to_read,cookie=cookie,data={'session_type':session_type,'talker_id':talker_id,'csrf_token':cookie.get('bili_jct'),'csrf':cookie.get('bili_jct')})
#从会话列表移除，不会删除历史记录
def remove_session(cookie,session_type,talker_id):
    return mrequests.post(remove_session_on_list,cookie=cookie,data={'session_type':session_type,'talker_id':talker_id,'ack_seqno':ack_seqno,'csrf_token':cookie.get('bili_jct'),'csrf':cookie.get('bili_jct')})

def set_session_top(cookie,session_type,talker_id,is_top):
    return mrequests.post(set_session_on_top,cookie=cookie,data={'session_type':session_type,'talker_id':talker_id,'op_type':(0 if is_top else 1),'csrf_token':cookie.get('bili_jct'),'csrf':cookie.get('bili_jct')})

def set_session_dnd(cookie,session_type,vid,dnd):
    uid=''
    group_id=''
    p={'setting':(1 if dnd else 0),'csrf_token':cookie.get('bili_jct'),'csrf':cookie.get('bili_jct')}
    if session_type==1:
        p['dnd_uid']=vid
    if session_type==2:
        p['dnd_group_id']=vid
    return mrequests.post(set_session_dnd_stat,cookie=cookie,data=p)

def set_session_push(cookie,talker_id,push):
    return mrequests.post(set_session_push_setting,cookie=cookie,data={'talker_id':talker_id,'setting':(0 if push else 1),'csrf_token':cookie.get('bili_jct'),'csrf':cookie.get('bili_jct')})

def set_session_intercept(cookie,talker_id,intercept):
    return mrequests.post(set_session_intercept_stat,cookie=cookie,data={'talker_id':talker_id,'status':(1 if intercept else 0),'csrf_token':cookie.get('bili_jct'),'csrf':cookie.get('bili_jct')})
    
def read_intercept_session(cookie):
    return mrequests.post(set_intercept_to_read,cookie=cookie,data={'csrf_token':cookie.get('bili_jct'),'csrf':cookie.get('bili_jct')})

def remove_intercept_session(cookie):
    return mrequests.post(remove_all_intercept,cookie=cookie,data={'csrf_token':cookie.get('bili_jct'),'csrf':cookie.get('bili_jct')})

    
