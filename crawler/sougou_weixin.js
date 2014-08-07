var url = 'http://weixin.sogou.com/gzh?openid=oIWsFt86NKeSGd_BQKp1GcDkYpv0';
var links = []

var casper = require('casper').create({
    verbose: true,
    logLevel: 'debug'
});

function getLinks() {
    var links = document.querySelectorAll(".news_lst_tab")
    return Array.prototype.map.call(links, function(e) {
        return e.href;
    });
}

casper.start();
casper.userAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X)');

casper.thenOpen(url, function() {
    this.echo(this.getTitle());
    this.capture('1.png');

    var more = this.visible('.p-more');
    while(more){
        this.click('.p-more a');
        more = this.visible('.p-more');
    }
});

casper.wait(1000, function(){
    this.capture('3.png');
    links = this.evaluate(getLinks)
})

casper.run(function(){
     this.echo(' - ' + links.join('\n - ')).exit();
});
