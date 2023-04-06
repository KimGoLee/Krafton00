var logout;
var user_id;
var btn_rank;
var btn_start;
var hour;
var min;

var ms = 0;
var sec = 0;
var min = 0;
var hr = 0;
var tt = 0;
var login = "false";

//페이지가 처음 실행될 때 하는 일들
window.onload = function () {
  logout = document.querySelector(".logout");
  btn_rank = document.querySelector(".rank");
  btn_start = document.querySelector(".btn_start");

  //url에서 user_id 추출
  user_id = window.location.search.split("=")[1];

  logout.addEventListener("click", () => {
    login = "true";
    $.ajax({
      type: "POST",
      url: "/logout",
      data: { give_user_id: user_id },
      success: function (response) {
        if (response["result"] == "success") {
          window.location.href = "/";
        } else {
          alert("서버 오류!");
        }
      },
    });
  });

  btn_rank.addEventListener("click", () => {
    //stop하는 경우 reload될 때 session이 만료되면 안됨
    login = "true";
    window.location.href = "/rank?user_id=" + user_id;
  });

  // btn_start.addEventListener("click", cal_time());
};

function cal_time() {
  timer_status = btn_start.getAttribute("id");
  console.log(timer_status);
  if (timer_status == "stop") {
    btn_start.setAttribute("id", "start");
    btn_start.innerText = "Stop";
    startTimer = setInterval(() => {
      ms++;
      ms = ms < 10 ? "0" + ms : ms;

      if (ms == 100) {
        sec++;
        sec = sec < 10 ? "0" + sec : sec;
        ms = "0" + 0;
      }
      if (sec == 60) {
        min++;
        min = min < 10 ? "0" + min : min;
        sec = "0" + 0;
      }
      if (min == 60) {
        hr++;
        hr = hr < 10 ? "0" + hr : hr;
        min = "0" + 0;
      }
      putValue(ms, sec, min, hr);
    }, 10); //1000ms = 1s
  } else {
    tt = 3600 * Number(hr) + 60 * Number(min) + Number(sec);
    clearInterval(startTimer);
    hr = min = sec = ms = "0" + 0;
    putValue(ms, sec, min, hr);
    btn_start.setAttribute("id", "stop");
    btn_start.innerText = "Start";

    $.ajax({
      type: "POST",
      url: "/update_time",
      data: { give_user_id: user_id, give_time: tt },
      success: function (response) {
        if (response["result"] == "success") {
          //stop하는 경우 reload될 때 session이 만료되면 안됨
          login = "true";
          window.location.href = "/main?user_id=" + user_id;
        }
      },
    });
  }
}

function putValue() {
  document.querySelector(".millisecond").innerText = ms;
  document.querySelector(".second").innerText = sec;
  document.querySelector(".minute").innerText = min;
  document.querySelector(".hour").innerText = hr;
}

$(window).on("beforeunload", function () {
  tt = 3600 * Number(hr) + 60 * Number(min) + Number(sec);

  // Send the data to the server using AJAX
  $.ajax({
    url: "/main_close",
    type: "POST",
    data: { give_time: tt, give_user_id: user_id, give_login: login },
    success: function (data) {
      console.log("Data saved successfully");
    },
    error: function () {
      console.log("Error saving data");
    },
  });
});
