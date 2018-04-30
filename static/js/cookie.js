function getCookie(cname) {
	console.log("called for cookie with " + cname);
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";path=/";
}

function deleteCookie(cname) {
document.cookie = cname+ "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

function emptyCart(){
    deleteCookie('orderList');
    deleteCookie('totalAmnt');
    $("#simpleCart_total").html("0.00");
    $("#simpleCart_quantity").html("0");
       
}

