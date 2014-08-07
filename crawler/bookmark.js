// 搜狗微信页面，提取微信文章链接
javascript:(function(){var links = document.querySelectorAll(".news_lst_tab");var s='';for(var i=0;i<links.length;i++){s=s+'<br>'+links[i].href};var w = window.open('');w.document.write(s)})()

// 搜狗微信页面，自动点击“查看更多”
setInterval(function(){var more = document.querySelector(".p-more"); if (more.style.visibility!='hidden') {document.querySelector(".p-more").click()};}, 100)