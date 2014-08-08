var links = []

var casper = require('casper').create({
    verbose: true,
    // logLevel: 'debug'
});
// require("utils").dump(casper.cli.args);
var url = casper.cli.args[0]

function getLinks() {
    var links = document.querySelectorAll(".news_lst_tab")
    return Array.prototype.map.call(links, function(e) {
        return e.href;
    });
}

function check(){
    casper.wait(500, function(){
        var more = this.visible('.p-more')
        // this.debugHTML('.p-more', true)
        if (more) {
            this.click('.p-more a');
            check()
        };
    })
}

casper.start();
casper.userAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X)');

casper.thenOpen(url, function() {
    // this.debugHTML('.p-more', true)
    this.click('.p-more a');
    check()
});


casper.wait(1000, function(){
    // this.capture('3.png');
    links = this.evaluate(getLinks)
})

casper.run(function(){
     this.echo(links.join('\n')).exit();
});
