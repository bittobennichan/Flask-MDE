var converter = Markdown.getSanitizingConverter();
converter.hooks.chain("postConversion", function (text) {
    return text.replace(/<pre>/gi, "<pre class=prettyprint>");
});


var editor = new Markdown.Editor(converter, "-5");

var editor = new Markdown.Editor(converter);
    editor.hooks.chain("onPreviewRefresh", function () {
    prettyPrint();
});

editor.run();