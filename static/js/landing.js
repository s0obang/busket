document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("closebtn").addEventListener("click", function () {
        const checkbox = document.getElementById("confirmcheckbox");
        if (checkbox.checked) {
            document.querySelector(".popup").style.display = "none";
            window.location.href = "/";
        } else {
            alert("다시 보지 않기를 체크해 주세요.");
        }
    });
});
