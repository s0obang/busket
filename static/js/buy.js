document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.busket input[type="checkbox"]');
    const calContainer = document.querySelector('.sc2');
    const sumCostContainer = document.querySelector('.sum-cost span');
    const countContainer = document.querySelector('.add-btn .count');
    const addButton = document.querySelector('.add-button');

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
    addButton.addEventListener('click', function () {
        const selectedIds = [];

        checkboxes.forEach((checkbox) => {
            if (checkbox.checked) {
                const busket = checkbox.closest('.busket');
                const itemId = parseInt(busket.querySelector('.id').value, 10);
                selectedIds.push(itemId);
            }
        });

        if (selectedIds.length > 0) {
            fetch('/buket/buy/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({ selectedIds: selectedIds }), 
            })
                .then((response) => {
                    if (response.ok) {
                        alert('선택한 비스켓들이 성공적으로 추가되었습니다!');
                        window.location.reload();
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

    updateSelectedItems();
});
