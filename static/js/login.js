var modal;
var join;
var login;
var exit;
var save;

/* onload 될 때마다 하는일
1. 이벤트 리스너를 만든다
*/
window.onload = function () {
  join = document.querySelector(".join");
  login = document.querySelector(".login");
  exit = document.querySelector(".exit");
  save = document.querySelector(".save");

  login.addEventListener("click", () => {
    const email = document.querySelector(".email").value;
    const password = document.querySelector(".password").value;
    console.log(email, password);
    $.ajax({
      type: "POST",
      url: "/login", // 보낼 서버의 url
      data: {
        give_email: email,
        give_password: password,
      },
      success: function (response) {
        if (response["result"] == "success") {
          alert("로그인 완료");
          window.location.href = "/main?user_id=" + response["user_id"];
        } else {
          alert("로그인 실패");

          window.location.reload();
        }
      },
    });
  });

  // join eventListener
  join.addEventListener("click", () => {
    document.querySelector(".modal").style.display = "block";
  });
  // ÷
  // exit eventListener
  exit.addEventListener("click", () => {
    initialize_modal();
  });

  // save eventListener
  save.addEventListener("click", () => {
    const name = document.querySelector(".join_name").value;
    const phnum = document.querySelector(".join_phnum").value;
    const room = document.querySelector(".join_room").value;
    const team = document.querySelector(".join_team").value;
    const email = document.querySelector(".join_email").value;
    const pw = document.querySelector(".join_pw").value;
    const blog = document.querySelector(".join_blog").value;

    // console.log(name, phnum, room, team, email, pw, blog);
    $.ajax({
      type: "POST",
      url: "/save", // 보낼 서버의 url
      data: {
        give_name: name,
        give_phnum: phnum,
        give_room: room,
        give_team: team,
        give_email: email,
        give_pw: pw,
        give_blog: blog,
      },
      success: function (response) {
        if (response["result"] == "fail") {
          alert("서버 오류!");
          window.reload();
        } else {
          alert("회원가입 완료!");
          initialize_modal();
          window.reload();
        }
      },
    });
  });

  //modal 창 초기화
  function initialize_modal() {
    document.querySelector(".join_name").value = null;
    document.querySelector(".join_phnum").value = null;
    document.querySelector(".join_room").value = null;
    document.querySelector(".join_team").value = null;
    document.querySelector(".join_email").value = null;
    document.querySelector(".join_pw").value = null;
    document.querySelector(".join_blog").value = null;
    document.querySelector(".modal").style.display = "none";
  }
};
