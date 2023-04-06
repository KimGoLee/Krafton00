var modal;
var exit;
var logo;
var user_id;
var login = "false";

//페이지가 처음 실행될 때 하는 일들
window.onload = function () {
  modal = document.querySelector(".modal");
  exit = document.querySelector(".exit");
  logo = document.querySelector(".title_logo");
  user_id = window.location.search.split("=")[1];

  exit.addEventListener("click", () => {
    modal.style.display = "none";
  });

  logo.addEventListener("click", () => {
    login = "true";
    window.location.href = "/main?user_id=" + user_id;
  });
};

function see_user(user_id) {
  $.ajax({
    type: "POST",
    url: "/user_info",
    data: {
      give_user_id: user_id,
    },
    success: function (response) {
      if (response["result"] == "success") {
        console.log(response["name"]);
        document.querySelector(".modal_name").innerHTML =
          "이름 " + response["name"];
        document.querySelector(".modal_phnum").innerHTML =
          "전화번호 " + response["phnum"];
        document.querySelector(".modal_room").innerHTML =
          "호수 " + response["room"];
        document.querySelector(".modal_team").innerHTML =
          "팀 " + response["team"];
        document.querySelector(".modal_email").innerHTML =
          "이메일 " + response["email"];
        document.querySelector(".modal_blog").innerHTML =
          "블로그 " + response["blog"];
        document
          .querySelector(".modal_blog")
          .setAttribute("href", response["blog"]);
        // document.querySelector(".modal_time").innerHTML =
        //   response["hour"] + " h : " + response["min"] + " m";
        document.querySelector(".profile_img").src =
          "./static/images/" + response["email"] + ".jpg";
        modal.style.display = "block";
      }
    },
  });
}
