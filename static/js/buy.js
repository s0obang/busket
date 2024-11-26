document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.busket input[type="checkbox"]');
    const calContainer = document.querySelector('.sc2'); 
    const sumCostContainer = document.querySelector('.sum-cost span'); 
    const countContainer = document.querySelector('.add-btn .count'); 

    function updateSelectedItems() {
        const existingCals = calContainer.querySelectorAll('.cal');
        existingCals.forEach((cal) => cal.remove());

        let totalCost = 0;
        let selectedCount = 0; 

        checkboxes.forEach((checkbox) => {
            if (checkbox.checked) {
                const busket = checkbox.closest('.busket'); 
                const itemName = busket.querySelector('.item-name').innerText; 
                const itemCost = parseFloat(busket.querySelector('img').getAttribute('data-price')) || 0; 

                const calItem = document.createElement('div');
                calItem.classList.add('cal');
                calItem.innerHTML = `
                    <div class="name">
                        <h2>${itemName}</h2>
                    </div>
               
                    <div class="cost">
                        <h2>+ <span>${itemCost.toLocaleString()}</span></h2>
                    </div>
                `;

                calContainer.insertBefore(calItem, calContainer.querySelector('.sum-cost'));

                totalCost += itemCost;
                selectedCount++;
            }
        });

        sumCostContainer.innerText = totalCost.toLocaleString();
        countContainer.innerText = selectedCount;
    }

    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', updateSelectedItems);
    });

    updateSelectedItems();
});



//여기는 챗지피티가 짠 백엔드로 체크한 비스켓 배열을 전송하는 js 


document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.busket input[type="checkbox"]');
    const addButton = document.querySelector('.add-btn button'); // ADD 버튼

    addButton.addEventListener('click', function () {
        // 체크된 항목들의 정보를 수집
        const selectedItems = [];
        checkboxes.forEach((checkbox) => {
            if (checkbox.checked) {
                const busket = checkbox.closest('.busket'); // 해당 busket div
                const itemName = busket.querySelector('.item-name').innerText; // 비스켓 이름

                selectedItems.push({
                    name: itemName,

                });
            }
        });

        // 서버에 데이터 전송
        if (selectedItems.length > 0) {
            fetch('/add-selected-items/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'), // CSRF 토큰 추가
                },
                body: JSON.stringify({ selectedItems: selectedItems }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.success) {
                        alert('선택한 비스켓들이 성공적으로 추가되었습니다!');
                        location.reload(); // 페이지 새로고침
                    } else {
                        alert('문제가 발생했습니다. 다시 시도해주세요.');
                    }
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        } else {
            alert('선택한 비스켓이 없습니다.');
        }
    });

    // CSRF 토큰 가져오기 함수
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

