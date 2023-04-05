var logout;
var user_id;

window.onload = function () {
  logout = document.querySelector(".logout");

  //url에서 user_id 추출
  user_id = window.location.search.split("=")[1];

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
