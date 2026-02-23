from biliAPI.api.login import cookie_refresh

def refresh(cookie):
    is_need_refresh_resp=cookie_refresh.is_need_refresh(cookie)
    
    is_need_refresh_resp.raise_for_status()
    
    inr=is_need_refresh_resp.json()
    
    if inr['code']==0:
        need_refresh=inr['data']['refresh']
        if need_refresh:
            
        else:
            return False