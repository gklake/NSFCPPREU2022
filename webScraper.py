from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re
htmlDoc = '''<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><!-- start: forumdisplay --> <html xml:lang="en" lang="en" 
xmlns="http://www.w3.org/1999/xhtml"> <head> <title>CryptBB - Beginner Hacking </title> <!-- start: headerinclude --> 
<link rel="alternate" type="application/rss+xml" title="Latest Threads (RSS 2.0)" 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/syndication.php" /> <link rel="alternate" 
type="application/atom+xml" title="Latest Threads (Atom 1.0)" 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/syndication.php?type=atom1.0" /> <meta 
http-equiv="Content-Type" content="text/html; charset=UTF-8" /> <meta http-equiv="Content-Script-Type" 
content="text/javascript" /> <link type="text/css" rel="stylesheet" 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/cache/themes/theme6/global.min.css" /> 
<link type="text/css" rel="stylesheet" href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion
/cache/themes/theme6/css3.min.css" /> <link type="text/css" rel="stylesheet" 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/cache/themes/theme6/star_ratings.min.css" 
/> <link type="text/css" rel="stylesheet" href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion
/cache/themes/theme6/thread_status.min.css" /> <link type="text/css" rel="stylesheet" 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/cache/themes/theme1/alerts.min.css" /> 
<link type="text/css" rel="stylesheet" href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion
/css.php?stylesheet=37" /> <!-- end: headerinclude --> <!-- start: forumdisplay_rssdiscovery --> <link 
rel="alternate" type="application/rss+xml" title="Latest Threads in Beginner Hacking (RSS 2.0)" 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/syndication.php?fid=87" /> <link 
rel="alternate" type="application/atom+xml" title="Latest Threads in Beginner Hacking (Atom 1.0)" 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/syndication.php?type=atom1.0&amp;fid=87" 
/> <!-- end: forumdisplay_rssdiscovery --> <script type="text/javascript"> <!-- lang.no_new_posts = "Forum Contains 
No New Posts"; lang.click_mark_read = "Click to mark this forum as read"; lang.inline_edit_description = "(Click and 
hold to edit)"; lang.post_fetch_error = "There was an error fetching the posts."; // --> </script> <!-- jeditable (
jquery) --> <script type="text/javascript" src="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion
/jscripts/jeditable/jeditable.min.js"></script> <script type="text/javascript" 
src="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/jscripts/inline_edit.js?ver=1808"></script
> </head> <body> <!-- start: header --> <link rel="shortcut icon" type="image/ico" href="/images/favicon.ico"/> <div 
id="container"> <a name="top" id="top"></a> <div id="header"> <div id="logo"> <div class="wrapper"> <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/"><img style="padding-top:38.2px;" 
src="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/images/dark/logo_white.png" alt="CryptBB" 
title="CryptBB" /></a> <ul class="menu top_links"> <div style="display: inline-block; padding: 10px; color: 
white;background-color:#0066A2;border-top-left-radius: 3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="/">Home</a></div> <div style="display: inline-block; padding: 10px; color: 
white;background-color:#0066A2;border-top-left-radius: 3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="/search.php">Search</a></div> <div style="display: inline-block; padding: 10px; color: 
white;background-color:#0066A2;border-top-left-radius: 3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="/memberlist.php">Members</a></div> <div style="display: inline-block; padding: 10px; color: 
white;background-color:#0066A2;border-top-left-radius: 3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="/challenges.php">Challenges</a></div> <div style="display: inline-block; padding: 10px; 
color: white;background-color:#0066A2;border-top-left-radius: 3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="/mirrors.php">Mirrors</a></div> <div style="display: inline-block; padding: 10px; color: 
white;background-color:#0066A2;border-top-left-radius: 3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="http://darkindex5pin6jb.onion/" target="blank">DarkIndex</a></div> <div style="display: 
inline-block; padding: 10px; color: white;background-color:#0066A2;border-top-left-radius: 
3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="http://cryptbbsfmzv6dq4ec2iv6ravrw5ohgmklfagqhtvkgiaknvte5fylqd.onion/" 
target="_blank">XMPP</a></div> <div style="display: inline-block; padding: 10px; color: 
white;background-color:#0066A2;border-top-left-radius: 3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="http://cryptbbmgu4offops7nj676thvibogf2mokfv2vlmvnsrzdh5xtdvhqd.onion/" 
target="_blank">File Sharing</a></div> <div style="display: inline-block; padding: 10px; color: 
white;background-color:#0066A2;border-top-left-radius: 3px;border-top-right-radius: 3px;font-weight:bold;"><a 
style="color:white;"href="/showteam.php">Staff</a></div> </ul> </div> </div> <div id="panel"> <div class="upper"> 
<div class="wrapper"> <!-- start: header_quicksearch --> <form 
action="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/search.php"method="post"> <fieldset 
id="search"> <input name="keywords" type="text" style="font-size:14px;padding:1px;"class="textbox" /> <input 
value="Search" type="submit" style="padding:1px;"class="button" /> <input type="hidden" name="action" 
value="do_search" /> <input type="hidden" name="postthread" value="1" /> </fieldset> </form> <!-- end: 
header_quicksearch --> <!-- start: header_welcomeblock_member --> <!-- Continuation of div(class="upper") as opened 
in the header template --> <span class="welcome"><strong>Welcome back, 
<a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid
=44508">holyre</a></strong>. You last visited: <span title="07-05-2022">Today</span>, 04:16 PM &nbsp; <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=logout&amp;logoutkey
=3c0891f96726f940108d990e64830cf6"><i class="fa fa-sign-out" aria-hidden="true"></i> Log Out</a></span> </div> </div> 
<div class="lower"> <div class="wrapper"> <ul class="menu panel_links"> <!-- start: header_welcomeblock_member_user 
--> <li><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/usercp.php"><i class="fa 
fa-user" aria-hidden="true"></i> User CP</a></li> <!-- end: header_welcomeblock_member_user --> <!-- start: 
myalerts_headericon --> <li class="alerts "> <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/alerts.php" 
class="myalerts"><span>Alerts:</span> 0</a> </li> <!-- end: myalerts_headericon --> </ul> <ul class="menu 
user_links"> <li><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/misc.php?action
=buddypopup&modal=1">Open Buddy List</a></li> <!-- start: header_welcomeblock_member_search --> <li><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/search.php?action=getnew">View New 
Posts</a></li> <li><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/search.php?action
=getdaily">View Today's Posts</a></li> <!-- end: header_welcomeblock_member_search --> <!-- start: 
header_welcomeblock_member_pms --> <li><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion
/private.php">Private Messages</a> (Unread 0, Total 1)</li> <!-- end: header_welcomeblock_member_pms --> </ul> </div> 
<br class="clear" /> </div> <!-- end: header_welcomeblock_member --> <!-- </div> in header_welcomeblock_member and 
header_welcomeblock_guest --> <!-- </div> in header_welcomeblock_member and header_welcomeblock_guest --> </div> 
</div> <div id="content"> <div class="wrapper"> <!-- start: nav --> <div class="navigation"> <i class="fa fa-home" 
aria-hidden="true"></i> <!-- start: nav_bit --> <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/index.php">CryptBB</a><!-- start: nav_sep 
--> &rsaquo; <!-- end: nav_sep --> <!-- end: nav_bit --><!-- start: nav_bit --> <a 
href="forumdisplay.php?fid=85">Public</a> <!-- end: nav_bit --><!-- start: nav_sep_active --> &rsaquo; <!-- end: 
nav_sep_active --><!-- start: nav_bit_active --> <span class="active">Beginner Hacking</span> <!-- end: 
nav_bit_active --> </div> <!-- end: nav --> <br /> <!-- end: header --> <!-- start: forumdisplay_rules --> <br /> 
<table border="0" cellspacing="0" cellpadding="5" class="tborder tfixed"> <tr> <td 
class="thead"><strong>Rules</strong></td> </tr> <tr> <td class="trow1 scaleimages"><span class="smalltext">1. Read 
sticky before posting.</span></td> </tr> </table> <br /> <!-- end: forumdisplay_rules --> <!-- start: 
forumdisplay_threadlist --> <div class="float_left"> <!-- start: multipage --> <div class="pagination"> <span 
class="pages">Pages (35):</span> <!-- start: multipage_page_current --> <span class="pagination_current">1</span> 
<!-- end: multipage_page_current --><!-- start: multipage_page --> <a href="forumdisplay.php?fid=87&amp;page=2" 
class="pagination_page">2</a> <!-- end: multipage_page --><!-- start: multipage_page --> <a 
href="forumdisplay.php?fid=87&amp;page=3" class="pagination_page">3</a> <!-- end: multipage_page --><!-- start: 
multipage_page --> <a href="forumdisplay.php?fid=87&amp;page=4" class="pagination_page">4</a> <!-- end: 
multipage_page --><!-- start: multipage_page --> <a href="forumdisplay.php?fid=87&amp;page=5" 
class="pagination_page">5</a> <!-- end: multipage_page --><!-- start: multipage_end --> ... <a 
href="forumdisplay.php?fid=87&amp;page=35" class="pagination_last">35</a> <!-- end: multipage_end --><!-- start: 
multipage_nextpage --> <a href="forumdisplay.php?fid=87&amp;page=2" class="pagination_next">Next &raquo;</a> <!-- 
end: multipage_nextpage --> </div> <!-- end: multipage --> </div> <div class="float_right"> <!-- start: 
forumdisplay_newthread --> <a href="newthread.php?fid=87" class="button new_thread_button"><span>Post 
Thread</span></a> <!-- end: forumdisplay_newthread --> </div> <table border="0" cellspacing="0" cellpadding="5" 
class="tborder clear"> <tr> <td class="thead" colspan="6"> <div class="float_right"> <span 
class="smalltext"><strong></strong></span> </div> <div> <strong>Beginner Hacking</strong> </div> </td> </tr> <tr> <td 
class="tcat" colspan="3" width="66%"><span class="smalltext"><strong><a 
href="forumdisplay.php?fid=87&amp;datecut=9999&amp;prefix=0&amp;sortby=subject&amp;order=asc">Thread</a> / <a 
href="forumdisplay.php?fid=87&amp;datecut=9999&amp;prefix=0&amp;sortby=starter&amp;order=asc">Author</a> 
</strong></span></td> <td class="tcat" align="center" width="7%"><span class="smalltext"><strong><a 
href="forumdisplay.php?fid=87&amp;datecut=9999&amp;prefix=0&amp;sortby=replies&amp;order=desc">Replies</a> 
</strong></span></td> <td class="tcat" align="center" width="7%"><span class="smalltext"><strong><a 
href="forumdisplay.php?fid=87&amp;datecut=9999&amp;prefix=0&amp;sortby=views&amp;order=desc">Views</a> 
</strong></span></td> <td class="tcat" align="right" width="20%"><span class="smalltext"><strong><a 
href="forumdisplay.php?fid=87&amp;datecut=9999&amp;prefix=0&amp;sortby=lastpost&amp;order=desc">Last Post</a> <!-- 
start: forumdisplay_orderarrow --> <span class="smalltext">[<a 
href="forumdisplay.php?fid=87&amp;datecut=9999&amp;prefix=0&amp;sortby=lastpost&amp;order=asc">asc</a>]</span> <!-- 
end: forumdisplay_orderarrow --></strong></span></td> </tr> <!-- start: forumdisplay_sticky_sep --> <tr> <td 
class="trow_sep" colspan="6">Important Threads</td> </tr> <!-- end: forumdisplay_sticky_sep --><!-- start: 
forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow1 forumdisplay_sticky" width="2%"><span 
class="thread_status hotlockfolder" title="No new posts. Hot thread. Locked thread."><img 
src="/images/topic_hotlockfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow1 
forumdisplay_sticky" width="2%">&nbsp;</td> <td class="trow1 forumdisplay_sticky"> <div> <span style="width:100px;"> 
<span class=" subject_old" id="tid_1209"><a href="showthread.php?tid=1209">Beginner Hacking Rules &amp; 
Etiquette</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=2
"><span style="color: #ffd700;"><strong>Power</strong></span></a></div> </div> </td> <td align="center" class="trow1 
forumdisplay_sticky">0</td> <td align="center" class="trow1 forumdisplay_sticky">12,572</td> <td class="trow1 
forumdisplay_sticky" style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext">12-24-2019, 
03:29 PM<br /> <a href="showthread.php?tid=1209&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=2
"><span style="color: #ffd700;"><strong>Power</strong></span></a></span> </td> </tr> <!-- end: forumdisplay_thread 
--><!-- start: forumdisplay_threads_sep --> <tr> <td class="trow_sep" colspan="6">Normal Threads</td> </tr> <!-- end: 
forumdisplay_threads_sep --><!-- start: forumdisplay_thread --> <tr class="inline_row"> <td align="center" 
class="trow2 forumdisplay_regular" width="2%"><span class="thread_status newhotfolder" title="New posts. Hot 
thread."><img src="/images/topic_newhotfolder.png" height="20" width="20"></img></span></td> <td align="center" 
class="trow2 forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow2 forumdisplay_regular"> <div> <span 
style="width:100px;"> <!-- start: forumdisplay_thread_gotounread --> <a 
href="showthread.php?tid=8305&amp;action=newpost"><i class="fa fa-chevron-circle-right" aria-hidden="true" alt="Go to 
first unread post" title="Go to first unread post"></i></a> <!-- end: forumdisplay_thread_gotounread --><span class=" 
subject_new" id="tid_8305"><a href="showthread.php?tid=8305">About reverse shell coding</a></span></span> <div 
class="author smalltext"><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php
?action=profile&amp;uid=32033"><span style="color: #0066a2;">KIARA</span></a></div> </div> </td> <td align="center" 
class="trow2 forumdisplay_regular">3</td> <td align="center" class="trow2 forumdisplay_regular">1,894</td> <td 
class="trow2 forumdisplay_regular" style="white-space: nowrap; text-align: right;"> <span class="lastpost 
smalltext"><span title="07-05-2022">Today</span>, 03:16 AM<br /> <a 
href="showthread.php?tid=8305&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=32033
"><span style="color: #0066a2;">KIARA</span></a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: 
forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow1 forumdisplay_regular" 
width="2%"><span class="thread_status newhotfolder" title="New posts. Hot thread."><img 
src="/images/topic_newhotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow1 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow1 forumdisplay_regular"> <div> <span 
style="width:100px;"> <!-- start: forumdisplay_thread_gotounread --> <a 
href="showthread.php?tid=8272&amp;action=newpost"><i class="fa fa-chevron-circle-right" aria-hidden="true" alt="Go to 
first unread post" title="Go to first unread post"></i></a> <!-- end: forumdisplay_thread_gotounread --><span class=" 
subject_new" id="tid_8272"><a href="showthread.php?tid=8272">Kali linux on Windows</a></span><!-- start: 
forumdisplay_thread_multipage --> <span class="smalltext">(Pages: <!-- start: forumdisplay_thread_multipage_page --> 
<a href="showthread.php?tid=8272">1</a> <!-- end: forumdisplay_thread_multipage_page --><!-- start: 
forumdisplay_thread_multipage_page --> <a href="showthread.php?tid=8272&amp;page=2">2</a> <!-- end: 
forumdisplay_thread_multipage_page -->)</span> <!-- end: forumdisplay_thread_multipage --></span> <div class="author 
smalltext"><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile
&amp;uid=32572">D-dash</a></div> </div> </td> <td align="center" class="trow1 forumdisplay_regular">11</td> <td 
align="center" class="trow1 forumdisplay_regular">2,100</td> <td class="trow1 forumdisplay_regular" 
style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext"><span 
title="07-04-2022">Yesterday</span>, 09:03 PM<br /> <a href="showthread.php?tid=8272&amp;action=lastpost">Last 
Post</a>: <a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile
&amp;uid=45035">Pestilence</a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: forumdisplay_thread 
--> <tr class="inline_row"> <td align="center" class="trow2 forumdisplay_regular" width="2%"><span 
class="thread_status newhotfolder" title="New posts. Hot thread."><img src="/images/topic_newhotfolder.png" 
height="20" width="20"></img></span></td> <td align="center" class="trow2 forumdisplay_regular" 
width="2%">&nbsp;</td> <td class="trow2 forumdisplay_regular"> <div> <span style="width:100px;"> <!-- start: 
forumdisplay_thread_gotounread --> <a href="showthread.php?tid=8839&amp;action=newpost"><i class="fa 
fa-chevron-circle-right" aria-hidden="true" alt="Go to first unread post" title="Go to first unread post"></i></a> 
<!-- end: forumdisplay_thread_gotounread --><span class=" subject_new" id="tid_8839"><a 
href="showthread.php?tid=8839">Using neighbor wifi to increase anonimity</a></span></span> <div class="author 
smalltext"><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile
&amp;uid=43676">mrcroc403</a></div> </div> </td> <td align="center" class="trow2 forumdisplay_regular">6</td> <td 
align="center" class="trow2 forumdisplay_regular">930</td> <td class="trow2 forumdisplay_regular" style="white-space: 
nowrap; text-align: right;"> <span class="lastpost smalltext">07-01-2022, 08:49 AM<br /> <a 
href="showthread.php?tid=8839&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=141
"><span style="color: #0066a2;">yany3</span></a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: 
forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow1 forumdisplay_regular" 
width="2%"><span class="thread_status newfolder" title="New posts."><img src="/images/topic_newfolder.png" 
height="20" width="20"></img></span></td> <td align="center" class="trow1 forumdisplay_regular" 
width="2%">&nbsp;</td> <td class="trow1 forumdisplay_regular"> <div> <span style="width:100px;"> <!-- start: 
forumdisplay_thread_gotounread --> <a href="showthread.php?tid=9126&amp;action=newpost"><i class="fa 
fa-chevron-circle-right" aria-hidden="true" alt="Go to first unread post" title="Go to first unread post"></i></a> 
<!-- end: forumdisplay_thread_gotounread --><span class=" subject_new" id="tid_9126"><a 
href="showthread.php?tid=9126">learning to hack</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=45243
">magacrypt</a></div> </div> </td> <td align="center" class="trow1 forumdisplay_regular">1</td> <td align="center" 
class="trow1 forumdisplay_regular">96</td> <td class="trow1 forumdisplay_regular" style="white-space: nowrap; 
text-align: right;"> <span class="lastpost smalltext">07-01-2022, 02:36 AM<br /> <a 
href="showthread.php?tid=9126&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=11927
"><span style="color: #ffd700;"><strong>Cyberjagu</strong></span></a></span> </td> </tr> <!-- end: 
forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow2 
forumdisplay_regular" width="2%"><span class="thread_status newhotfolder" title="New posts. Hot thread."><img 
src="/images/topic_newhotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow2 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow2 forumdisplay_regular"> <div> <span 
style="width:100px;"> <!-- start: forumdisplay_thread_gotounread --> <a 
href="showthread.php?tid=9039&amp;action=newpost"><i class="fa fa-chevron-circle-right" aria-hidden="true" alt="Go to 
first unread post" title="Go to first unread post"></i></a> <!-- end: forumdisplay_thread_gotounread --><span class=" 
subject_new" id="tid_9039"><a href="showthread.php?tid=9039">Best way to deliver a payload on android phones 
?</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=44097
">bubbleTea</a></div> </div> </td> <td align="center" class="trow2 forumdisplay_regular">9</td> <td align="center" 
class="trow2 forumdisplay_regular">454</td> <td class="trow2 forumdisplay_regular" style="white-space: nowrap; 
text-align: right;"> <span class="lastpost smalltext">06-30-2022, 10:10 AM<br /> <a 
href="showthread.php?tid=9039&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=141
"><span style="color: #0066a2;">yany3</span></a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: 
forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow1 forumdisplay_regular" 
width="2%"><span class="thread_status newhotfolder" title="New posts. Hot thread."><img 
src="/images/topic_newhotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow1 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow1 forumdisplay_regular"> <div> <span 
style="width:100px;">Poll: <!-- start: forumdisplay_thread_gotounread --> <a 
href="showthread.php?tid=8969&amp;action=newpost"><i class="fa fa-chevron-circle-right" aria-hidden="true" alt="Go to 
first unread post" title="Go to first unread post"></i></a> <!-- end: forumdisplay_thread_gotounread --><span class=" 
subject_new" id="tid_8969"><a href="showthread.php?tid=8969">nfc hacking device</a></span></span> <div class="author 
smalltext"><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile
&amp;uid=44401">riri</a></div> </div> </td> <td align="center" class="trow1 forumdisplay_regular">2</td> <td 
align="center" class="trow1 forumdisplay_regular">497</td> <td class="trow1 forumdisplay_regular" style="white-space: 
nowrap; text-align: right;"> <span class="lastpost smalltext">06-30-2022, 06:52 AM<br /> <a 
href="showthread.php?tid=8969&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=45200
">NULLv0id</a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr 
class="inline_row"> <td align="center" class="trow2 forumdisplay_regular" width="2%"><span class="thread_status 
newhotfolder" title="New posts. Hot thread."><img src="/images/topic_newhotfolder.png" height="20" 
width="20"></img></span></td> <td align="center" class="trow2 forumdisplay_regular" width="2%">&nbsp;</td> <td 
class="trow2 forumdisplay_regular"> <div> <span style="width:100px;"> <!-- start: forumdisplay_thread_gotounread --> 
<a href="showthread.php?tid=8896&amp;action=newpost"><i class="fa fa-chevron-circle-right" aria-hidden="true" alt="Go 
to first unread post" title="Go to first unread post"></i></a> <!-- end: forumdisplay_thread_gotounread --><span 
class=" subject_new" id="tid_8896"><a href="showthread.php?tid=8896">Cracking Access Points</a></span></span> <div 
class="author smalltext"><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php
?action=profile&amp;uid=39056">kalistamp</a></div> </div> </td> <td align="center" class="trow2 
forumdisplay_regular">2</td> <td align="center" class="trow2 forumdisplay_regular">739</td> <td class="trow2 
forumdisplay_regular" style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext">06-30-2022, 
06:46 AM<br /> <a href="showthread.php?tid=8896&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=45200
">NULLv0id</a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr 
class="inline_row"> <td align="center" class="trow1 forumdisplay_regular" width="2%"><span class="thread_status 
newhotfolder" title="New posts. Hot thread."><img src="/images/topic_newhotfolder.png" height="20" 
width="20"></img></span></td> <td align="center" class="trow1 forumdisplay_regular" width="2%">&nbsp;</td> <td 
class="trow1 forumdisplay_regular"> <div> <span style="width:100px;"> <!-- start: forumdisplay_thread_gotounread --> 
<a href="showthread.php?tid=9007&amp;action=newpost"><i class="fa fa-chevron-circle-right" aria-hidden="true" alt="Go 
to first unread post" title="Go to first unread post"></i></a> <!-- end: forumdisplay_thread_gotounread --><span 
class=" subject_new" id="tid_9007"><a href="showthread.php?tid=9007">IoT is our golden ticket. How do we make the 
most of it?</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=41573
"><span style="color: #0066a2;">Pronoxys</span></a></div> </div> </td> <td align="center" class="trow1 
forumdisplay_regular">7</td> <td align="center" class="trow1 forumdisplay_regular">492</td> <td class="trow1 
forumdisplay_regular" style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext">06-29-2022, 
07:02 PM<br /> <a href="showthread.php?tid=9007&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=41573
"><span style="color: #0066a2;">Pronoxys</span></a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: 
forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow2 forumdisplay_regular" 
width="2%"><span class="thread_status hotfolder" title="No new posts. Hot thread."><img 
src="/images/topic_hotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow2 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow2 forumdisplay_regular"> <div> <span 
style="width:100px;"> <span class=" subject_old" id="tid_9085"><a href="showthread.php?tid=9085">BlackArch in a VM on 
a **LOCAL** server? What could go wrong with this?</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=41573
"><span style="color: #0066a2;">Pronoxys</span></a></div> </div> </td> <td align="center" class="trow2 
forumdisplay_regular">0</td> <td align="center" class="trow2 forumdisplay_regular">154</td> <td class="trow2 
forumdisplay_regular" style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext">06-26-2022, 
03:48 PM<br /> <a href="showthread.php?tid=9085&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=41573
"><span style="color: #0066a2;">Pronoxys</span></a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: 
forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow1 forumdisplay_regular" 
width="2%"><span class="thread_status hotfolder" title="No new posts. Hot thread."><img 
src="/images/topic_hotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow1 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow1 forumdisplay_regular"> <div> <span 
style="width:100px;"> <span class=" subject_old" id="tid_9084"><a href="showthread.php?tid=9084">How to spoof an IP 
address</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=27240
"><span style="color: #0066a2;">ss11ss</span></a></div> </div> </td> <td align="center" class="trow1 
forumdisplay_regular">1</td> <td align="center" class="trow1 forumdisplay_regular">263</td> <td class="trow1 
forumdisplay_regular" style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext">06-25-2022, 
07:03 PM<br /> <a href="showthread.php?tid=9084&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=3
"><span style="color: #ffd700;"><strong>LongPig</strong></span></a></span> </td> </tr> <!-- end: forumdisplay_thread 
--><!-- start: forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow2 forumdisplay_regular" 
width="2%"><span class="thread_status hotfolder" title="No new posts. Hot thread."><img 
src="/images/topic_hotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow2 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow2 forumdisplay_regular"> <div> <span 
style="width:100px;"> <span class=" subject_old" id="tid_8841"><a href="showthread.php?tid=8841">How obsolete are 
MITM attacks?</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=43860
">rcerodant</a></div> </div> </td> <td align="center" class="trow2 forumdisplay_regular">3</td> <td align="center" 
class="trow2 forumdisplay_regular">883</td> <td class="trow2 forumdisplay_regular" style="white-space: nowrap; 
text-align: right;"> <span class="lastpost smalltext">06-23-2022, 02:13 PM<br /> <a 
href="showthread.php?tid=8841&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=7441
"><span style="color: #ffa500;"><strong>Century Child</strong></span></a></span> </td> </tr> <!-- end: 
forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow1 
forumdisplay_regular" width="2%"><span class="thread_status hotfolder" title="No new posts. Hot thread."><img 
src="/images/topic_hotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow1 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow1 forumdisplay_regular"> <div> <span 
style="width:100px;"> <span class=" subject_old" id="tid_9061"><a href="showthread.php?tid=9061">Looking for 2 
separate things, a tool/method &amp; combo-list for a certain site</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=44839
">SadBowlOfCereal</a></div> </div> </td> <td align="center" class="trow1 forumdisplay_regular">0</td> <td 
align="center" class="trow1 forumdisplay_regular">196</td> <td class="trow1 forumdisplay_regular" style="white-space: 
nowrap; text-align: right;"> <span class="lastpost smalltext">06-22-2022, 04:45 PM<br /> <a 
href="showthread.php?tid=9061&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=44839
">SadBowlOfCereal</a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr 
class="inline_row"> <td align="center" class="trow2 forumdisplay_regular" width="2%"><span class="thread_status 
hotfolder" title="No new posts. Hot thread."><img src="/images/topic_hotfolder.png" height="20" 
width="20"></img></span></td> <td align="center" class="trow2 forumdisplay_regular" width="2%">&nbsp;</td> <td 
class="trow2 forumdisplay_regular"> <div> <span style="width:100px;"> <span class=" subject_old" id="tid_8892"><a 
href="showthread.php?tid=8892">Unlocking an Apple Watch</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=44144
">netzyx</a></div> </div> </td> <td align="center" class="trow2 forumdisplay_regular">6</td> <td align="center" 
class="trow2 forumdisplay_regular">578</td> <td class="trow2 forumdisplay_regular" style="white-space: nowrap; 
text-align: right;"> <span class="lastpost smalltext">06-20-2022, 06:13 PM<br /> <a 
href="showthread.php?tid=8892&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=44097
">bubbleTea</a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr 
class="inline_row"> <td align="center" class="trow1 forumdisplay_regular" width="2%"><span class="thread_status 
hotfolder" title="No new posts. Hot thread."><img src="/images/topic_hotfolder.png" height="20" 
width="20"></img></span></td> <td align="center" class="trow1 forumdisplay_regular" width="2%">&nbsp;</td> <td 
class="trow1 forumdisplay_regular"> <div> <span style="width:100px;"> <span class=" subject_old" id="tid_8914"><a 
href="showthread.php?tid=8914">hash cracking</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=43967
">snotRocket</a></div> </div> </td> <td align="center" class="trow1 forumdisplay_regular">2</td> <td align="center" 
class="trow1 forumdisplay_regular">680</td> <td class="trow1 forumdisplay_regular" style="white-space: nowrap; 
text-align: right;"> <span class="lastpost smalltext">06-20-2022, 02:09 PM<br /> <a 
href="showthread.php?tid=8914&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=44097
">bubbleTea</a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr 
class="inline_row"> <td align="center" class="trow2 forumdisplay_regular" width="2%"><span class="thread_status 
hotfolder" title="No new posts. Hot thread."><img src="/images/topic_hotfolder.png" height="20" 
width="20"></img></span></td> <td align="center" class="trow2 forumdisplay_regular" width="2%">&nbsp;</td> <td 
class="trow2 forumdisplay_regular"> <div> <span style="width:100px;"> <span class=" subject_old" id="tid_9006"><a 
href="showthread.php?tid=9006">How to get windows sandbox in 10 home</a></span></span> <div class="author 
smalltext"><a href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile
&amp;uid=27240"><span style="color: #0066a2;">ss11ss</span></a></div> </div> </td> <td align="center" class="trow2 
forumdisplay_regular">2</td> <td align="center" class="trow2 forumdisplay_regular">423</td> <td class="trow2 
forumdisplay_regular" style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext">06-20-2022, 
08:34 AM<br /> <a href="showthread.php?tid=9006&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=27240
"><span style="color: #0066a2;">ss11ss</span></a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: 
forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow1 forumdisplay_regular" 
width="2%"><span class="thread_status hotfolder" title="No new posts. Hot thread."><img 
src="/images/topic_hotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow1 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow1 forumdisplay_regular"> <div> <span 
style="width:100px;"> <span class=" subject_old" id="tid_8990"><a href="showthread.php?tid=8990">How well will this 
work and what to use?</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=43821
">SugeKnight</a></div> </div> </td> <td align="center" class="trow1 forumdisplay_regular">4</td> <td align="center" 
class="trow1 forumdisplay_regular">496</td> <td class="trow1 forumdisplay_regular" style="white-space: nowrap; 
text-align: right;"> <span class="lastpost smalltext">06-16-2022, 10:01 PM<br /> <a 
href="showthread.php?tid=8990&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=43821
">SugeKnight</a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr 
class="inline_row"> <td align="center" class="trow2 forumdisplay_regular" width="2%"><span class="thread_status 
hotfolder" title="No new posts. Hot thread."><img src="/images/topic_hotfolder.png" height="20" 
width="20"></img></span></td> <td align="center" class="trow2 forumdisplay_regular" width="2%">&nbsp;</td> <td 
class="trow2 forumdisplay_regular"> <div> <span style="width:100px;"> <span class=" subject_old" id="tid_7275"><a 
href="showthread.php?tid=7275">Ukraine Support</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=24700
"><span style="color: #0066a2;">Cryptery</span></a></div> </div> </td> <td align="center" class="trow2 
forumdisplay_regular">8</td> <td align="center" class="trow2 forumdisplay_regular">2,694</td> <td class="trow2 
forumdisplay_regular" style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext">06-14-2022, 
06:03 PM<br /> <a href="showthread.php?tid=7275&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=43731
">Obzek</a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- start: forumdisplay_thread --> <tr 
class="inline_row"> <td align="center" class="trow1 forumdisplay_regular" width="2%"><span class="thread_status 
hotfolder" title="No new posts. Hot thread."><img src="/images/topic_hotfolder.png" height="20" 
width="20"></img></span></td> <td align="center" class="trow1 forumdisplay_regular" width="2%">&nbsp;</td> <td 
class="trow1 forumdisplay_regular"> <div> <span style="width:100px;"> <span class=" subject_old" id="tid_8847"><a 
href="showthread.php?tid=8847">How to test files safely</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=27240
"><span style="color: #0066a2;">ss11ss</span></a></div> </div> </td> <td align="center" class="trow1 
forumdisplay_regular">4</td> <td align="center" class="trow1 forumdisplay_regular">844</td> <td class="trow1 
forumdisplay_regular" style="white-space: nowrap; text-align: right;"> <span class="lastpost smalltext">06-14-2022, 
07:35 AM<br /> <a href="showthread.php?tid=8847&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=14465
"><span style="color: #0066a2;">Xprogrammer</span></a></span> </td> </tr> <!-- end: forumdisplay_thread --><!-- 
start: forumdisplay_thread --> <tr class="inline_row"> <td align="center" class="trow2 forumdisplay_regular" 
width="2%"><span class="thread_status hotfolder" title="No new posts. Hot thread."><img 
src="/images/topic_hotfolder.png" height="20" width="20"></img></span></td> <td align="center" class="trow2 
forumdisplay_regular" width="2%">&nbsp;</td> <td class="trow2 forumdisplay_regular"> <div> <span 
style="width:100px;"> <span class=" subject_old" id="tid_8952"><a href="showthread.php?tid=8952">Money making ways 
for beginner</a></span></span> <div class="author smalltext"><a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=24570
">vcs0707</a></div> </div> </td> <td align="center" class="trow2 forumdisplay_regular">1</td> <td align="center" 
class="trow2 forumdisplay_regular">453</td> <td class="trow2 forumdisplay_regular" style="white-space: nowrap; 
text-align: right;"> <span class="lastpost smalltext">06-12-2022, 05:49 PM<br /> <a 
href="showthread.php?tid=8952&amp;action=lastpost">Last Post</a>: <a 
href="http://cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid.onion/member.php?action=profile&amp;uid=28501
">duracelltheta</a></span> </td> </tr> <!-- end: forumdisplay_thread --> <tr> <td class="tfoot" align="right" 
colspan="6"> <form action="forumdisplay.php" method="get"> <input type="hidden" name="fid" value="87" /> <select 
name="sortby"> <option value="subject">Sort by: Subject</option> <option value="lastpost" selected="selected">Sort 
by: Last Post</option> <option value="starter">Sort by: Author</option> <option value="started">Sort by: Creation 
Time</option> <option value="replies">Sort by: Replies</option> <option value="views">Sort by: Views</option> 
</select> <select name="order"> <option value="asc">Order: Ascending</option> <option value="desc" 
selected="selected">Order: Descending</option> </select> <select name="datecut"> <option value="1">From: 
Today</option> <option value="5">From: 5 Days Ago</option> <option value="10">From: 10 Days Ago</option> <option 
value="20">From: 20 Days Ago</option> <option value="50">From: 50 Days Ago</option> <option value="75">From: 75 Days 
Ago</option> <option value="100">From: 100 Days Ago</option> <option value="365">From: The Last Year</option> <option 
value="9999" selected="selected">From: The Beginning</option> </select> <!-- start: forumdisplay_threadlist_prefixes 
--> <select name="prefix"> <option value="-2">Prefix: Any Prefix</option> <option value="-1">Prefix: No 
Prefix</option> <option value="0" selected="selected">Prefix: Any/No Prefix</option> <!-- start: 
forumdisplay_threadlist_prefixes_prefix --> <option value="8">Prefix: [Official]</option> <!-- end: 
forumdisplay_threadlist_prefixes_prefix --> </select> <!-- end: forumdisplay_threadlist_prefixes --> <!-- start: 
gobutton --> <input type="submit" class="button" value="Go" /> <!-- end: gobutton --> </form> </td> </tr> </table> 
<div class="float_left"> <!-- start: multipage --> <div class="pagination"> <span class="pages">Pages (35):</span> 
<!-- start: multipage_page_current --> <span class="pagination_current">1</span> <!-- end: multipage_page_current 
--><!-- start: multipage_page --> <a href="forumdisplay.php?fid=87&amp;page=2" class="pagination_page">2</a> <!-- 
end: multipage_page --><!-- start: multipage_page --> <a href="forumdisplay.php?fid=87&amp;page=3" 
class="pagination_page">3</a> <!-- end: multipage_page --><!-- start: multipage_page --> <a 
href="forumdisplay.php?fid=87&amp;page=4" class="pagination_page">4</a> <!-- end: multipage_page --><!-- start: 
multipage_page --> <a href="forumdisplay.php?fid=87&amp;page=5" class="pagination_page">5</a> <!-- end: 
multipage_page --><!-- start: multipage_end --> ... <a href="forumdisplay.php?fid=87&amp;page=35" 
class="pagination_last">35</a> <!-- end: multipage_end --><!-- start: multipage_nextpage --> <a 
href="forumdisplay.php?fid=87&amp;page=2" class="pagination_next">Next &raquo;</a> <!-- end: multipage_nextpage --> 
</div> <!-- end: multipage --> </div> <div class="float_right" style="margin-top: 4px;"> </div> <br class="clear" /> 
<br /> <div class="float_left"> <br class="clear" /> </div> <div class="float_right" style="text-align: right;"> 
</div> <br class="clear" /> <!-- end: forumdisplay_threadlist --> <!-- start: footer -->  </div> </div> <div 
id="footer"> </div> <!-- end: footer --> </body> </html> <!-- end: forumdisplay --> '''
# html = urlopen('')

soup = BeautifulSoup(htmlDoc, 'html.parser')
# print(soup.prettify())

url = input("Enter the URL: ")

pageText = soup.text
cleanPageText = re.sub(r'[^a-zA-Z]', ' ', pageText)
words = cleanPageText.split()
unique_words = set(words)
print(unique_words)