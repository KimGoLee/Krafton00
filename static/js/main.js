var logout;
var user_id;

//페이지가 처음 실행될 때 하는 일들
window.onload = function () {
  logout = document.querySelector(".logout");
  //url에서 user_id 추출
  user_id = window.location.search.split("=")[1];

  $.ajax({
    type: "POST",
    url: "/user_info",
    data: {
      give_user_id: user_id,
    },
    success: function (response) {
      if (response["result"] == "success") {
        document.querySelector(".name").innerHTML =
          "이름 : " + response["name"];
        document.querySelector(".phnum").innerHTML =
          "전화번호 : " + response["phnum"];
        document.querySelector(".room").innerHTML =
          "호수 : " + response["room"];
        document.querySelector(".team").innerHTML = "팀 : " + response["team"];
        document.querySelector(".email").innerHTML =
          "이메일 : " + response["email"];
        document.querySelector(".blog").innerHTML =
          "블로그 : " + response["blog"];
      }
    },
  });

  logout.addEventListener("click", () => {
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
};

// user_id값으로 사용자 정보 요청
// $.ajax({
//   type: "GET",
//   url: "/user_info",
//   data: {
//     give_user_id: user_id,
//   },
//   success: function (response) {
//     if (response["result"] == "success") {
//       phnum.style.value()=response['phnum'];
//       room.style.value()=response['room'];
//       team.style.value()=response['team'];
//       email.style.value()=response['email'];
//       blog.style.value()=response['blog'];
//       time.style.value()=response['time'];
//       name.styel.value()=response['name']

//     } else {
//       //사용자의 정보를 불러오는데 실패하였다면 logout을 통해 메인 창으로
//       alert("로그인 실패");
//       $.ajax({
//         type: "POST",
//         url: "/logout",
//         data: { give_user_id: user_id },
//         success: function (response) {
//           if (response["result"] == "success") {
//             window.location.href = "/";
//           }
//         },
//       });
//     }
//   },
// });
