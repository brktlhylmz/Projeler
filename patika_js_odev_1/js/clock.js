let a = document.getElementById("myName");
let isim = prompt("İsim giriniz: ")
a.innerHTML=isim
let günler = ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]
let zaman = new Date();
let gün = zaman.getDay();
let hh = zaman.getHours();
let dk = zaman.getMinutes();
let sn = zaman.getSeconds();
let göster = `${hh}:${dk}:${sn} ${günler[gün-1]}`
let saat = document.getElementById("myClock");
saat.innerHTML=göster