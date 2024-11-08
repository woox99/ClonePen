// Text Editors
var htmlEditor = CodeMirror.fromTextArea(document.getElementById("html-editor"), {
    lineNumbers: true,
    mode: "htmlmixed", 
    htmlMode: true,
    theme: 'mbo',
    // onChange: updatePreview, // Use CodeMirror's onChange event
});

var cssEditor = CodeMirror.fromTextArea(document.getElementById("css-editor"), {
    lineNumbers: true,
    mode: "css", 
    theme: 'mbo',
});

var jsEditor = CodeMirror.fromTextArea(document.getElementById("js-editor"), {
    lineNumbers: true,
    mode: "javascript",
    theme: 'mbo',
});

// Adjust editor height
// var newHeight = "400px";
// htmlEditor.setSize(null, newHeight);
// cssEditor.setSize(null, newHeight);
// jsEditor.setSize(null, newHeight);

// Attach onChange event to js editors
htmlEditor.on("change", updatePreview);
cssEditor.on("change", updatePreview);
jsEditor.on("change", updatePreview);

const iframe = document.getElementById('iframe');

function updatePreview() {
    const htmlCode = htmlEditor.getValue();
    const cssCode = cssEditor.getValue();
    const jsCode = jsEditor.getValue();
    
    // Clear existing content
    iframe.innerHTML = "";
    
    // Write HTML and CSS to the iframe document
    var doc = iframe.contentDocument || iframe.contentWindow.document;
    doc.open();
    doc.write(htmlCode);
    doc.write(`<style>${cssCode} </style>`)
    doc.write("<script>" + jsCode + "</script>");
    doc.close();
    // console.log(doc)

    return null;
}