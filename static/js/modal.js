document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.modal_btn');
    const modals = document.querySelectorAll('.modal_box');
    const closeButtons = document.querySelectorAll('.close');
  
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const classList = this.classList;
            modals.forEach(modal => {
                classList.forEach(className => {
                    if (modal.classList.contains(className.replace('_btn', '_modal'))) {
                        modal.classList.add('active');
                    }
                });
            });
        });
    });
  
    closeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const modal = this.closest('.modal_box'); // 가장 가까이 있는 모달박스 선택
            modal.classList.remove('active'); //active 제거
        });
    });
  });