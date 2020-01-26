window.onload = function() {
    loadMDE();
    makePreviewPretty();
};

loadMDE = function(){
    try {
        let converter = Markdown.getSanitizingConverter();
        converter.hooks.chain("postConversion", function (text) {
            return text.replace(/<pre>/gi, "<pre class=prettyprint>");
        });
        Markdown.Extra.init(converter);
    
        let editor = new Markdown.Editor(converter);
        editor.hooks.chain("onPreviewRefresh", function () {
            prettyPrint();
        });
        editor.run();
    }
    catch(err) {
        if(err instanceof TypeError){
            // Caused if mde.js is only used for preview
            ; // So pass 
        }
        else{
            console.log('MDE Editor not Loaded: ' + err);
        }   
    } 
}

makePreviewPretty = function(){
    let preview_items = document.getElementsByClassName('make-pretty');
    for (var i = 0; i < preview_items.length; i++) {
        code_elems = preview_items[i].getElementsByTagName('pre');
        for (var i = 0; i < code_elems.length; i++) {
            code_elems[i].className = "prettyprint "+ code_elems[i].className;
        }
    }
    prettyPrint();
}