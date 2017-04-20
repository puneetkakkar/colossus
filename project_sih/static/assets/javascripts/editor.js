$(document).ready(function() {
    document.getElementById('textEditor').contentWindow.document.designMode = "on";
    var editWindow = document.getElementById("textEditor").contentWindow;
    editWindow.focus();
    $("#bold").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        bold_text();
    });
    $("#italic").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        italic_text();
    });
    $("#underline").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        underline_text();
    });
    $("#strikethrough").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        strikeThrough_text();
    });
    $("#orderedlist").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        orderedList();
    });
    $("#unorderedlist").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        unorderedList();
    });
    $("#indentText").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        indent_text();
    });
    $("#outdentText").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        outdent_text();
    });
    $("#fonts").on('change', function() {
        changeFont($("#fonts").val());
    });
    $("#fontSize").on('change', function() {
        increase_fontsize($("#fontSize").val());
    });
    $("#center_align").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        centerAlign();
    });
    $("#left_align").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        leftAlign();
    });
    $("#right_align").click(function() {
        if ($(this).hasClass("selected")) {
            $(this).removeClass("selected");
        } else {
            $(this).addClass("selected");
        }
        rightAlign();
    });
});

function bold_text() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("bold", false, "");
    edit.focus();
}

function italic_text() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("italic", false, "");
    edit.focus();
}

function underline_text() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("underline", false, "");
    edit.focus();
}

function strikeThrough_text() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("strikethrough", false, "");
    edit.focus();
}


function changeFont(font) {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("fontName", false, font);
    edit.focus();
}

function increase_fontsize(font_size) {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("fontSize", false, font_size);
    var fontElements = edit.document.getElementsByTagName("font");
    var len = fontElements.length;
    for (var i = 0; i <= len; ++i) {
        if (fontElements[i].size == "1") {
            fontElements[i].removeAttribute("size");
            fontElements[i].style.fontSize = "12px";
        } else if (fontElements[i].size == "2") {
            fontElements[i].removeAttribute("size");
            fontElements[i].style.fontSize = "18px";
        } else if (fontElements[i].size == "3") {
            fontElements[i].removeAttribute("size");
            fontElements[i].style.fontSize = "24px";
        } else if (fontElements[i].size == "4") {
            fontElements[i].removeAttribute("size");
            fontElements[i].style.fontSize = "30px";
        } else if (fontElements[i].size == "5") {
            fontElements[i].removeAttribute("size");
            fontElements[i].style.fontSize = "36px";
        } else if (fontElements[i].size == "6") {
            fontElements[i].removeAttribute("size");
            fontElements[i].style.fontSize = "48px";
        } else {
            fontElements[i].removeAttribute("size");
            fontElements[i].style.fontSize = "60px";
        }
    }
    edit.focus();

}

function centerAlign() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("justifyCenter", false, "");
    edit.focus();
}


function leftAlign() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("justifyLeft", false, "");
    document.querySelector('div').style.textAlign == "left";
    edit.focus();
}

function rightAlign() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("justifyRight", false, "");
    edit.focus();
}

function orderedList() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("insertOrderedList", false, "");
    edit.focus();
}

function unorderedList() {
    var edit = document.getElementById("textEditor").contentWindow;
    edit.focus();
    edit.document.execCommand("insertUnorderedList", false, "");
    edit.focus();
}

function indent_text() {
  var edit = document.getElementById("textEditor").contentWindow;
  edit.focus();
  edit.document.execCommand("indent", false, "");
  edit.focus();
}

function outdent_text() {
  var edit = document.getElementById("textEditor").contentWindow;
  edit.focus();
  edit.document.execCommand("outdent", false, "");
  edit.focus();
}








/*var el = document.getElementById("editorWindow");
if (el) {
    el.addEventListener('load', load(), false);
}

var x = document.getElementById('boldBtn');

x.addEventListener('click', function() {
    alert("helllo");
}, false);

function load() {
    getIFrameDocument('editorFrame').designMode = "On";
}

function getIFrameDocument(aID) {
    var iframe = document.getElementById(aID);
    var innerDoc = (iframe.contentDocument || iframe.contentwindow.document);
    if (innerDoc.getElementById(aID).contentDocument) {
        return innerDoc.getElementById(aID).contentDocument;
    } else {
        return innerDoc.frames[aID].document;
    }
}

function doRichEditCommand(aName, aArg) {
    document.execCommand(aName, false, aArg);
}



*/





/*
var btn = document.getElementById("boldBtn")
  if(btn) {
      btn.addEventListener('click', doRichEditCommand('bold'), false);
  }

function load() {
  getIFrameDocument('editorFrame').designMode = "On";
}

function getIFrameDocument(aID) {
  var iframe = document.getElementById(aID);
  var innerDoc = iframe.contentDocument || iframe.contentwindow.document;
  if(innerDoc.getElementById(aID).contentDocument) {
    return innerDoc.getElementById(aID).contentDocument;
  }
  else {
    return innerDoc.frames[aID].document;
  }
}

function doRichEditCommand(aName , aArg) {
document.execCommand(aName, false, aArg);
  innerDoc.getElementById('editorWindow').contentWindow.focus();
} */
