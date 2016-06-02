// ==UserScript==
// @name        Auto_refresh_and_alert
// @namespace
// @description PLM自动刷新提醒
// @author      Bluethon
// @supportURL
// @include     http://plmprd.sfdomain.com/Windchill/*
// @version     0.01
// @grant       none
// ==/UserScript==

// @include     http://plmqas.sfdomain.com/Windchill/*
// @include     http://plmprd.sfdomain.com/Windchill/*

//----参数设置--------
// 刷新间隔, 10s
var time = 10;
// 查找内容, 触发提醒
var find = 'B000000542';
//定位ID, 未知勿动
var element_ID = 'ext-gen187';

//-------------------
// 是否刷新
var refresh = true;

(function () {
    //if (document.getElementsByTagName('div') [0].getAttribute('id') == 'errorPageContainer') {
    setTimeout(function() {
        var all = document.getElementById(element_ID).getElementsByTagName('a');
        var thisElement;
        for (var i = 0; i < all.length; i++) {
            if (all[i].innerHTML == find) {
                thisElement = all[i];
                refresh = false;
                alert(thisElement);
            }
        }
        if (refresh === true) {
            setTimeout(function () {
                window.location.reload(true);
            }, time * 1000);
        }
    }, 3 * 1000);
}
)();
