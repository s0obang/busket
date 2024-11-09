// 비스켓 추가하는 함수
function addBusket(event) {
    const popup = document.querySelector('.popup'); // 팝업 요소 선택
    const overlay = document.createElement('div'); // 오버레이 생성
    overlay.className = 'overlay'; // 클래스 추가

    // 클릭한 요소가 'bu-add'인지 확인
    if (event.target.id === 'bu-add') {
        document.body.appendChild(overlay); // 오버레이를 body에 추가
        overlay.style.display = 'flex'; // 오버레이 보이기
        popup.style.display = 'block'; // 팝업 보이기

        // 오버레이 클릭 시 팝업 닫기
        overlay.addEventListener('click', function() {
            popup.style.display = 'none'; // 팝업 숨기기
            overlay.style.display = 'none'; // 오버레이 숨기기
            document.body.removeChild(overlay); // 오버레이 제거
                });
    } else {
        popup.style.display = 'none';
        overlay.style.display = 'none';    
    }

    // 팝업 닫기 버튼 클릭 시
    document.querySelector('.close-popup').addEventListener('click', function() {
    const popup = document.querySelector('.popup');
    const overlay = document.querySelector('.overlay');

    popup.style.display = 'none'; // 팝업 숨기기
    if (overlay) {
        overlay.style.display = 'none'; // 오버레이 숨기기
        document.body.removeChild(overlay); // 오버레이 제거
    }
});
    
}


function cateSelect(selectedButton) {
    // 모든 버튼 요소 선택
    const buttons = document.querySelectorAll(".pinkbox_top2");

    // 모든 버튼의 'selected' 클래스를 제거하여 배경색을 기본값으로 설정
    buttons.forEach(button => button.classList.remove("selected", "shadow"));

    // 선택된 버튼에만 'selected' 클래스를 추가하여 클릭 색상으로 변경
    selectedButton.classList.add("selected", "shadow");

    const categoryBoxes = document.querySelectorAll(".category-box");
    categoryBoxes.forEach(category => {
        category.style.display = "none"; // 모든 카테고리 창 숨기기
    });
    
    // 기본적으로 의류 카테고리 숨기기 (btn-cl 외의 다른 버튼을 눌렀을 때)
    const clothesDetail = document.querySelector(".clothes-u");
    if (clothesDetail) {
        clothesDetail.style.display = "none"; // 의류 카테고리 숨기기
    }
 
    // 선택된 버튼에 해당하는 카테고리 창만 보이게 설정
    if (selectedButton.id === "btn-cl") {
        const clothesDetail = document.querySelector(".clothes-u");
        if (clothesDetail) {
            clothesDetail.style.display = "block"; // 의류 카테고리 표시
        }
    } 
    else if (selectedButton.id === "btn-in") {
        const interiorDetail = document.querySelector(".interior-u");
        if (interiorDetail) {
            interiorDetail.style.display = "block"; // 인테리어 카테고리 표시
        }
    } 
    else if (selectedButton.id === "btn-go") {
        const goodsDetail = document.querySelector(".goods-u");
        if (goodsDetail) {
            goodsDetail.style.display = "block"; // 굿즈 카테고리 표시
        }
    } 
    else if (selectedButton.id === "btn-fo") {
        const foodDetail = document.querySelector(".food-u");
        if (foodDetail) {
            foodDetail.style.display = "block"; // 음식 카테고리 표시
        }
    } 
    else if (selectedButton.id === "btn-ho") {
        const hobbyDetail = document.querySelector(".hobby-u");
        if (hobbyDetail) {
            hobbyDetail.style.display = "block"; // 취미 카테고리 표시
        }
    } 
    else if (selectedButton.id === "btn-etc") {
        const etcDetail = document.querySelector(".etc-u");
        if (etcDetail) {
            etcDetail.style.display = "block"; // 기타 카테고리 표시
        }
    }
}

// 페이지 로드 시 기본 버튼(의류)을 활성화 상태로 시작
document.addEventListener('DOMContentLoaded', function () {
    const defaultButton = document.getElementById('btn-cl');
    cateSelect(defaultButton); // 기본적으로 '의류' 카테고리가 보이도록 설정
});


// function cateSelect(selectedButton) {
//     // 모든 버튼 요소 선택
//     const buttons = document.querySelectorAll(".pinkbox_top2");

//     // 카테고리 버튼 선택
//     // 모든 버튼의 'selected' 클래스를 제거하여 배경색을 기본값으로 설정
//     buttons.forEach(button => button.classList.remove("selected", "shadow"));

//     // 선택된 버튼에만 'selected' 클래스를 추가하여 클릭 색상으로 변경
//     selectedButton.classList.add("selected", "shadow");

//     // 카테고리에 해당하는 내용물 창 띄우기
//     const detailBase = document.querySelectorAll(".clothes-u");

//     // 각 카테고리 버튼의 data 속성이나 클래스를 확인해서 해당하는 클래스를 추가
//     if (selectedButton.classList.contains("btn-in")) {
//         detailBase.forEach(item => item.classList.remove("clothes-u"));
//         detailBase.classList.add("interior-u");
//     } 
    
//     else if  (selectedButton.classList.contains("btn-go")) {
//         detailBase.forEach(item => item.classList.remove("clothes-u"));
//         detailBase.classList.add("goods-u");
//     } 
    
//     else if (selectedButton.classList.contains("btn-fo")) {
//         detailBase.forEach(item => item.classList.remove("clothes-u"));
//         detailBase.classList.add("food-u");
//     } 
    
//     else if  (selectedButton.classList.contains("btn-ho")) {
//         detailBase.forEach(item => item.classList.remove("clothes-u"));
//         detailBase.classList.add("hobby-u"); 
//     }

//     else {
//         detailBase.forEach(item => item.classList.remove("clothes-u"));
//         detailBase.classList.add("etc-u");
//     }

//   };
