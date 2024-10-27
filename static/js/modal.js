document.addEventListener('DOMContentLoaded', () => {
    // 모달 관련 요소 선택
    const loginLogoutModal = document.querySelector('.login_logout_modal');
    const loginModal = document.querySelector('.login_modal');
    const signinModal = document.querySelector('.signin_modal');
    const profileModal = document.querySelector('.profile_modal');

    // 버튼 요소 선택
    const loginLogoutBtn = document.querySelector('.login_logout_btn');
    const loginBtn = document.querySelector('.login_btn');
    const signinBtn = document.querySelector('.signin_btn');
    const profileBtn = document.querySelector('.profile_btn');
    const logoutBtn = document.querySelector('.logout_btn');

    const closeButtons = document.querySelectorAll('.close');

    // 모달 열기 함수
    function openModal(modal) {
        // 모든 모달을 닫고 시작 (다른 모달과 겹치는 문제 방지)
        document.querySelectorAll('.modal_box').forEach(m => m.classList.remove('active'));
        modal.classList.add('active');
    }

    // 모달 닫기 함수
    function closeModal(modal) {
        modal.classList.remove('active');
    }

    // 로그인/로그아웃 모달 열기
    loginLogoutBtn.addEventListener('click', () => openModal(loginLogoutModal));

    // 로그인 버튼 클릭 시: 로그인/로그아웃 모달 닫고 로그인 모달 열기
    loginBtn.addEventListener('click', () => {
        closeModal(loginLogoutModal);
        openModal(loginModal);
    });

    // 회원가입 버튼 클릭 시: 로그인/로그아웃 모달 닫고 회원가입 모달 열기
    signinBtn.addEventListener('click', () => {
        closeModal(loginLogoutModal);
        openModal(signinModal);
    });

    // 프로필 수정 모달 열기
    profileBtn.addEventListener('click', () => openModal(profileModal));

    // 로그아웃 버튼 클릭 시: 로그인/로그아웃 모달 닫기
    logoutBtn.addEventListener('click', () => closeModal(loginLogoutModal));

    // 모든 닫기 버튼에 이벤트 추가: 모달 닫기
    closeButtons.forEach((btn) =>
        btn.addEventListener('click', () => {
            const modal = btn.closest('.modal_box');
            closeModal(modal);
        })
    );

});
