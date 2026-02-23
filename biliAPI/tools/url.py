# Copyright (c) 2025 JiJiucha
# Licensed under the MIT License (see LICENSE file for details)

# login
# login qr web
generate_web_url='https://passport.bilibili.com/x/passport-login/web/qrcode/generate'
poll_web_url='https://passport.bilibili.com/x/passport-login/web/qrcode/poll'

# login info
get_nav_info_url='https://api.bilibili.com/x/web-interface/nav'


# logout
logout_url='https://passport.bilibili.com/login/exit/v2'

# refresh cookie
is_need_refresh_url='https://passport.bilibili.com/x/passport-login/web/cookie/info'
get_refresh_csrf_url='https://www.bilibili.com/correspond/1/'
refresh_cookie_irl='https://passport.bilibili.com/x/passport-login/web/cookie/refresh'
confirm_refresh_url='https://passport.bilibili.com/x/passport-login/web/confirm/refresh'
#buvid
get_buvid3_url='https://api.bilibili.com/x/web-frontend/getbuvid'
get_buvid_url='https://api.bilibili.com/x/frontend/finger/spi'

# safety
bili_ticket_get='https://api.bilibili.com/bapis/bilibili.api.ticket.v1.Ticket/GenWebTicket'
my_base_info='https://api.bilibili.com/x/member/web/account'
day_reward='https://api.bilibili.com/x/member/web/exp/reward'
day_coin_reward='https://api.bilibili.com/x/web-interface/coin/today/exp'
my_account_info='https://passport.bilibili.com/web/site/user/info'
is_realname='https://api.bilibili.com/x/member/realname/status'
realname_info='https://api.bilibili.com/x/member/realname/apply/status'

coin_log='https://api.bilibili.com/x/member/web/coin/log'
exp_log='https://api.bilibili.com/x/member/web/exp/log'
moral_log='https://api.bilibili.com/x/member/web/moral/log'


# my_info
vip_info='https://api.bilibili.com/x/vip/web/user/info'
my_info='https://api.bilibili.com/x/space/myinfo'

update_sign='https://api.bilibili.com/x/member/web/sign/update'

stat_of_login_user='https://api.bilibili.com/x/web-interface/nav/stat'
get_coin_count='https://account.bilibili.com/site/getCoin'

# message
# private message
get_unread_count_private_url='https://api.vc.bilibili.com/session_svr/v1/session_svr/single_unread'
get_unread_count_group_url='https://api.vc.bilibili.com/session_svr/v1/session_svr/my_group_unread'

get_session_list_by_type='https://api.vc.bilibili.com/session_svr/v1/session_svr/get_sessions'
get_new_session_list='https://api.vc.bilibili.com/session_svr/v1/session_svr/new_sessions'
get_session_push_setting='https://api.vc.bilibili.com/link_setting/v1/link_setting/get_session_ss'

set_session_to_read='https://api.vc.bilibili.com/session_svr/v1/session_svr/update_ack'

remove_session_on_list='https://api.vc.bilibili.com/session_svr/v1/session_svr/remove_session'
set_session_on_top='https://api.vc.bilibili.com/session_svr/v1/session_svr/set_top'


session_detail='https://api.vc.bilibili.com/session_svr/v1/session_svr/session_detail'
get_session_limit_stat='https://api.vc.bilibili.com/link_setting/v1/link_setting/is_limit'
get_session_dnd_stat='https://api.vc.bilibili.com/link_setting/v1/link_setting/get_msg_dnd'
set_session_dnd_stat='https://api.vc.bilibili.com/link_setting/v1/link_setting/set_msg_dnd'
set_session_push_setting='https://api.vc.bilibili.com/link_setting/v1/link_setting/set_push_ss'

set_session_intercept_stat='https://api.vc.bilibili.com/session_svr/v1/session_svr/update_intercept'
set_intercept_to_read='https://api.vc.bilibili.com/session_svr/v1/session_svr/batch_update_dustbin_ack'
remove_all_intercept='https://api.vc.bilibili.com/session_svr/v1/session_svr/batch_rm_dustbin'

get_session_msgs_url='https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs'
send_message_url='https://api.vc.bilibili.com/web_im/v1/web_im/send_msg'

# notice message
get_notice_unread='https://api.vc.bilibili.com/x/im/web/msgfeed/unread'
get_replies_url='https://api.bilibili.com/x/msgfeed/reply'

# user
# info
# card
get_user_card='https://api.bilibili.com/x/web-interface/card'
get_user_cards='https://api.bilibili.com/x/polymer/pc-electron/v1/user/cards'
# info
get_user_info='https://api.bilibili.com/x/space/wbi/acc/info'



# video
# view
get_video_view='https://api.bilibili.com/x/web-interface/view'
# detail
get_video_detail='https://api.bilibili.com/x/web-interface/view/detail'
# desc
get_video_desc='https://api.bilibili.com/x/web-interface/archive/desc'
# pagelist
get_video_pagelist='https://api.bilibili.com/x/player/pagelist'
#like
like_video_url='https://api.bilibili.com/x/web-interface/archive/like'

# search
search_all='https://api.bilibili.com/x/web-interface/wbi/search/all/v2'
search_type='https://api.bilibili.com/x/web-interface/wbi/search/type'

# 关系
followings_list='https://api.bilibili.com/x/relation/followings'
followings_list2='https://app.biliapi.net/x/v2/relation/followings'

search_following_list='https://api.bilibili.com/x/relation/followings/search'

followers_unread_count='https://api.bilibili.com/x/relation/followers/unread/count'

followers_list='https://api.bilibili.com/x/relation/fans'
followers_list2='https://app.biliapi.net/x/v2/relation/followers'


modify_relation='https://api.bilibili.com/x/relation/modify'
same_followings_list='https://api.bilibili.com/x/relation/same/followings'

dynamic_get_all_url='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all'
dynamic_get_update_url='https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all/update'

upload_dynamic_url='https://api.bilibili.com/x/dynamic/feed/draw/upload_bfs'